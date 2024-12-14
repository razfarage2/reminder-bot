# import schedule
# from clients.weather_client import Weather_Client
# from clients.whatsapp_client import Whatsapp_Client
# import datetime
# from dotenv import load_dotenv
#
#
# load_dotenv()
# get_message = lambda message: message
#
# iac_days = ["Sunday", "Monday", "Wednesday"]
#
# open_uni_days = {
#     "Tuesday": "You have Class today - Statistics.",
#     "Thursday": "You have Class today - Intro To Psychology.",
# }
#
# assignment_days = {
#     "Wednesday": "Dont forget you have to turn in your assignment Tomorrow.",
#     "Thursday": "You need to turn in your assignment Today.",
#     "Saturday": "Reminder: Assignment submission due by Monday.",
# }
#
#
# def run_tasks():
#     current_day = datetime.datetime.now().strftime("%A")
#
#     for day in iac_days:
#         if current_day == day:
#             schedule.every().day.at("15:30").do(
#                 lambda day=day: wa_client.custom_message(f"Weather for {day}: {we_client.get_weather()}")
#             )
#
#     for day, message in open_uni_days.items():
#         if current_day == day:
#             schedule.every().day.at("10:30").do(
#                 lambda message=message: wa_client.custom_message(
#                     f"Class reminder: {get_message(message)}"
#                 )
#             )
#
#     for day, message in assignment_days.items():
#         if current_day == day:
#             schedule.every().day.at("11:02").do(
#                 lambda message=message: wa_client.custom_message(
#                     f"Assignment reminder: {get_message(message)}"
#                 )
#             )
