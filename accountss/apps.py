# accountss/apps.py

from django.apps import AppConfig

class AccountsConfig(AppConfig):
    name = 'accountss'
    
class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accountss'

    def ready(self):
        import accountss.signals  # noqa


