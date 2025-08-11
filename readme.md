# Quiz App - Flask + PostgreSQL + HTML/CSS

A simple quiz application built with Flask backend, PostgreSQL database, and server-rendered HTML/CSS frontend 

---

## Features

- View quizzes, questions, and submit answers via elegant HTML pages
- Stores quizzes, questions, choices, and results in PostgreSQL
- Organized Flask app with blueprints and database migrations
- Easy setup with `.env` config for sensitive info
- Simple and clean UI using templates and CSS

---
## Prerequisites

- Python 3.8+  
- PostgreSQL installed and running  
- `pip` package manager  
- Git (optional, for cloning repo)

---

## Installation & Setup

### 1. Clone the repository

git clone https://github.com/Lokeshkrishna07/Quiz_App_Flask_PostgreSQL.git

cd quiz_app/backend

### 2. Create PostgreSQL database and user

Login to PostgreSQL shell:

psql -U postgres

Create database and user:

CREATE DATABASE quiz_db;
CREATE USER quiz_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE quiz_db TO quiz_user;
\q

*Replace 'your_password' with a secure password.*

### 3. Setup Python environment

Create and activate virtual environment:

python3 -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows PowerShell

### 4. Install dependencies

pip install -r requirements.txt

### 5. Configure environment variables

Create a `.env` file in the `backend/` folder with:

FLASK_ENV=development
SECRET_KEY=your_secret_key_here
DATABASE_URL=postgresql://quiz_user:your_password@localhost:5432/quiz_db

*Replace your_password and your_secret_key_here accordingly.*

### 6. Run database migrations

Initialize migration folder (only once):

flask db init

Generate migration scripts:

flask db migrate -m "Initial migration"

Apply migrations to database:

flask db upgrade

### 7. Run the Flask app

Make sure you are inside the `backend/` directory, then run:

python3 run.py

Open your browser at: http://127.0.0.1:5000/


