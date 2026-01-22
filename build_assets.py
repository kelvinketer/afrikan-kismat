import os
import shutil
import sys
import django
from django.conf import settings

# 1. Setup Django standalone
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# 2. Define Paths
BASE_DIR = settings.BASE_DIR
CORE_STATIC_DIR = os.path.join(BASE_DIR, 'core', 'static')
TARGET_ADMIN_DIR = os.path.join(CORE_STATIC_DIR, 'admin')

# 3. Find the real Django Admin Static path
django_root = os.path.dirname(django.__file__)
admin_static_source = os.path.join(django_root, 'contrib', 'admin', 'static', 'admin')

print(f"--- ASSET BUILDER: Checking source: {admin_static_source}")

# 4. Copy the files manually
if os.path.exists(admin_static_source):
    print(f"--- ASSET BUILDER: Found Admin files! Copying to {TARGET_ADMIN_DIR}...")
    # Remove old copy if it exists to be safe
    if os.path.exists(TARGET_ADMIN_DIR):
        shutil.rmtree(TARGET_ADMIN_DIR)
    
    # Copy the entire admin/static/admin folder to core/static/admin
    shutil.copytree(admin_static_source, TARGET_ADMIN_DIR)
    print("--- ASSET BUILDER: Copy Success!")
else:
    print("--- ASSET BUILDER: ERROR - Could not find Django Admin source files.")

# 5. Run Collectstatic (Now that files are definitely in core/static)
print("--- ASSET BUILDER: Running collectstatic...")
from django.core.management import call_command
call_command('collectstatic', interactive=False, clear=True)