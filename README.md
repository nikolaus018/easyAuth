# 🚀 easyAuth: A Simple FastAPI User Authentication System

This project is a simple yet robust user authentication system built with **FastAPI**. It includes user login/logout, secure session management using HTTP-only cookies, and an admin panel for managing users. The frontend is built with vanilla HTML, CSS (TailwindCSS via CDN), and JavaScript, demonstrating a full-stack application.

A key strength of easyAuth is the ability to **easily add authentication to any HTML files** simply by placing them in the `authorized` folder.

---

## ✨ Features

* **User Authentication**: Secure login and logout functionality using JWTs stored in HTTP-only cookies.
* **Password Hashing**: Passwords are **securely hashed** using `bcrypt` via the `passlib` library.
* **Role-Based Access Control**:
    * Authenticated users can access a profile page (`/authorized/index.html`) and their own data via the `/api/me` endpoint.
    * Admin users have **exclusive access** to the admin panel and a set of API endpoints for managing users.
* **Admin Panel**: A single-page application (SPA) style admin interface allows administrators to:
    * 👀 View all users.
    * ➕ Create new users (with an option to grant admin status).
    * 🗑️ Delete users (with a restriction to prevent self-deletion).
    * ✏️ Update user information, including username, password, admin status, and profile picture URL.
* **SQLite Database**: Uses `SQLAlchemy` with a local SQLite database for simplicity, which is perfect for development and small-scale applications.
* **Automated Setup**: The application automatically creates the database and a default admin user on startup.

---

## ⚙️ Getting Started

### Prerequisites
* Python 3.7+
* `pip` package manager

### Installation
1. Clone the repository or download the project files.
2. Navigate to the main directory.
3. Install the required Python packages:

```bash
pip install fastapi "uvicorn[standard]" sqlalchemy passlib[bcrypt] python-jose "python-multipart" jinja2 pydantic
```

### Running the Application
1. Navigate to the `auth` directory.
2. Start the application with Uvicorn:

```bash
python main.py
```

The application will run on `http://127.0.0.1:80`.

### Default Admin Account
On first run, a default admin account is created:
* **Username**: `admin`
* **Password**: `password123`

---

## ⚡ API Endpoints

This section provides a comprehensive overview of the available API endpoints.

### Authentication Endpoints
These endpoints are used for user login and logout, managing the authentication cookie.

#### `POST /token`
Authenticates a user and issues an access token. The token is stored in a secure, HTTP-only cookie.

**Request Body (Form Data)**

```
username: string
password: string
```

**Success Response**

```json
{
  "message": "Login successful",
  "is_admin": true
}
```

#### `POST /api/logout`

Logs the current user out by deleting their authentication cookie.

**Success Response**

```json
{
  "message": "Logged out successfully"
}
```

### User Endpoints (Authenticated)

These endpoints are accessible to any logged-in user with a valid authentication cookie.

#### `GET /api/me`

Fetches the details of the currently authenticated user.

**Success Response**

```json
{
  "username": "user123",
  "is_admin": false,
  "profile_picture_url": "https://example.com/profile.jpg"
}
```

### Admin Endpoints (Admin Only)

These endpoints require admin privileges and a valid authentication cookie.

#### `GET /api/admin/users`

Retrieves a list of all users in the system.

**Success Response**

```json
[
  { "id": 1, "username": "admin", "is_admin": true, "profile_picture_url": "..." },
  { "id": 2, "username": "user1", "is_admin": false, "profile_picture_url": "..." }
]
```

#### `POST /api/admin/users`

Creates a new user.

**Request Body**

```json
{
  "username": "newuser",
  "password": "strongpassword",
  "is_admin": false,
  "profile_picture_url": "https://example.com/newuser.jpg"
}
```

**Success Response**

```json
{
  "message": "User created successfully",
  "user_id": 3
}
```

#### `DELETE /api/admin/users/{user_id}`

Deletes a user by their ID. You cannot delete your own admin account.

**Success Response**

```json
{
  "message": "User deleted successfully"
}
```

#### `PUT /api/admin/users/{user_id}`

Updates an existing user. Accepts partial updates (e.g., you can just change the password or profile picture).

**Request Body (Partial)**

```json
{
  "password": "a-new-password",
  "profile_picture_url": "https://new-url.com/picture.jpg"
}
```

**Success Response**

```json
{
  "message": "User updated successfully"
}
```

-----

## 🎨 Frontend

The frontend is served from the `templates/` directory.

* `GET /`: Serves the `index.html` login page.
* `GET /authorized/{filepath:path}`: Serves protected HTML pages from the `templates/authorized/` directory after a successful login.

The `index.html` page uses JavaScript to handle form submissions and dynamically show/hide different panels based on user actions and administrative privileges. It uses `fetch` to interact with the backend API endpoints.

-----

## 📦 Dependencies

* `fastapi`: Web framework for building the API.
* `uvicorn`: ASGI server for running the FastAPI application.
* `sqlalchemy`: ORM for database interactions.
* `passlib`: For password hashing and verification.
* `python-jose`: For handling JWT token creation and decoding.
* `python-multipart`: For parsing form data.
* `jinja2`: For rendering HTML templates.
* `pydantic`: For data validation with FastAPI models.
