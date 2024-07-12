# Notes Project

This is a simple Django application for managing personal notes. The application allows users to sign up, log in, and create, read, update, and delete their notes. Each note includes a title and a body, and the notes are paginated with 10 notes per page.

## Features

- User Authentication (sign up, log in, log out)
- CRUD operations for notes (create, read, update, delete)
- Notes pagination (10 notes per page)
- Docker support for easy setup

## Project Structure

The project follows Django's best practices, including the use of class-based views, models, templates, and static files. Success and error messages are displayed using Django's messages framework.

## Setup

### Prerequisites

- Python 3.7 or later
- pip (Python package installer)
- virtualenv (for creating a virtual environment)

### Local Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/notes_project.git
   cd notes_project
   
2.Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate 

3.Install the dependencies:
pip install -r requirements.txt

4.Apply migrations:
python manage.py migrate

5.Run the server:
python manage.py runserver

6.Access the application:
Open your browser and go to http://127.0.0.1:8000.
