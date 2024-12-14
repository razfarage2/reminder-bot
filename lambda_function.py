import json
import datetime
import logging
from src.clients.weather_client import Weather_Client
from src.clients.whatsapp_client import Whatsapp_Client
from dotenv import load_dotenv
from src.message_type import Message_Type

load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)


def lambda_handler(event, context):
    try:
        wa_client = Whatsapp_Client()
        we_client = Weather_Client()

        iac_days = ["Sunday", "Monday", "Wednesday", "Saturday"]

        open_uni_days = {
            "Tuesday": "You have Class today - Statistics.",
            "Thursday": "You have Class today - Intro To Psychology.",
            "Saturday": "You have Class today - Programming.",
        }
        assignment_days = {
            "Wednesday": "Don't forget you have to turn in your assignment Tomorrow.",
            "Thursday": "You need to turn in your assignment Today.",
            "Saturday": "Reminder: Assignment submission due by Monday.",
        }

        event_type = event.get("type", "unknown").lower()

        current_day = datetime.datetime.now().strftime("%A")

        message = ""

        # Process event types
        if event_type == Message_Type.WEATHER.value:
            logging.info("Processing weather event")
            weather_message = we_client.get_weather()
            wa_client.custom_message(weather_message)

        elif event_type == Message_Type.ASSIGNMENT.value:
            logging.info("Processing assignment event")
            message = assignment_days.get(current_day, "")
            if message:
                wa_client.custom_message(message)

        elif event_type == Message_Type.LESSON.value:
            logging.info("Processing lesson event")
            message = open_uni_days.get(current_day, "")
            if message:
                wa_client.custom_message(message)

        return {
            'statusCode': 200,
            'body': json.dumps({'message': message})
        }

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
