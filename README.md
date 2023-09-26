## Running the cookiecutter

1. [Install cookiecutter](https://pypi.org/project/cookiecutter/) on your machine
2. `cookiecutter ./cookie-cutter/`
3. The new project is built in the same directory, using the `project_name` given in the above command
4. Change the class name at `{{project_slug}}/{{package_name}}/{{app_name}}/apps.py` to the correct format
5. Add the `OTP_TOTP_ISSUER` for one time passwords in the `settings.py` file