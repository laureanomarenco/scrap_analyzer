import logging
from django.utils import timezone
from .views.scrap_views import scrap_titles, count_words

def scheduled_scrap():
    now = timezone.now()
    # Acción que deseas realizar periódicamente
    #scrap_titles('https://www.infobae.com/')
    webs = ["https://www.infobae.com/","https://www.lanacion.com.ar", "https://www.lacapital.com.ar", "https://www.pagina12.com.ar"]
    for i, web in enumerate(webs, 1):
        count_words(web)
    print(f"Tarea programada ejecutada a las {now}")
