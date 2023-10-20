from django.apps import AppConfig

def ready(self):
    from . import signals
class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'
    
