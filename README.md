# README.md for FastAPI Blog Project


## Overview

This project is a simple blogging platform built using FastAPI, SQLAlchemy, and Pydantic. It allows users to sign up, log in, create posts, retrieve their posts, and delete posts.

## Installation

1. Clone the repository:
   `git clone https://github.com/denishjpatel/test_task.git`


2. Navigate to the project directory:
   `cd test_task`

3. Install the required packages:
    `pip install -r requirements.txt`
    
## Configuration
- Update the database connection details in `database.py`:
    - Update the `SQLALCHEMY_DATABASE_URL`

- Set your secret key for JWT in `services/auth_services.py`:
    - Update the `SECRET_KEY` variable
    
## Running the Application

1. Start the FastAPI server:
   `uvicorn main:app --reload`
   