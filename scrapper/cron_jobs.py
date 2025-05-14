import logging
from django.utils import timezone
from .views.scrap_views import scrap_titles

def scheduled_scrap():
    now = timezone.now()
    # Acción que deseas realizar periódicamente
    scrap_titles('https://www.infobae.com/')
    print(f"Tarea programada ejecutada a las {now}")
