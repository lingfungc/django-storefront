# Set up your configurations here.

# * This "apps.py" is for configuring our application

from django.apps import AppConfig


class PlaygroundConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'playground'
