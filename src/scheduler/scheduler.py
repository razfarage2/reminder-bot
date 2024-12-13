import schedule
from src.clients.weather_client import get_weather
from src.clients.whatappConnector import custom_message
import datetime

get_message = lambda message: message

iac_days = ["Sunday", "Monday", "Wednesday"]

open_uni_days = {
    "Tuesday": "You have Class today - Statistics.",
    "Thursday": "You have Class today - Intro To Psychology.",
}

assignment_days = {
    "Wednesday": "Dont forget you have to turn in your assignment Tomorrow.",
    "Thursday": "You need to turn in your assignment Today.",
}


def run_tasks():
    current_day = datetime.datetime.now().strftime("%A")

    for day in iac_days:
        if current_day == day:
            schedule.every().day.at("15:30").do(
                lambda day=day: custom_message(f"Weather for {day}: {get_weather()}")
            )

    for day, message in open_uni_days.items():
        if current_day == day:
            schedule.every().day.at("10:30").do(
                lambda message=message: custom_message(
                    f"Class reminder: {get_message(message)}"
                )
            )

    for day, message in assignment_days.items():
        if current_day == day:
            schedule.every().day.at("12:00").do(
                lambda message=message: custom_message(
                    f"Assignment reminder: {get_message(message)}"
                )
            )
