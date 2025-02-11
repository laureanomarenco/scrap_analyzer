import logging
from django.utils import timezone
from .views.scrap_views import scrap_and_count

def scheduled_scrap():
    now = timezone.now()
    # Acción que deseas realizar periódicamente
    scrap_and_count('https://www.infobae.com/')
    print(f"Tarea programada ejecutada a las {now}")
