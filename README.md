# Book Management REST API

## Overview
This is a Python-based REST API for managing a book collection, built using FastAPI and MySQL. The API provides endpoints for creating, reading, updating, and deleting books.

## Features
- Create new books
- Retrieve all books
- Retrieve a specific book by ID
- Update existing book details
- Delete a book

## Prerequisites
- Python 3.8+
- MySQL Database
- pip (Python package manager)

## Project Structure
```
project_root/
│
├── main.py          # Main FastAPI application routes and logic
├── models.py        # SQLAlchemy database models
├── database.py      # Database connection configuration
├── schemas.py       # Pydantic validation schemas
├── run.py           # Server startup script
├── requirements.txt # Project dependencies
└── __pycache__/     # Python compiled bytecode (ignored by version control)
```

## Installation

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd <project-directory>
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
1. Create a MySQL database
2. Update database connection details in `database.py`
```sql
CREATE DATABASE book_api;
USE book_api;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    description TEXT
);
```

### 5. Environment Configuration
Create a `.env` file with your database credentials:
```
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=book_api
```

## Running the Application
```bash
python run.py
```

### run.py Details
The application uses `run.py` to start the server:
```python
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",  # Bind to all available network interfaces
        port=5000,       # Set the port to 5000
        reload=True      # Enable live-reload for development
    )
```

## API Endpoints

### Create a Book
- **URL**: `POST http://0.0.0.0:5000/books/`
- **Request Body**:
```json
{
  "title": "To Kill a Mockingbird",
  "author": "Harper Lee",
  "description": "A classic novel."
}
```

### Get All Books
- **URL**: `GET http://0.0.0.0:5000/books/`
- **Response**: List of all books

### Get Book by ID
- **URL**: `GET http://0.0.0.0:5000/books/{book_id}`
- **Example**: `http://0.0.0.0:5000/books/1`

### Update a Book
- **URL**: `PUT http://0.0.0.0:5000/books/{book_id}`
- **Request Body**:
```json
{
  "title": "Updated Title",
  "author": "Updated Author",
  "description": "Updated description"
}
```

### Delete a Book
- **URL**: `DELETE http://0.0.0.0:5000/books/{book_id}`
- **Example**: `http://0.0.0.0:5000/books/1`

## Error Handling
- 404 Not Found: When a book with the specified ID doesn't exist
- 400 Bad Request: For invalid input data

## File Descriptions

### `main.py`
Contains the FastAPI application routes and main application logic for book operations.

### `models.py`
Defines SQLAlchemy database models representing the structure of database tables.

### `database.py`
Manages database connection configuration and session management.

### `schemas.py`
Defines Pydantic schemas for request and response validation.

### `run.py`
Provides the startup script for running the FastAPI application.

### `requirements.txt`
Lists all Python package dependencies for the project.


## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Project Link: https://drive.google.com/file/d/1JykCm3Wk_eEm8F_OJL9NERu62H8MjE-Q/view?usp=drive_link

