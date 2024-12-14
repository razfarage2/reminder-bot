from lambda_packages.scheduler.scheduler import run_tasks
from lambda_packages import schedule
import time
from lambda_packages.dotenv import load_dotenv



load_dotenv()

run_tasks()

# Make sure to run this 12:00 or 15:30
while True:
    schedule.run_pending()
    time.sleep(12600)
