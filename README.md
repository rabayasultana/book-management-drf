# Book Management REST API

A Book Management REST API built with Django and Django REST Framework.

This project provides book CRUD operations, JWT authentication, filtering, searching, ordering, pagination, API throttling, PostgreSQL database integration, and a simple web-based UI.

---

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [PostgreSQL Database Setup](#postgresql-database-setup)
- [Database Migrations](#database-migrations)
- [Create Superuser](#create-superuser)
- [Run the Project](#run-the-project)
- [JWT Authentication](#jwt-authentication)
- [Book API Endpoints](#book-api-endpoints)
- [Filtering](#filtering)
- [Searching](#searching)
- [Ordering](#ordering)
- [Pagination](#pagination)
- [Throttling](#throttling)
- [Combined API Request](#combined-api-request)
- [Web UI](#web-ui)
- [PostgreSQL Database Dump](#postgresql-database-dump)
- [Restore Database Dump](#restore-database-dump)
- [Test Database Dump](#test-database-dump)
- [Security](#security)
- [Assignment Requirements](#assignment-requirements)

---

# Features

The project supports:

- REST API
- Book model
- Book serialization
- JWT authentication
- JWT access token
- JWT refresh token
- Book CRUD operations
- Authentication-based permissions
- Filtering
- Searching
- Ordering
- Pagination
- API throttling
- PostgreSQL database
- PostgreSQL database dump and restore
- User registration
- User login
- Web-based book management UI

---

# Technologies

The project is built using:

- Python
- Django
- Django REST Framework
- Django REST Framework Simple JWT
- Django Filter
- PostgreSQL
- psycopg2
- python-dotenv
- Bootstrap
- HTML
- CSS
- JavaScript

---

# Project Structure

```text
book-management-api/
│
├── accounts/
│   ├── migrations/
│   ├── templates/
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── books/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── static/
│
├── templates/
│
├── database/
│   └── book_management_db.dump
│
├── manage.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
└── README.md