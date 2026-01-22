#!/usr/bin/env bash
# Exit on error
set -o errexit

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# --- NEW: Ensure static directories exist ---
# This prevents errors if Git didn't upload empty folders
mkdir -p static
mkdir -p staticfiles

# Convert static files
# Added --clear to remove old broken files before creating new ones
python manage.py collectstatic --noinput --clear

# Apply database migrations
python manage.py migrate

# Create Superuser Automatically
# The "|| true" part ensures the build doesn't fail if the user already exists
python manage.py createsuperuser --noinput || true