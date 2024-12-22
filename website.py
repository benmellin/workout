from flask import Flask
from workoutgen import *
app = Flask(__name__)
import json
from datetime import datetime

app = Flask(__name__)

WORKOUT_FILE = 'workout.json'  # File to store the workout and last update date


def get_daily_workout():
    """Retrieve today's workout or generate a new one if not yet created for today."""
    try:
        # Load the saved workout and date
        with open(WORKOUT_FILE, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # File doesn't exist or is corrupted, initialize new data
        data = {}

    today = datetime.now().strftime('%Y-%m-%d')

    if data.get("date") == today:
        # If the workout is already set for today, return it
        return data["workout"]
    else:
        # Otherwise, generate a new workout and save it
        new_workout = level_1_workout_gen()
        data = {"date": today, "workout": new_workout}

        with open(WORKOUT_FILE, 'w') as file:
            json.dump(data, file)

        return new_workout

@app.route('/')
def home():
    workout = get_daily_workout()
   
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>The Workoutle.</title>
    </head>
    <body>
        <h1>The Workoutle.</h1>
        <p>A constantly varied, daily, bodyweight workout you can do anywhere.</p>
         <p>Today's Workoutle:</p>

        <p>{workout}</p>

    </body>
    </html>


    """





if __name__ == '__main__':
    app.run(debug=True)