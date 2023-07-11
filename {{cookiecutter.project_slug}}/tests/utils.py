import functools

import httpx
import testino

import {{cookiecutter.package_name}}.wsgi

TEST_SERVER_URL = "http://{{cookiecutter.project_slug}}-testserver:{{cookiecutter.port}}/"


def with_client(func):
    @functools.wraps(func)
    def _inner(*args, **kwargs):
        with httpx.Client(app={{cookiecutter.package_name}}.wsgi.application, base_url=TEST_SERVER_URL) as client:
            return func(client, *args, **kwargs)

    return _inner


def make_testino_client():
    client = testino.WSGIAgent({{cookiecutter.package_name}}.wsgi.application, TEST_SERVER_URL)
    return client
