# Backend E-Commerce Platform

## Overview
This backend system powers an e-commerce platform, managing customers, accounts, products, and orders. Built with Flask, the system ensures secure authentication, scalable architecture, and smooth integration with frontend and database components. A CI/CD pipeline ensures rapid and reliable deployment, making it suitable for production-level applications.

## Features

- **Comprehensive Data Management**: Supports CRUD operations for customers, accounts, products, and orders.
- **Secure Authentication**: Implements role-based access control with JWT for secure API access.
- **Modular Design**: Well-structured modules for scalability and maintainability.
- **Automated Workflows**: CI/CD pipeline for streamlined testing and deployment.

## Technologies Used

- Flask (Python)
- SQLAlchemy
- PostgreSQL
- JWT for authentication
- Docker for containerization
- GitHub Actions for CI/CD

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/DanPaul12/Backend-Ecommerce-Platform
   ```

2. Navigate to the project directory:
   ```bash
   cd Backend-Ecommerce-Platform
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Configure database connection details in the `config.py` file.
   - Run migrations to initialize the database schema:
     ```bash
     flask db upgrade
     ```

5. Start the server:
   ```bash
   flask run
   ```

6. The API will be available at `http://localhost:5000`.

## API Endpoints

### Authentication
- `POST /auth/login`: Logs in a user and returns a JWT.
- `POST /auth/register`: Registers a new user.

### Customers
- `GET /customers`: Retrieves a list of customers.
- `POST /customers`: Adds a new customer.

### Products
- `GET /products`: Retrieves a list of products.
- `POST /products`: Adds a new product.

### Orders
- `GET /orders`: Retrieves a list of orders.
- `POST /orders`: Creates a new order.

## CI/CD Pipeline
- **Testing**: Automated unit tests run on every commit.
- **Deployment**: Dockerized application deployed seamlessly using GitHub Actions.

## Future Enhancements
- Implement advanced analytics and reporting features.
- Integrate payment gateways for real-time order processing.
- Add support for multiple languages and currencies.


