#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# --- FIX 1: Create the missing folders explicitly ---
# This fixes the "directory does not exist" warning
mkdir -p core/static
mkdir -p staticfiles

# --- FIX 2: Collect static files ---
python manage.py collectstatic --noinput --clear

# Apply database migrations
python manage.py migrate

# --- FIX 3: Typo corrected (removed the accidental '#') ---
python manage.py createsuperuser --noinput || true