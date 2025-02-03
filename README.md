# DRF Authentication API

A robust Django REST Framework (DRF) based authentication API that provides secure user authentication and authorization functionality.

## Features

- User Registration and Authentication
- JWT (JSON Web Token) based authentication
- Secure password handling
- RESTful API endpoints
- Built with Django 5.0.1 and DRF 3.14.0

## Prerequisites

- Python 3.x
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd drf-auth-api
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory and add your configuration:
```env
SECRET_KEY=your_secret_key
DEBUG=True
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

## Project Structure

```
drf-auth-api/
├── api/                # Main API application
├── core/               # Core application
├── manage.py          # Django management script
└── requirements.txt   # Project dependencies
```

## API Endpoints

The API provides the following endpoints:

- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `POST /api/auth/token/refresh/` - Refresh JWT token
- `GET /api/auth/user/` - Get user details

## Dependencies

- Django (5.0.1)
- Django REST Framework (3.14.0)
- djangorestframework-simplejwt (5.3.1)
- python-dotenv (1.0.0)

## Security

- Uses JWT for secure authentication
- Implements password hashing
- Environment variables for sensitive data

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository.
