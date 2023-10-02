from django.apps import AppConfig


class {{cookiecutter.__app_ref.capitalize()}}Config(AppConfig): # TODO: It's likely you'll have to fix this class name
    default_auto_field = "django.db.models.BigAutoField"
    name = "{{cookiecutter.package_name}}.{{cookiecutter.__app_name_formatted}}"
