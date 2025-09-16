  easyAuth: A Simple FastAPI User Authentication System @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Poppins:wght@500;600&display=swap'); body { font-family: 'Roboto', sans-serif; background-color: #f3f4f6; color: #1f2937; } .container { max-width: 900px; margin: 0 auto; padding: 2rem; } .header { text-align: center; margin-bottom: 2.5rem; } .header h1 { font-family: 'Poppins', sans-serif; font-size: 2.5rem; font-weight: 700; color: #111827; text-shadow: 1px 1px 2px rgba(0,0,0,0.1); } .header p { font-size: 1.125rem; color: #4b5563; } .section-title { font-family: 'Poppins', sans-serif; font-size: 2rem; font-weight: 600; color: #1f2937; border-bottom: 2px solid #3b82f6; padding-bottom: 0.5rem; margin-bottom: 1.5rem; } .feature-list { list-style: none; padding: 0; display: grid; gap: 1.5rem; } .feature-item { background-color: #ffffff; border: 1px solid #e5e7eb; border-radius: 0.75rem; padding: 1.5rem; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05); transition: transform 0.2s; } .feature-item:hover { transform: translateY(-5px); } .feature-item h3 { font-weight: 600; font-size: 1.25rem; margin-bottom: 0.5rem; } .code-block { background-color: #111827; color: #f9fafb; padding: 1rem; border-radius: 0.5rem; overflow-x: auto; font-family: monospace; white-space: pre; } .api-endpoint { background-color: #ffffff; border: 1px solid #e5e7eb; border-radius: 0.75rem; padding: 1.5rem; margin-bottom: 1rem; } .method-badge { display: inline-block; padding: 0.25rem 0.75rem; border-radius: 9999px; font-weight: 700; font-size: 0.75rem; margin-right: 0.5rem; } .method-get { background-color: #dbeafe; color: #1e40af; } .method-post { background-color: #d1fae5; color: #065f46; } .method-put { background-color: #fef3c7; color: #92400e; } .method-delete { background-color: #fee2e2; color: #991b1b; } .footer { text-align: center; margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #e5e7eb; color: #6b7280; }

# 🚀 easyAuth: A Simple FastAPI User Authentication System

A simple, robust user authentication system with a full-stack implementation using FastAPI and a dynamic admin panel.

- - -

## ✨ Features

*   ### User Authentication
    
    Secure login and logout functionality using JWTs stored in HTTP-only cookies.
    
*   ### Password Hashing
    
    Passwords are \*\*securely hashed\*\* using \`bcrypt\` via the \`passlib\` library.
    
*   ### Role-Based Access Control
    
    Authenticated users have basic access, while admin users have exclusive access to a full user management system.
    
*   ### Admin Panel
    
    A dynamic, single-page admin interface for viewing, creating, updating, and deleting users directly from the browser.
    
*   ### SQLite Database
    
    Uses \`SQLAlchemy\` with a local SQLite database for simplicity, perfect for development and small-scale applications.
    
*   ### Automated Setup
    
    The application automatically creates the database and a default admin user on startup.
    

- - -

## ⚙️ Getting Started

### Prerequisites

*   Python 3.7+
*   \`pip\` package manager

### Installation

1.  Clone the repository or download the project files.
2.  Navigate to the \`auth\` directory.
3.  Install the required Python packages:
    
    pip install fastapi "uvicorn\[standard\]" sqlalchemy passlib\[bcrypt\] python-jose "python-multipart" jinja2 pydantic
    

### Running the Application

1.  Navigate to the \`auth\` directory.
2.  Start the application with Uvicorn:
    
    python main.py
    

The application will run on \`http://127.0.0.1:80\`.

### Default Admin Account

On first run, a default admin account is created:

*   **Username**: \`admin\`
*   **Password**: \`password123\`

- - -

## ⚡ API Endpoints

This section provides a comprehensive overview of the available API endpoints.

### Authentication Endpoints

These endpoints are used for user login and logout, managing the authentication cookie.

POST

#### /token

Authenticates a user and issues an access token. The token is stored in a secure, HTTP-only cookie.

##### Request Body (Form Data)

username: string  
password: string

##### Success Response

// Status: 200 OK  
{  
  "message": "Login successful",  
  "is\_admin": true  
}

POST

#### /api/logout

Logs the current user out by deleting their authentication cookie.

##### Success Response

// Status: 200 OK  
{  
  "message": "Logged out successfully"  
}

### User Endpoints (Authenticated)

These endpoints are accessible to any logged-in user with a valid authentication cookie.

GET

#### /api/me

Fetches the details of the currently authenticated user.

##### Success Response

// Status: 200 OK  
{  
  "username": "user123",  
  "is\_admin": false,  
  "profile\_picture\_url": "https://example.com/profile.jpg"  
}

### Admin Endpoints (Admin Only)

These endpoints require admin privileges and a valid authentication cookie.

GET

#### /api/admin/users

Retrieves a list of all users in the system.

##### Success Response

// Status: 200 OK  
\[  
  { "id": 1, "username": "admin", "is\_admin": true, "profile\_picture\_url": "..." },  
  { "id": 2, "username": "user1", "is\_admin": false, "profile\_picture\_url": "..." }  
\]

POST

#### /api/admin/users

Creates a new user.

##### Request Body

{  
  "username": "newuser",  
  "password": "strongpassword",  
  "is\_admin": false,  
  "profile\_picture\_url": "https://example.com/newuser.jpg"  
}

##### Success Response

// Status: 200 OK  
{ "message": "User created successfully", "user\_id": 3 }

DELETE

#### /api/admin/users/{user\_id}

Deletes a user by their ID. You cannot delete your own admin account.

##### Success Response

// Status: 200 OK  
{ "message": "User deleted successfully" }

PUT

#### /api/admin/users/{user\_id}

Updates an existing user. Accepts partial updates (e.g., you can just change the password or profile picture).

##### Request Body (Partial)

{  
  "password": "a-new-password",  
  "profile\_picture\_url": "https://new-url.com/picture.jpg"  
}

##### Success Response

// Status: 200 OK  
{ "message": "User updated successfully" }

- - -

## 🎨 Frontend

The frontend is served from the \`templates/\` directory.

*   \`GET /\`: Serves the \`index.html\` login page.
*   \`GET /authorized/{filepath:path}\`: Serves protected HTML pages from the \`templates/authorized/\` directory after a successful login.

The \`index.html\` page uses JavaScript to handle form submissions and dynamically show/hide different panels based on user actions and administrative privileges. It uses \`fetch\` to interact with the backend API endpoints.

- - -

## 📦 Dependencies

*   \`fastapi\`: Web framework for building the API.
*   \`uvicorn\`: ASGI server for running the FastAPI application.
*   \`sqlalchemy\`: ORM for database interactions.
*   \`passlib\`: For password hashing and verification.
*   \`python-jose\`: For handling JWT token creation and decoding.
*   \`python-multipart\`: For parsing form data.
*   \`jinja2\`: For rendering HTML templates.
*   \`pydantic\`: For data validation with FastAPI models.

© 2025 easyAuth Project. All rights reserved.
