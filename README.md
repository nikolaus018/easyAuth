# FastAPI User Authentication and Admin Panel

This project is a a simple yet robust user authentication system built with **FastAPI**. It includes user login/logout, a secure session management using HTTP-only cookies, and an admin panel for managing users. The frontend is built with vanilla HTML, CSS (TailwindCSS via CDN), and JavaScript, demonstrating a full-stack application. A great aspect of this project is the ability to easily add authentication to any HTML files by placing them in the `authenticated` folder.

## Features

* **User Authentication**: Secure login and logout functionality using JWTs stored in HTTP-only cookies.
* **Password Hashing**: Passwords are securely hashed using `bcrypt` via the `passlib` library.
* **Role-Based Access Control**:
    * Authenticated users can access a profile page (`/authorized/index.html`) and their own data via the `/api/me` endpoint.
    * Admin users have exclusive access to the admin panel and a set of API endpoints for managing users.
* **Admin Panel**: A single-page application (SPA) style admin interface allows administrators to:
    * View all users.
    * Create new users (with an option to grant admin status).
    * Delete users (with a restriction to prevent self-deletion).
    * Update user information, including username, password, admin status, and profile picture URL.
* **SQLite Database**: Uses `SQLAlchemy` with a local SQLite database for simplicity, which is perfect for development and small-scale applications.
* **Automated Setup**: The application automatically creates the database and a default admin user on startup.

---

## Project Structure

.
├── auth.zip
│   ├── main.py
│   ├── documentation.html
│   └── templates/
│       ├── index.html
│       └── authorized/
│           └── index.html
└── README.md


### File Descriptions

* `main.py`: The core FastAPI application. It defines all the API endpoints, database models, security dependencies, and serves the HTML templates.
* `documentation.html`: A static HTML file providing simple, human-readable API documentation.
* `templates/index.html`: The main login page with client-side JavaScript for handling login, and a dynamic admin panel for managing users.
* `templates/authorized/index.html`: A protected page that displays the currently logged-in user's profile information.

---

## Getting Started

### Prerequisites

* Python 3.7+
* `pip` package manager

### Installation

1.  Clone the repository or download the project files.
2.  Navigate to the `auth` directory.
3.  Install the required Python packages:

    ```bash
    pip install fastapi "uvicorn[standard]" sqlalchemy passlib[bcrypt] python-jose "python-multipart" jinja2 pydantic
    ```

### Running the Application

1.  Navigate to the `auth` directory.
2.  Start the application with Uvicorn:

    ```bash
    python main.py
    ```

The application will run on `http://127.0.0.1:80`.

### Default Admin Account

On first run, a default admin account is created:

* **Username**: `admin`
* **Password**: `password123`

---

## API Endpoints

The API includes endpoints for both general users and administrators. The full documentation for the API can be found in `documentation.html`.

### Authentication Endpoints

* **`POST /token`**: Authenticates a user and sets an `access_token` cookie.
    * **Body**: `username` (form data), `password` (form data)
* **`POST /api/logout`**: Logs out the current user by deleting the `access_token` cookie.

### User Endpoints (Authenticated)

* **`GET /api/me`**: Retrieves the details of the currently authenticated user.

### Admin Endpoints (Admin Only)

* **`GET /api/admin/users`**: Lists all users in the system.
* **`POST /api/admin/users`**: Creates a new user.
    * **Body**: `username`, `password`, `is_admin`, `profile_picture_url`
* **`DELETE /api/admin/users/{user_id}`**: Deletes a specific user by ID.
* **`PUT /api/admin/users/{user_id}`**: Updates an existing user.
    * **Body**: Accepts a partial JSON body with any of the user fields to be updated.

---

## Frontend

The frontend is served from the `templates/` directory.

* `GET /`: Serves the `index.html` login page.
* `GET /authorized/{filepath:path}`: Serves protected HTML pages from the `templates/authorized/` directory after a successful login.

The `index.html` page uses JavaScript to handle form submissions and dynamically show/hide different panels based on user actions and administrative privileges. It uses `fetch` to interact with the backend API endpoints.

---

## Dependencies

* `fastapi`: Web framework for building the API.
* `uvicorn`: ASGI server for running the FastAPI application.
* `sqlalchemy`: ORM for database interactions.
* `passlib`: For password hashing and verification.
* `python-jose`: For handling JWT token creation and decoding.
* `python-multipart`: For parsing form data.
* `jinja2`: For rendering HTML templates.
* `pydantic`: For data validation with FastAPI models.
