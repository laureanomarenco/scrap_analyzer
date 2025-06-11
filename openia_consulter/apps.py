from django.apps import AppConfig
from .views.testDeep import testDeep

class OpeniaConsulterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'openia_consulter'
   # testDeep()

