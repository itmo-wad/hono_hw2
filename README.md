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

### 1. **Login - Connexion**
   The login functionality allows users to authenticate themselves by entering their username and password. The credentials are validated against the stored data in the MongoDB database, ensuring a secure login process. 
   
![login](https://github.com/user-attachments/assets/7fc29d7b-7150-4c17-968f-a1c352702936)

![login1](https://github.com/user-attachments/assets/54bb31ec-976b-46b3-bf82-9a51141ab2d4)



### 2. **Sign Up - Inscription**
   Users can create a new account by providing their username, email, age, and a secure password. The system validates the entered data before storing it in the MongoDB database.
   
   ![sign up](https://github.com/user-attachments/assets/a1365062-daec-43ba-9d76-066b33c6d398)


### 3. **Profile - Profil Utilisateur**
   Each user has a personal profile where they can view and update their information, such as their username, email, and age. Access to the profile is protected and only available after successful authentication.
   
   ![profile](https://github.com/user-attachments/assets/91c4e125-6114-4daf-8ffc-b58fdaffa172)
   
   ![profile1](https://github.com/user-attachments/assets/49dcad9a-1a3d-438d-855b-19609f6d8134)
   
   ![profile2](https://github.com/user-attachments/assets/a45d296b-0010-4c5b-a0d5-3252c69952c6)


### 4. **Update Profile - Mise à jour des informations**
   Users can edit their profile information (name, email, age). The updated details are saved in the database and reflected in real-time on the user’s profile.
   ![motpasse](https://github.com/user-attachments/assets/cc06a80e-b898-47ce-910e-cbca73dffd75)
   
   ![passe](https://github.com/user-attachments/assets/75d32ee6-7cdd-4f13-a61b-0cb9f6fcd953)


### 5. **Password Hashing with Mongo - Hachage du mot de passe**
   To ensure the security of user passwords, the application hashes passwords before storing them in MongoDB. This process uses a secure hashing algorithm like `bcrypt` to prevent retrieving the passwords in plaintext, ensuring protection against unauthorized access.

![mongodb](https://github.com/user-attachments/assets/827158b8-64f8-4042-bb7c-d49df81b6a25)




