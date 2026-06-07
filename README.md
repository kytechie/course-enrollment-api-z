# Course Enrollment Platform API

## Overview

A FastAPI-based REST API for course enrollment management.

Features:

* User Registration
* User Login
* JWT Authentication
* Course Management
* Student Enrollment
* PostgreSQL Database Integration

---

## Setup

### Create Virtual Environment

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Run Application

uvicorn app.main:app --reload

---

## Database

PostgreSQL

Tables:

* users
* courses
* enrollments

---

## API Endpoints

### Authentication

POST /auth/register

POST /auth/login

### Courses

GET /courses

GET /courses/{id}

POST /courses

### Enrollments

POST /enrollments

DELETE /enrollments/{course_id}

---

## Swagger Documentation

http://127.0.0.1:8000/docs

---

## Author

Peculiar Ugbo
