This is a back-end flask application that can be used for a small e-commerce business. It includes API endpoints for
adding, deleting, updating, and viewing one or all customers, customer accounts, products, and orders by communicating with a database.
It has login functionality for each account, and the ability to assign different accounts to different roles. Certain actions (like viewing all
customers) are only allowed if a user is logged in (by using jwt authentication), and still others are only permitted for certain roles. All requirements
are documented in the requirements.txt file, and api documentation is provided through the swagger.yaml file.
This app is integrated with a postgresql database and is deployed through render. It is equipped with a CI/CD pipeline, ensuring that any changes
made are tested, and if they pass, are automatically deployed. 
