from django.apps import AppConfig


class {{cookiecutter.appname.capitalize()}}Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "{{cookiecutter.package_name}}.{{cookiecutter.appname}}"
