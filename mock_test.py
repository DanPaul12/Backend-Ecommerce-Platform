import unittest
from unittest.mock import MagicMock, patch
from faker import Faker
from werkzeug.security import generate_password_hash
from services.customerAccountService import login_customer
from services.customerService import save

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



class TestSaveCustomer(unittest.TestCase):
    @patch('services.customerService.Session')
    @patch('services.customerService.db')
    def test_saave_customer(self, mock_db, mock_session):
        customer = {'name':'dan', 'email':'dan@gmail.com','phone':'123123123'}
        mock_session_instance = mock_session.return_value.__enter__.return_value
        mock_session_instance.add = MagicMock()

        save(customer)
        call_arguments = mock_session_instance.add.call_args[0][0]
        mock_session_instance.add.assert_called_once()
        self.assertEqual(call_arguments.name, customer['name'])

if __name__ == '__main__':
    unittest.main()