import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pos_project.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

try:
    User.objects.create_superuser('Admin123', 'admin@example.com', 'Admin1234')
    print("Superuser created successfully for E-commerce Catalog")
except Exception as e:
    print(f"Error creating superuser: {e}")
