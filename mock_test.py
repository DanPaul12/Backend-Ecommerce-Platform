import unittest
from unittest.mock import MagicMock, patch
from faker import Faker
from werkzeug.security import generate_password_hash
from app import create_app
from services.customerAccountService import login_customer
from services.customerService import find_all, save
from models.customer import Customer

class TestLoginCustomer(unittest.TestCase):


    @patch('services.customerAccountService.db.session.execute')
    def test_login_customer(self, mock_customer):

        faker = Faker()
        mock_user = MagicMock()
        mock_user.id = 1
        mock_user.roles = [MagicMock(role_name='admin'), MagicMock(role_name='user')]
        password = faker.password()
        mock_user.username = faker.user_name()
        mock_user.password = generate_password_hash(password)
        mock_customer.return_value.scalar_one_or_none.return_value = mock_user

        response = login_customer(mock_user.username, password)

        self.assertEqual(response['status'], 'success')



class TestCustomerEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app('DevelopmentConfig')
        self.app_context = self.app.app_context()
        self.app_context.push()
    @patch('services.customerService.Session')
    #@patch('services.customerService.db')
    def test_saave_customer(self, mock_session):
        customer = {'name':'dan', 'email':'dan@gmail.com','phone':'123123123'}
        mock_session.return_value.__enter__.return_value = mock_session
        #mock_session_instance.add = MagicMock()

        response = save(customer)
        #call_arguments = mock_session_instance.add.call_args[0][0]
        #mock_session_instance.add.assert_called_once()
        self.assertEqual(response.name, customer['name'])
        self.assertEqual(response.email, customer['email'])
        self.assertEqual(response.phone, customer['phone'])

    @patch('services.customerService.db.session.execute')
    def test_find_customers(self, mock_execute):
        mock_customer1 = MagicMock(spec=Customer)
        mock_customer1.id = 1
        mock_customer1.name = "dan"
        mock_customer1.email = "dan@@gmail.com"
        mock_customer1.phone = "1231231233"

        mock_customer2 = MagicMock(spec=Customer)
        mock_customer2.id = 2
        mock_customer2.name = "doon"
        mock_customer2.email = "hank@@gmail.com"
        mock_customer2.phone = "34245631233"
        mock_customers = [mock_customer1, mock_customer2]

        mock_execute.return_value.scalars.return_value.all.return_value = mock_customers
        customers = find_all()
        self.assertEqual(len(customers), len(mock_customers))
        self.assertEqual(customers[0].name, mock_customer1.name)
    

if __name__ == '__main__':
    unittest.main()