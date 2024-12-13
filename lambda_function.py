import json
from src.clients.weather_client import Weather_Client
from src.clients.whatsapp_client import Whatsapp_Client
from dotenv import load_dotenv

load_dotenv()

def lambda_handler(event, context):
    try:
        # Initialize the clients
        wa_client = Whatsapp_Client()
        we_client = Weather_Client()

        # Get the weather data
        weather_data = we_client.get_weather()

        # Create the message to send via WhatsApp
        message = wa_client.custom_message(weather_data)
        print(message)
        # Return a successful response with a JSON body
        return {
            'statusCode': 200,
            'body': json.dumps({'message': message})
        }

    except Exception as e:
        # Return an error response if something goes wrong
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
