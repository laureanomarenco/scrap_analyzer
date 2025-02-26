import logging
from django.db.models.signals import post_migrate
from django.dispatch import receiver
##from .scheduler import start_scheduler_migration

##@receiver(post_migrate)
##def start_scheduler_migration():
    ##""" Inicia el scheduler cuando la conexión a la base de datos se ha creado. """
    ##print("Iniciando el BackgroundScheduler...")
    ##start_scheduler_migration()