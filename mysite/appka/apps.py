from django.apps import AppConfig


class AppkaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appka'

    def ready(self):
        import appka.signals
