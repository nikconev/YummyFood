from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mysite.users'

    def ready(self):
        import mysite.users.signals

