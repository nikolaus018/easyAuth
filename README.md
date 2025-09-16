<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>easyAuth: A Simple FastAPI User Authentication System</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Poppins:wght@500;600&display=swap');
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f3f4f6;
            color: #1f2937;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem;
        }
        .header {
            text-align: center;
            margin-bottom: 2.5rem;
        }
        .header h1 {
            font-family: 'Poppins', sans-serif;
            font-size: 2.5rem;
            font-weight: 700;
            color: #111827;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }
        .header p {
            font-size: 1.125rem;
            color: #4b5563;
        }
        .section-title {
            font-family: 'Poppins', sans-serif;
            font-size: 2rem;
            font-weight: 600;
            color: #1f2937;
            border-bottom: 2px solid #3b82f6;
            padding-bottom: 0.5rem;
            margin-bottom: 1.5rem;
        }
        .feature-list {
            list-style: none;
            padding: 0;
            display: grid;
            gap: 1.5rem;
        }
        .feature-item {
            background-color: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 0.75rem;
            padding: 1.5rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            transition: transform 0.2s;
        }
        .feature-item:hover {
            transform: translateY(-5px);
        }
        .feature-item h3 {
            font-weight: 600;
            font-size: 1.25rem;
            margin-bottom: 0.5rem;
        }
        .code-block {
            background-color: #111827;
            color: #f9fafb;
            padding: 1rem;
            border-radius: 0.5rem;
            overflow-x: auto;
            font-family: monospace;
            white-space: pre;
        }
        .api-endpoint {
            background-color: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 0.75rem;
            padding: 1.5rem;
            margin-bottom: 1rem;
        }
        .method-badge {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 9999px;
            font-weight: 700;
            font-size: 0.75rem;
            margin-right: 0.5rem;
        }
        .method-get { background-color: #dbeafe; color: #1e40af; }
        .method-post { background-color: #d1fae5; color: #065f46; }
        .method-put { background-color: #fef3c7; color: #92400e; }
        .method-delete { background-color: #fee2e2; color: #991b1b; }
        .footer {
            text-align: center;
            margin-top: 2rem;
            padding-top: 1rem;
            border-top: 1px solid #e5e7eb;
            color: #6b7280;
        }
    </style>
</head>
<body class="bg-gray-100">

    <div class="container">
        <header class="header">
            <h1 class="text-4xl font-extrabold">🚀 easyAuth: A Simple FastAPI User Authentication System</h1>
            <p class="mt-2 text-lg text-gray-600">
                A simple, robust user authentication system with a full-stack implementation using FastAPI and a dynamic admin panel.
            </p>
        </header>

        <hr class="my-8">

        <section id="features">
            <h2 class="section-title">✨ Features</h2>
            <ul class="feature-list">
                <li class="feature-item">
                    <h3>User Authentication</h3>
                    <p>Secure login and logout functionality using JWTs stored in HTTP-only cookies.</p>
                </li>
                <li class="feature-item">
                    <h3>Password Hashing</h3>
                    <p>Passwords are **securely hashed** using `bcrypt` via the `passlib` library.</p>
                </li>
                <li class="feature-item">
                    <h3>Role-Based Access Control</h3>
                    <p>Authenticated users have basic access, while admin users have exclusive access to a full user management system.</p>
                </li>
                <li class="feature-item">
                    <h3>Admin Panel</h3>
                    <p>A dynamic, single-page admin interface for viewing, creating, updating, and deleting users directly from the browser.</p>
                </li>
                <li class="feature-item">
                    <h3>SQLite Database</h3>
                    <p>Uses `SQLAlchemy` with a local SQLite database for simplicity, perfect for development and small-scale applications.</p>
                </li>
                <li class="feature-item">
                    <h3>Automated Setup</h3>
                    <p>The application automatically creates the database and a default admin user on startup.</p>
                </li>
            </ul>
        </section>

        <hr class="my-8">

        <section id="getting-started">
            <h2 class="section-title">⚙️ Getting Started</h2>
            <h3 class="text-xl font-bold mt-4">Prerequisites</h3>
            <ul class="list-disc list-inside ml-4">
                <li>Python 3.7+</li>
                <li>`pip` package manager</li>
            </ul>

            <h3 class="text-xl font-bold mt-4">Installation</h3>
            <ol class="list-decimal list-inside ml-4">
                <li>Clone the repository or download the project files.</li>
                <li>Navigate to the `auth` directory.</li>
                <li>Install the required Python packages:
                    <div class="code-block mt-2">
                        <pre>pip install fastapi "uvicorn[standard]" sqlalchemy passlib[bcrypt] python-jose "python-multipart" jinja2 pydantic</pre>
                    </div>
                </li>
            </ol>

            <h3 class="text-xl font-bold mt-4">Running the Application</h3>
            <ol class="list-decimal list-inside ml-4">
                <li>Navigate to the `auth` directory.</li>
                <li>Start the application with Uvicorn:
                    <div class="code-block mt-2">
                        <pre>python main.py</pre>
                    </div>
                </li>
            </ol>
            <p class="mt-2">The application will run on `http://127.0.0.1:80`.</p>

            <h3 class="text-xl font-bold mt-4">Default Admin Account</h3>
            <p>On first run, a default admin account is created:</p>
            <ul class="list-disc list-inside ml-4">
                <li><strong>Username</strong>: `admin`</li>
                <li><strong>Password</strong>: `password123`</li>
            </ul>
        </section>

        <hr class="my-8">

        <section id="api-endpoints">
            <h2 class="section-title">⚡ API Endpoints</h2>
            <p class="text-gray-600 mb-6">This section provides a comprehensive overview of the available API endpoints.</p>

            <h3 class="text-2xl font-bold mb-4">Authentication Endpoints</h3>
            <p class="text-gray-600 mb-4">These endpoints are used for user login and logout, managing the authentication cookie.</p>

            <div class="api-endpoint">
                <div class="flex items-center">
                    <span class="method-badge method-post">POST</span>
                    <h4 class="font-semibold text-lg">/token</h4>
                </div>
                <p class="text-gray-600 mt-2">Authenticates a user and issues an access token. The token is stored in a secure, HTTP-only cookie.</p>
                <h5 class="font-semibold mt-4">Request Body (Form Data)</h5>
                <div class="code-block mt-2"><pre>username: string<br>password: string</pre></div>
                <h5 class="font-semibold mt-4">Success Response</h5>
                <div class="code-block mt-2"><pre>// Status: 200 OK<br>{<br>  "message": "Login successful",<br>  "is_admin": true<br>}</pre></div>
            </div>

            <div class="api-endpoint">
                <div class="flex items-center">
                    <span class="method-badge method-post">POST</span>
                    <h4 class="font-semibold text-lg">/api/logout</h4>
                </div>
                <p class="text-gray-600 mt-2">Logs the current user out by deleting their authentication cookie.</p>
                <h5 class="font-semibold mt-4">Success Response</h5>
                <div class="code-block mt-2"><pre>// Status: 200 OK<br>{<br>  "message": "Logged out successfully"<br>}</pre></div>
            </div>

            <h3 class="text-2xl font-bold mt-6 mb-4">User Endpoints (Authenticated)</h3>
            <p class="text-gray-600 mb-4">These endpoints are accessible to any logged-in user with a valid authentication cookie.</p>

            <div class="api-endpoint">
                <div class="flex items-center">
                    <span class="method-badge method-get">GET</span>
                    <h4 class="font-semibold text-lg">/api/me</h4>
                </div>
                <p class="text-gray-600 mt-2">Fetches the details of the currently authenticated user.</p>
                <h5 class="font-semibold mt-4">Success Response</h5>
                <div class="code-block mt-2"><pre>// Status: 200 OK<br>{<br>  "username": "user123",<br>  "is_admin": false,<br>  "profile_picture_url": "https://example.com/profile.jpg"<br>}</pre></div>
            </div>

            <h3 class="text-2xl font-bold mt-6 mb-4">Admin Endpoints (Admin Only)</h3>
            <p class="text-gray-600 mb-4">These endpoints require admin privileges and a valid authentication cookie.</p>

            <div class="api-endpoint">
                <div class="flex items-center">
                    <span class="method-badge method-get">GET</span>
                    <h4 class="font-semibold text-lg">/api/admin/users</h4>
                </div>
                <p class="text-gray-600 mt-2">Retrieves a list of all users in the system.</p>
                <h5 class="font-semibold mt-4">Success Response</h5>
                <div class="code-block mt-2"><pre>// Status: 200 OK<br>[<br>  { "id": 1, "username": "admin", "is_admin": true, "profile_picture_url": "..." },<br>  { "id": 2, "username": "user1", "is_admin": false, "profile_picture_url": "..." }<br>]</pre></div>
            </div>

            <div class="api-endpoint">
                <div class="flex items-center">
                    <span class="method-badge method-post">POST</span>
                    <h4 class="font-semibold text-lg">/api/admin/users</h4>
                </div>
                <p class="text-gray-600 mt-2">Creates a new user.</p>
                <h5 class="font-semibold mt-4">Request Body</h5>
                <div class="code-block mt-2"><pre>{<br>  "username": "newuser",<br>  "password": "strongpassword",<br>  "is_admin": false,<br>  "profile_picture_url": "https://example.com/newuser.jpg"<br>}</pre></div>
                <h5 class="font-semibold mt-4">Success Response</h5>
                <div class="code-block mt-2"><pre>// Status: 200 OK<br>{ "message": "User created successfully", "user_id": 3 }</pre></div>
            </div>

            <div class="api-endpoint">
                <div class="flex items-center">
                    <span class="method-badge method-delete">DELETE</span>
                    <h4 class="font-semibold text-lg">/api/admin/users/{user_id}</h4>
                </div>
                <p class="text-gray-600 mt-2">Deletes a user by their ID. You cannot delete your own admin account.</p>
                <h5 class="font-semibold mt-4">Success Response</h5>
                <div class="code-block mt-2"><pre>// Status: 200 OK<br>{ "message": "User deleted successfully" }</pre></div>
            </div>

            <div class="api-endpoint">
                <div class="flex items-center">
                    <span class="method-badge method-put">PUT</span>
                    <h4 class="font-semibold text-lg">/api/admin/users/{user_id}</h4>
                </div>
                <p class="text-gray-600 mt-2">Updates an existing user. Accepts partial updates (e.g., you can just change the password or profile picture).</p>
                <h5 class="font-semibold mt-4">Request Body (Partial)</h5>
                <div class="code-block mt-2"><pre>{<br>  "password": "a-new-password",<br>  "profile_picture_url": "https://new-url.com/picture.jpg"<br>}</pre></div>
                <h5 class="font-semibold mt-4">Success Response</h5>
                <div class="code-block mt-2"><pre>// Status: 200 OK<br>{ "message": "User updated successfully" }</pre></div>
            </div>
        </section>

        <hr class="my-8">

        <section id="frontend">
            <h2 class="section-title">🎨 Frontend</h2>
            <p class="mt-4">
                The frontend is served from the `templates/` directory.
            </p>
            <ul class="list-disc list-inside ml-4 mt-2">
                <li>`GET /`: Serves the `index.html` login page.</li>
                <li>`GET /authorized/{filepath:path}`: Serves protected HTML pages from the `templates/authorized/` directory after a successful login.</li>
            </ul>
            <p class="mt-4 text-gray-600">
                The `index.html` page uses JavaScript to handle form submissions and dynamically show/hide different panels based on user actions and administrative privileges. It uses `fetch` to interact with the backend API endpoints.
            </p>
        </section>

        <hr class="my-8">

        <section id="dependencies">
            <h2 class="section-title">📦 Dependencies</h2>
            <ul class="list-disc list-inside ml-4 mt-4">
                <li>`fastapi`: Web framework for building the API.</li>
                <li>`uvicorn`: ASGI server for running the FastAPI application.</li>
                <li>`sqlalchemy`: ORM for database interactions.</li>
                <li>`passlib`: For password hashing and verification.</li>
                <li>`python-jose`: For handling JWT token creation and decoding.</li>
                <li>`python-multipart`: For parsing form data.</li>
                <li>`jinja2`: For rendering HTML templates.</li>
                <li>`pydantic`: For data validation with FastAPI models.</li>
            </ul>
        </section>

        <footer class="footer">
            <p>&copy; 2025 easyAuth Project. All rights reserved.</p>
        </footer>
    </div>
</body>
</html>
