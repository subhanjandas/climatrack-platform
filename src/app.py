from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
import requests
from datetime import datetime

app = Flask(__name__)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client['climatrack']
weather_collection = db['weather_data']

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/get_weather", methods=["POST"])
def get_weather():
    city_coords = request.form.get("city")
    if city_coords:
        lat, lon = city_coords.split(",")
        api_key = 'v0Z4QXKPryNSpRoFJRRH1ZPDnNdZ1jkB'  # Replace with your Tomorrow.io API key
        url = f'https://api.tomorrow.io/v4/timelines?location={lat},{lon}&fields=temperature,temperatureApparent,dewPoint,humidity,windSpeed,windDirection,windGust,pressureSurfaceLevel,precipitationProbability,cloudCover,visibility&timesteps=1h&units=metric&apikey={api_key}'

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            if 'data' in data and 'timelines' in data['data'] and data['data']['timelines']:
                latest_data = data['data']['timelines'][0]['intervals'][0]['values']
                weather_data = {
                    'city': city_coords,
                    'timestamp': datetime.now(),
                    'temperature': latest_data['temperature'],
                    'temperatureApparent': latest_data['temperatureApparent'],
                    'dewPoint': latest_data['dewPoint'],
                    'humidity': latest_data['humidity'],
                    'windSpeed': latest_data['windSpeed'],
                    'windDirection': latest_data['windDirection'],
                    'windGust': latest_data['windGust'],
                    'pressureSurfaceLevel': latest_data['pressureSurfaceLevel'],
                    'precipitationProbability': latest_data['precipitationProbability'],
                    'cloudCover': latest_data['cloudCover'],
                    'visibility': latest_data['visibility']
                }
                weather_collection.insert_one({'type': 'weather', 'data': weather_data})
                return redirect(url_for('view_weather', city=city_coords))
            else:
                return "API response structure has changed. Required keys not found.", 500
        else:
            return f"Failed to get weather data: {response.status_code} - {data}", 500
    return "Please select a city", 400

@app.route("/view_weather")
def view_weather():
    city_coords = request.args.get("city")
    if city_coords:
        weather_data = weather_collection.find_one({'data.city': city_coords}, sort=[('data.timestamp', -1)])
        if weather_data:
            return render_template('weather.html', weather=weather_data['data'])
    return "No weather data available", 404

if __name__ == "__main__":
    app.run(debug=True)
