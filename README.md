# User Management System

## Overview
This is a backend-only user management system built using Python and the Model-View-Controller (MVC) architecture. It provides a command-line interface for managing user accounts, roles, and activity logs. The system uses two SQLite databases: one for user data (with tables for `users`, `roles`, and `genders`) and another for logging user activities (e.g., login/logout, function calls, and execution times). Four user roles are supported, each with different access levels, from Manager (full access) to Default User (limited access).

## Features
- **User Authentication**: Register new users or log in with existing credentials. Validates input to prevent empty fields, incorrect credentials, or inactive accounts.
- **Role-Based Access Control**: Four roles: 1. **Manager**: Full access, including viewing logs, activating/deactivating users, changing user roles (to Admin, Super Admin, or Default User), deleting users, and printing user data. 2. **Super Admin**: Access to user list, limited log access, and some user management features. 3. **Admin**: Access to user list with restricted permissions. 4. **Default User**: Can only view and edit their own profile. Manager, Super Admin, and Admin can view and sort the user list (by name, role, or gender), excluding the logged-in user.
- **User Management**: View, edit, or delete user profiles (except the logged-in user’s profile). Activate or deactivate user accounts (Manager only). Change user roles (e.g., to Admin, Super Admin, or Default User; Manager only). Export user data to a text file and convert it to PDF using the "Print Table Data" button. Sort user list by name, role, or gender.
- **Activity Logging**: Logs user actions (e.g., function name, execution date, duration, and user). Manager has full access to view all logs. Export logs to CSV and generate a graph based on execution times via the "Print Table Data" button.
- **Profile Management**: All users can view and edit their own profile information via the "Your Profile" and "Edit Information" sections.
- **Lightweight Database**: Two SQLite databases for user data and logs, requiring no external configuration.

## Tech Stack
- **Language**: Python 3.x
- **Libraries**: Standard Python libraries (e.g., `sqlite3` for database operations, `csv` for log exports)
- **Database**: SQLite (two databases: `users.db` for user data with tables `users`, `roles`, `genders`; `logs.db` for activity logs)
- **Architecture**: Model-View-Controller (MVC)
- **Environment**: Virtual environment (`.venv`)

## Prerequisites
- Python 3.8 or higher installed on your system.
- No external libraries are required, as the project uses Python's built-in libraries.

## Installation
Follow these steps to set up and run the project locally:
1. **Clone the Repository**: `git clone https://github.com/Awmirhm/UserManagement.git`
2. **Navigate to the Project Directory**: `cd UserManagement`
3. **Activate the Virtual Environment**:
   - On Windows: `.venv\Scripts\activate`
   - On macOS/Linux: `source .venv/bin/activate`
   *Note*: The virtual environment (`.venv`) includes all required libraries.
4. **Run the Application**: `python main.py`
   This will start the user management system in your terminal.

## Usage
1. **Sign Up/Login**: Choose "Register" to create a new account or "Login" to access an existing account. The system checks for valid input, correct credentials, and account status.
2. **User Management**: Manager, Super Admin, and Admin can view the user list (sorted by name, role, or gender using the "Sort By" option). Manager can: Activate or deactivate user accounts using the "Activate" or "Deactivate" buttons. Change user roles (e.g., to Admin, Super Admin, or Default User) using the respective buttons. Delete user profiles using the "Delete User" button. Export user data to a text file and convert it to PDF using the "Print Table Data" button.
3. **Activity Logging**: Manager can view all logs, including function name, execution date, duration, and user, via the Logs section. Export logs to CSV and generate a graph of execution times via the "Print Table Data" button.
4. **Profile Management**: All users can view their profile (e.g., name, email, role) in the "Your Profile" section. Edit profile information (e.g., name, email, age, country) in the "Edit Information" section.

*Example Interaction*:
Welcome to User Management System

Register
Login
Exit
Enter choice: 2
Username: a.ri
Password: 123
Login successful! Role: Manager


User Management Menu:

View User List
Your Profile
Edit Information
Activate/Deactivate User
Change User Role
Delete User
Export User Data to PDF
View Logs
Export Logs to CSV
Exit

## Test Credentials
For testing purposes, you can use the following credentials:
- **Username**: `a.ri`
- **Password**: `123`
- **Role**: Manager (full access)
*Note*: For security, avoid using default credentials in production. Consider hashing passwords (e.g., using `hashlib`) and storing sensitive data in a `.env` file.

## Project Structure
UserManagement/
├── controllers/
# Handles business logic (MVC Controller)
├── models/
# Defines data structures and database interactions (MVC Model)
├── views/
# Manages command-line interface output (MVC View)
├── .venv/
# Virtual environment with required libraries
├── main.py
# Entry point of the application
├── users.db
# SQLite database for user data (tables: users, roles, genders)
├── logs.db
# SQLite database for activity logs
└── README.md
# Project documentation
## Contributing
We welcome contributions to improve this project! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please read our [Contributing Guide](CONTRIBUTING.md) for more details (if available).

## Contact
- **Author**: Amir (Awmirhm)
- **GitHub**: [Awmirhm](https://github.com/Awmirhm)
