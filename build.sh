#!/usr/bin/env bash
# Exit on error
set -o errexit

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Convert static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate

# --- NEW: Create Superuser Automatically ---
# The "|| true" part ensures the build doesn't fail if the user already exists
python manage.py createsuperuser --noinput || true