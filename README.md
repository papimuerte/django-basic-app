# Django Basic Application

A simple Django web application with a basic home page.

## Setup Instructions

1. **Create a virtual environment** (if not already created):
   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Open your browser** and go to:
   ```
   http://127.0.0.1:8000/
   ```

## Project Structure

- `myproject/` - Main Django project settings
- `main/` - Django app with views and URLs
- `manage.py` - Django management script
- `requirements.txt` - Python dependencies

## Features

- Basic home page with welcome message
- Django admin interface available at `/admin/`
- SQLite database for development

## Next Steps

To extend this application, you can:
- Add more views in `main/views.py`
- Create models in `main/models.py`
- Add templates in `main/templates/`
- Create forms in `main/forms.py` 