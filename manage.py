#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    if sys.argv[1] == "runserver":
        subprocess.Popen(
            [
                "pnpm",
                "tailwindcss",
                "-i",
                "./static/src/input.css",
                "-o",
                "./static/src/output.css",
                "--watch",
            ]
        )
        # Run collectstatic command with 'yes' as an argument
        subprocess.run(["python", "manage.py", "collectstatic", "--noinput"])
        subprocess.run(["echo", "-e", "\033[34mServer has successfully started\033[0m"])

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
