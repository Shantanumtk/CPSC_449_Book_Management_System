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
- Docker (For containerized deployment)
- Docker Compose (For easy orchestration)

## Project Structure
```
project_root/
│
├── .env             # Environment configuration
├── .gitignore       # Git ignore file
├── Dockerfile       # Docker container configuration
├── docker-compose.yml  # Docker Compose orchestration file
├── requirements.txt # Project dependencies
│
└── app/             # Main application directory
    ├── main.py      # FastAPI application routes and logic
    ├── models.py    # SQLAlchemy database models
    ├── database.py  # Database connection configuration
    ├── schemas.py   # Pydantic validation schemas
    └── run.py       # Server startup script
```

## Installation

### Traditional Installation
#### 1. Clone the Repository
```bash
git clone https://github.com/Shantanumtk/CPSC_449_Book_Management_System.git
cd CPSC_449_Book_Management_System/
```

#### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Database Setup
1. Create a MySQL database
2. Update database connection details in `app/database.py`
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

#### 5. Environment Configuration
Create a `.env` file with your database credentials:
```
MYSQL_USER=mysqluser
MYSQL_ROOT_PASSWORD=mysqlrootuser
MYSQL_PASSWORD=mysqluser123
MYSQL_HOST=mysql-db
MYSQL_PORT=3306
MYSQL_DB=bookdb
```

#### 6. Running the Application
```bash
python app/run.py
```

### Docker Installation

#### Prerequisites
- Docker installed
- Docker Compose installed

#### 1. Clone the Repository
```bash
git clone https://github.com/Shantanumtk/CPSC_449_Book_Management_System.git
cd CPSC_449_Book_Management_System/
```

#### 2. Build and Run with Docker Compose
```bash
docker compose up --build
```

This command will:
- Build the Docker images for the application and MySQL
- Start the containers
- Set up the database
- Launch the FastAPI application

#### Docker Compose Configuration
The `docker-compose.yml` file handles:
- MySQL database service
- FastAPI application service
- Network configuration
- Volume persistence for database data

#### Stopping the Containers
```bash
docker compose down --volumes
```

## Running the Application

### Traditional Method
```bash
python app/run.py
```

### Docker Method
```bash
docker compose up 
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
### `app/main.py`
Contains the FastAPI application routes and main application logic for book operations.

### `app/models.py`
Defines SQLAlchemy database models representing the structure of database tables.

### `app/database.py`
Manages database connection configuration and session management.

### `app/schemas.py`
Defines Pydantic schemas for request and response validation.

### `app/run.py`
Provides the startup script for running the FastAPI application.

### Additional Docker Files
### `Dockerfile`
Defines the Docker image configuration for the Python FastAPI application.

### `docker-compose.yml`
Orchestrates the multi-container Docker application, defining services, networks, and volumes.

### `requirements.txt`
Lists all Python package dependencies for the project.

## Notes for Docker Usage
- Ensure Docker and Docker Compose are installed
- The first run might take some time to download and build images
- Database data is persisted using Docker volumes
- Modify `.env` or `docker-compose.yml` for custom configurations

Project Link: https://drive.google.com/file/d/1JykCm3Wk_eEm8F_OJL9NERu62H8MjE-Q/view?usp=drive_link


