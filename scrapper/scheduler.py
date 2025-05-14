from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from .cron_jobs import scheduled_scrap  # Importa tu tarea programada
    
def start_scheduler():
    """Inicia el BackgroundScheduler"""
    print("Iniciando el BackgroundScheduler...")
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    # Agregar la tarea programada
    scheduler.add_job(
        scheduled_scrap,
        trigger="cron",
        hour="10,14,19,21",  # Ejecutar a las 10:00 AM, 2:00 PM, 7:00 PM 20:10
        minute="25",
        id="my_scheduled_task_id",
        replace_existing=True,
    )

    scheduler.start()
    print("Scheduler iniciado correctamente.")