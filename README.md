# Book Management REST API

A Book Management REST API built with Django and Django REST Framework.

This project provides REST API functionality with JWT authentication, CRUD operations, filtering, searching, ordering, pagination, throttling, PostgreSQL database integration, and a simple web UI.

---

## Features

- REST API
- Book management
- Book CRUD operations
- Django REST Framework serialization
- JWT authentication
- JWT access token
- JWT refresh token
- Authentication-based permissions
- Filtering by category and author
- Searching by title and author
- Ordering by title, price, and published date
- Pagination with 5 books per page
- API throttling
- PostgreSQL database
- PostgreSQL database dump and restore
- User registration and login
- Web-based UI

---

## Technologies

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

## Project Structure

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
    ├── database/
    │   └── book_management_db.dump
    │
    ├── static/
    ├── templates/
    │
    ├── manage.py
    ├── requirements.txt
    ├── .env.example
    ├── .gitignore
    └── README.md

---

# Setup and Installation

## 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd book-management-api
```

## 2. Create Virtual Environment

```bash
python3 -m venv venv
```

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# PostgreSQL Setup

Check PostgreSQL:

```bash
psql --version
```

Start PostgreSQL on Linux:

```bash
sudo systemctl start postgresql
```

Check status:

```bash
sudo systemctl status postgresql
```

## Create Database

```bash
sudo -u postgres createdb book_management_db
```

Or:

```bash
sudo -u postgres psql
```

```sql
CREATE DATABASE book_management_db;
```

Exit:

```sql
\q
```

---

# Environment Variables

The project uses `python-dotenv`.

Django settings load environment variables with:

```python
from dotenv import load_dotenv

load_dotenv()
```

Create `.env` in the project root:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=book_management_db
DB_USER=postgres
DB_PASSWORD=your_postgresql_password
DB_HOST=127.0.0.1
DB_PORT=5432
```

Replace `your_postgresql_password` with your PostgreSQL password.

## `.env.example`

Keep `.env.example` in GitHub, but never commit the real `.env`.

Example:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=book_management_db
DB_USER=postgres
DB_PASSWORD=your_postgresql_password
DB_HOST=127.0.0.1
DB_PORT=5432
```

Create your local `.env`:

```bash
cp .env.example .env
```

Then update the values.

---

# PostgreSQL Database Dump

The project can include a PostgreSQL custom-format dump at:

    database/book_management_db.dump

The dump can be used to restore the database structure and existing data.

---

# Restore Database From Dump

## 1. Create the Database

If it does not already exist:

```bash
sudo -u postgres createdb book_management_db
```

## 2. Restore the Dump

Run this from the project root:

```bash
pg_restore -U postgres -h 127.0.0.1 -p 5432 -d book_management_db database/book_management_db.dump
```

Multi-line version:

```bash
pg_restore \
    -U postgres \
    -h 127.0.0.1 \
    -p 5432 \
    -d book_management_db \
    database/book_management_db.dump
```

Make sure `\` is the last character on each line.

If your PostgreSQL user requires a password, PostgreSQL will prompt for it.

---

# Verify Database Restore

Connect:

```bash
psql -U postgres -h 127.0.0.1 -d book_management_db
```

List tables:

```sql
\dt
```

Check books:

```sql
SELECT * FROM books_book;
```

Count books:

```sql
SELECT COUNT(*) FROM books_book;
```

Exit:

```sql
\q
```

---

# Check the Dump File

To verify that the dump contains database objects:

```bash
pg_restore --list database/book_management_db.dump
```

A list of tables and other database objects means the dump is readable.

---

# Test the Dump Safely

You can test the dump using a separate database.

Create a temporary database:

```bash
sudo -u postgres createdb book_management_test
```

Restore:

```bash
pg_restore \
    -U postgres \
    -h 127.0.0.1 \
    -p 5432 \
    -d book_management_test \
    database/book_management_db.dump
```

Connect:

```bash
psql -U postgres -h 127.0.0.1 -d book_management_test
```

Check tables:

```sql
\dt
```

Check book data:

```sql
SELECT COUNT(*) FROM books_book;
```

Exit:

```sql
\q
```

Remove the temporary database:

```bash
sudo -u postgres dropdb book_management_test
```

---

# Django Database Check

After configuring `.env`:

```bash
python manage.py check
```

Check migrations:

```bash
python manage.py showmigrations
```

If you restored the provided dump, migration records and existing data should already be present.

---

# Create Superuser

If needed:

```bash
python manage.py createsuperuser
```

Admin:

    http://127.0.0.1:8000/admin/

---

# Run the Project

```bash
python manage.py runserver
```

Open:

    http://127.0.0.1:8000/

---

# API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/books/` | View all books |
| POST | `/books/` | Create a book |
| GET | `/books/<id>/` | View one book |
| PUT | `/books/<id>/` | Update a book |
| PATCH | `/books/<id>/` | Partially update a book |
| DELETE | `/books/<id>/` | Delete a book |

Anyone can view books.

Authentication is required for:

- Create
- Update
- Delete

---

# JWT Authentication

## Obtain Access and Refresh Tokens

```http
POST /api/token/
```

Example request:

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

Example response:

```json
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}
```

## Refresh Access Token

```http
POST /api/token/refresh/
```

Request:

```json
{
    "refresh": "your_refresh_token"
}
```

## Using JWT Authentication

For authenticated API requests:

```http
Authorization: Bearer <access_token>
```

---

# Create Book

```http
POST /books/
```

Example:

```json
{
    "title": "Python Programming",
    "author": "John Smith",
    "category": "Programming",
    "price": "850.00",
    "published_date": "2025-01-15"
}
```

