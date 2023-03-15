import time
import schedule
from api import defaultResponse

# Programar la función para que se ejecute cada 5 minutos
schedule.every(5).minutes.do(defaultResponse)

# Verificar si la tarea está programada
jobs = schedule.jobs
if jobs:
    for job in jobs:
        print(f"Tarea programada: {job}")
else:
    print("No hay tareas programadas.")

while True:
    # Ejecutar las tareas programadas
    schedule.run_pending()
    # Esperar un segundo antes de volver a verificar si hay tareas programadas
    time.sleep(1)