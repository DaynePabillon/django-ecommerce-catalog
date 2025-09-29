# Django E-commerce Catalog

A simple Django web application for managing and displaying products in an e-commerce catalog.

## Features

- Product listing and display
- Admin interface for product management
- Responsive design
- Clean and modern UI

## Setup Instructions

1. Create a virtual environment:
   ```
   python -m venv env
   ```

2. Install dependencies:
   ```
   .\env\Scripts\python.exe -m pip install -r requirements.txt
   ```

3. Run migrations:
   ```
   .\env\Scripts\python.exe manage.py makemigrations
   .\env\Scripts\python.exe manage.py migrate
   ```

4. Create a superuser:
   ```
   .\env\Scripts\python.exe manage.py createsuperuser
   ```

5. Run the development server:
   ```
   .\env\Scripts\python.exe manage.py runserver
   ```

## Project Structure

- `pos_app/` - Main application containing models, views, and templates
- `pos_project/` - Django project settings and configuration
- `static/` - Static files (CSS, JavaScript, images)
- `templates/` - HTML templates
- `requirements.txt` - Python dependencies

## Usage

- Visit the home page to see the welcome message
- Navigate to the products page to view all products
- Access the admin panel at `/admin/` to manage products