---

# Filtering

Filter by category:

```http
GET /books/?category=Programming
```

Filter by author:

```http
GET /books/?author=John
```

---

# Searching

Search by title or author:

```http
GET /books/?search=Python
```

---

# Ordering

Order by price:

```http
GET /books/?ordering=price
```

Highest price first:

```http
GET /books/?ordering=-price
```

Supported ordering fields:

- `title`
- `price`
- `published_date`

---

# Pagination

The API returns 5 books per page.

```http
GET /books/?page=2
```

The response provides:

- Total number of books
- Current results
- Next page
- Previous page

Example:

```json
{
    "count": 20,
    "next": "http://127.0.0.1:8000/books/?page=3",
    "previous": "http://127.0.0.1:8000/books/?page=1",
    "results": []
}
```

---

# Throttling

API throttling prevents unlimited requests.

Anonymous users:

    20 requests per minute

Authenticated users:

    60 requests per minute

Configuration:

```python
'DEFAULT_THROTTLE_CLASSES': [
    'rest_framework.throttling.AnonRateThrottle',
    'rest_framework.throttling.UserRateThrottle',
],

'DEFAULT_THROTTLE_RATES': {
    'anon': '20/minute',
    'user': '60/minute',
},
```

---

# Combined API Request

The API supports combining search, ordering, and pagination:

```http
GET /books/?search=Python&ordering=-price&page=2
```

This request:

1. Searches for `Python`
2. Searches in title and author
3. Orders by price
4. Shows highest-priced books first
5. Returns page 2
6. Applies API throttling

---

# Web UI

## Book List

    http://127.0.0.1:8000/book/

The book list page provides:

- Book listing
- Pagination
- Book details navigation
- Add Book button for authenticated users

## Book Details

Example:

    http://127.0.0.1:8000/book/1/

Displays:

- Title
- Author
- Category
- Price
- Published date

## Add Book

    http://127.0.0.1:8000/book/add/

Authenticated users can create a book.

## Edit Book

    http://127.0.0.1:8000/book/1/edit/

Authenticated users can update a book.

## Delete Book

    http://127.0.0.1:8000/book/1/delete/

Authenticated users can delete a book.

---

# User Authentication

## Register

    http://127.0.0.1:8000/register/

## Login

    http://127.0.0.1:8000/login/

## Logout

Use the Logout button in the navigation bar after login.

---

# Testing With Postman

## 1. Get JWT Token

POST:

    http://127.0.0.1:8000/api/token/

Body → raw → JSON:

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

Copy the returned access token.

## 2. Create Book

POST:

    http://127.0.0.1:8000/books/

Authorization:

    Type: Bearer Token
    Token: <your_access_token>

Body:

```json
{
    "title": "Django REST Framework",
    "author": "William Smith",
    "category": "Programming",
    "price": "950.00",
    "published_date": "2025-05-20"
}
```

## 3. Get Books

    GET http://127.0.0.1:8000/books/

## 4. Search

    GET http://127.0.0.1:8000/books/?search=Python

## 5. Filter

    GET http://127.0.0.1:8000/books/?category=Programming

## 6. Ordering

    GET http://127.0.0.1:8000/books/?ordering=-price

## 7. Pagination

    GET http://127.0.0.1:8000/books/?page=2

## 8. Combined Request

    GET http://127.0.0.1:8000/books/?search=Python&ordering=-price&page=2

---

# Database Dump Creation

Create the database directory:

```bash
mkdir -p database
```

Create a PostgreSQL custom-format dump:

```bash
pg_dump \
    -U postgres \
    -h 127.0.0.1 \
    -p 5432 \
    -d book_management_db \
    -F c \
    -f database/book_management_db.dump
```

The dump will be created at:

    database/book_management_db.dump

Check the file:

```bash
ls -lh database/book_management_db.dump
```

Check its contents:

```bash
pg_restore --list database/book_management_db.dump
```

---

# Security

Do not commit sensitive information to GitHub.

`.gitignore` should include:

```gitignore
.env
venv/
__pycache__/
*.pyc
.idea/
.vscode/
staticfiles/
media/
```

Commit:

    .env.example

Do not commit:

    .env

The `.env` file contains sensitive database credentials and the Django secret key.

---

# Complete Setup From GitHub

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>

cd book-management-api

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

cp .env.example .env
```

Configure `.env`.

Create the PostgreSQL database:

```bash
sudo -u postgres createdb book_management_db
```

Restore the dump:

```bash
pg_restore \
    -U postgres \
    -h 127.0.0.1 \
    -p 5432 \
    -d book_management_db \
    database/book_management_db.dump
```

Check Django:

```bash
python manage.py check
```

Run the server:

```bash
python manage.py runserver
```

Open:

    http://127.0.0.1:8000/

---

# Assignment Requirements

This project fulfills the required Assignment 12 features:

- [x] Book Model
- [x] Book Serializer
- [x] REST API
- [x] JWT Authentication
- [x] Access Token
- [x] Refresh Token
- [x] Public Book Listing
- [x] Public Book Details
- [x] Authenticated Book Creation
- [x] Authenticated Book Update
- [x] Authenticated Book Delete
- [x] Filtering by category
- [x] Filtering by author
- [x] Searching by title
- [x] Searching by author
- [x] Ordering by title
- [x] Ordering by price
- [x] Ordering by published date
- [x] Pagination
- [x] 5 books per page
- [x] API throttling
- [x] PostgreSQL
- [x] PostgreSQL database dump
- [x] Database restore process
- [x] Web UI

---

# Author

**Rabaya Shova**

Book Management REST API  
Assignment 12
