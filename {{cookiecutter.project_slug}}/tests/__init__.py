import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{cookiecutter.package_name}}.settings")
django.setup()
