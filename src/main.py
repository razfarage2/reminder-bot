from src.scheduler.scheduler import run_tasks
import schedule
import time
from dotenv import load_dotenv


load_dotenv()

run_tasks()

# Make sure to run this 12:00 or 15:30
while True:
    schedule.run_pending()
    time.sleep(12600)
