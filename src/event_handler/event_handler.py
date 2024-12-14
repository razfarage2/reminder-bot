from clients.weather_client import Weather_Client
from clients.whatsapp_client import Whatsapp_Client
import datetime


class Event_Handler():
    def __init__(self):

        self.wa_client = Whatsapp_Client()
        self.we_client = Weather_Client()
        self.current_day = datetime.datetime.now().strftime("%A")
        self.message = ""

        self.iac_days = ["Sunday", "Monday", "Wednesday", "Saturday"]

        self.open_uni_days = {
            "Tuesday": "You have Class today - Statistics.",
            "Thursday": "You have Class today - Intro To Psychology.",
            "Saturday": "You have Class today - Programming.",
        }
        self.assignment_days = {
            "Wednesday": "Don't forget you have to turn in your assignment Tomorrow.",
            "Thursday": "You need to turn in your assignment Today.",
            "Saturday": "Reminder: Assignment submission due by Monday.",
        }

    # TODO: check if this is a viable option for the future
    def generic_reminder(self, reminder_function):
        if not callable(reminder_function): # requires the user to input a function
            raise ValueError("The provided argument must be a function")

        reminder_message = reminder_function()
        if reminder_message:
            self.wa_client.custom_message(reminder_message)

    def weather_reminder(self):
        try:
            weather_message = self.we_client.get_weather()
            self.wa_client.custom_message(weather_message)
        except Exception as e:
            self.message = f"Failed to send weather reminder: {str(e)}"

    def assignment_reminder(self):
        self.message = self.assignment_days.get(self.current_day, "")
        if self.message:
            self.wa_client.custom_message(self.message)

    def class_reminder(self):
        self.message = self.open_uni_days.get(self.current_day, "")
        if self.message:
            self.wa_client.custom_message(self.message)


