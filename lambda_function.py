import json
from src.event_handler.event_handler import Event_Handler
from dotenv import load_dotenv
from src.message_type import Message_Type

load_dotenv()


def lambda_handler(event, context):
    try:
      
        event_type = event.get("type", "unknown").lower()

        match event_type:
            case Message_Type.WEATHER.value:
                event_handler.weather_reminder()
            case Message_Type.ASSIGNMENT.value:
                event_handler.assignment_reminder()
            case Message_Type.LESSON.value:
                event_handler.class_reminder()
            case _:
                return {
                    'statusCode': 400,
                    'body': json.dumps({'error': 'Unknown event type'})
                }

        return {
            'statusCode': 200,
            'body': json.dumps({'message': event_handler.message})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
