## Running the cookiecutter

1. [Install cookiecutter](https://pypi.org/project/cookiecutter/) on your machine
2. `cookiecutter ./cookie-cutter/`
3. The new project is built in the same directory, using the `project_name` given in the above command
4. Change the class name at `{{project_slug}}/{{package_name}}/{{app_name}}/apps.py` to the correct format
5. Add these settings in the `settings.py` file:
   - `OTP_TOTP_ISSUER` for one time passwords
   - `ALLOWED_HOSTS`
   - `CSRF_TRUSTED_ORIGINS`
   - `CSP_DEFAULT_SRC`
6. Update `privacy-policy.html`, `support.html`, `verification.txt` (email template) and `accessibility-statement.html` to match the new project, or remove if not needed
   - Search for phrases like `<DATE>`, `<SYSTEM_NAME>` and `<SYSTEM_URL>` for places that need to be edited