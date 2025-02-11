from django.urls import path
from .views.prompter_views import prompt_openia

urlpatterns = [
    path('prompt/', prompt_openia, name='prompt_openia'),
]