# My Application - Sign Up & Profile Management

## Description

This project is a simple web application built with **Flask**. It allows users to sign up, log in, and manage their profiles. Users can also update their profile information and change their password. 

## Features

- **Sign Up**: Users can create a new account by providing their username, email, age, and password.
- **Login**: Users can log in to the application using their credentials.
- **Profile Management**: Once logged in, users can view and update their profile information.
- **Flash Messages**: The application provides feedback messages (success or error) for actions like sign-up or login.

## Tech Stack

- **Backend**: Python with Flask
- **Frontend**: HTML, CSS, Bootstrap 4

## Installation

To run this project locally, follow these steps:

### Prerequisites

- Python 3.x
- pip (Python package installer)

## Setting Up the Virtual Environment (venv)

A virtual environment (`venv`) is an isolated environment where all the dependencies for your project are contained. This ensures that your project uses its own versions of libraries and doesn't depend on globally installed libraries.

### Step 1: Create a Virtual Environment

1. First, make sure you're using an up-to-date version of Python (at least Python 3.6). You can check your version with the following command:

   python --version

2. Create a new virtual environment:
   python3 -m venv venv

3. Activate the virtual environment:
   Windows: venv\Scripts\activate
   macOS/Linux: source venv/bin/activate

### Step 2: Install Dependencies

1. Navigate to the project directory:
   cd my-application

2. Install the required dependencies from the `requirements.txt` file:
   pip install -r requirements.txt

## Running the Application

1. Run the Flask application:
   python app.py

Now you can access the application at http://localhost:5000.



### Folder structure
my-application/
├── app.py               # Main Flask application file
├── static/
│   ├── style.css        # Custom styles
│   ├── images/
│   ├── uploads/          # Image assets (e.g., avatar images)
├── templates/
│   ├── registration.html       # registration template
│   ├── login.html       # Login page template
│   ├── profile.html     # Profile page template
│   ├── update_prof.html      # update template
├── requirements.txt     # List of Python dependencies
└── README.md            # Project documentation

