import requests
from datetime import datetime
import os

APP_ID = os.environ["ID"]
print(APP_ID)
API_KEY = "65ff6e5d43890e377401d1867d5038f4"
AGE = 21
GENDER = "Male"
WEIGHT = 71.3
HEIGHT= 173

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/6dfe38856b6139bc887888dcd700618e/workoutTracking/workouts"
exercise_header = {
    'x-app-id': APP_ID,
    'x-app-key':API_KEY
}
params = {
    "query": input("Tell me which exercise you did: "),
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT,
    "age":AGE
}

response1 = requests.post(url = exercise_endpoint,json = params , headers=exercise_header)
results = response1.json()
print(results)
print(results["exercises"][0])

# today_date = datetime.now().strftime("%d/%m/%Y")
# now_time = datetime.now().strftime("%X")
#
#
# for exercise in results["exercises"]:
#     print(exercise)
    # sheet_inputs = {
    #     "workout": {
    #         "date": today_date,
    #         "time": now_time,
    #         "exercise": exercise["name"].title(),
    #         "duration": exercise["duration_min"],
    #         "calories": exercise["nf_calories"]
    #     }
    # }
    #
    # header = {
    #     "Authorization": "Basic bnVsbDpudWxs"
    # }
    #
    # response2=requests.post(url = sheet_endpoint, json = sheet_inputs ,headers = header)
    # print(response2.text)
