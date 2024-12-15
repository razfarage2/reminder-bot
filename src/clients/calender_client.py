import datetime as dt
import os.path
import random

from whatsapp_client import Whatsapp_Client
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class Calender_Client():
    def __init__(self):
        self.SCOPES = ["https://www.googleapis.com/auth/calendar"]
        self.creds = None

    def connect_to_api(self):
        print("Starting to connect.....")

        if os.path.exists("token.json"):
            self.creds = Credentials.from_authorized_user_file("token.json", self.SCOPES)

        if not self.creds or not self.creds.valid:
            print("Creds not found or not valid")
            if self.creds and self.creds.expired and self.creds.refresh_token:
                print("Creds expired... Trying to refresh")
                self.creds.refresh(Request())
            else:
                print("OK, this is the path...")
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", self.SCOPES)
                self.creds = flow.run_local_server(port=8)

            print("Writing the token")
            with open("token.json", "w") as token:
                token.write(self.creds.to_json())

    def format_event_time(self, iso_time):

        event_time = dt.datetime.fromisoformat(iso_time)

        return event_time.strftime("%d %b %Y, %H:%M ")

    def get_events(self):
        self.connect_to_api()

        events_list = []

        try:
            service = build("calendar", "v3", credentials=self.creds)
            now = dt.datetime.now().isoformat() + "Z"
            event_result = service.events().list(
                calendarId="primary", timeMin=now, maxResults=10, singleEvents=True, orderBy="startTime"
            ).execute()

            events = event_result.get("items", [])

            if not events:
                print("No upcoming events found!")
                return "You have no upcoming events 🌞"

            for event in events:
                start = event["start"].get("dateTime", event["start"].get("date"))
                formatted_time = self.format_event_time(start)
                event_str = f"Event: {event['summary']} at {formatted_time}"
                events_list.append(event_str)

            # Format the list into a more readable message
            message = "Your upcoming events are:\n"
            for event in events_list:
                message += f"\n- {event}"

            return message

        except HttpError as error:
            error_msg = f"An error occurred: {error}"
            return error_msg

    def create_event(self):
        self.connect_to_api()

        try:
            service = build("calendar", "v3", credentials=self.creds)

            event = {
                "summary": "🥳Roy Birthday🥳",
                "location": "Google Meet!",
                "description": "Its Roy's Birthday! our time of the year to meetup!"
                               "\nThis Event was create by Jarvis - bot created by me :)",
                "colorId": random.randint(1, 8),
                "start": {
                    "date": "2024-12-29",
                    "timeZone": "Asia/Jerusalem"
                },
                "end": {
                    "date": "2024-12-30",
                    "timeZone": "Asia/Jerusalem"
                },

                "attendees": [
                    {"email": "razfarage3232@gmail.com"},
                    {"email": "tomergal1404@gmail.com"},
                    {"email": "royhadad98@gmail.com"}

                ]
            }

            event = service.events().insert(calendarId="primary", body=event).execute()

            print(f"Event create {event.get('htmlLink')}")

        except HttpError as error:
            error_msg = f"An error occurred: {error}"
            return error_msg

wa = Whatsapp_Client()
cc = Calender_Client()
cc.create_event()