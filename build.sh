#!/usr/bin/env bash
# Exit on error
set -o errexit

# --- ADDED: Upgrade pip first to avoid installation errors ---
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Convert static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate