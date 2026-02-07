from flask import Flask, render_template, request
import requests
app = Flask(__name__)
API_KEY = "98284da501aa12de56f8e74f07155135"

def aqi_parameters(aqi):
    if aqi<=50:
        return "Air this clean doesn’t come every day — open those windows!"
    elif aqi<=100:
        return "Light exercise outdoors is fine, just avoid peak traffic roads."
    elif aqi<=200:
        return "Air quality is manageable, but indoor workouts may feel better."
    else:
        return "Masks help, especially near traffic-heavy areas."

@app.route("/", methods=["GET","POST"])

    def home():
        data = none
    
        if request.method == "POST":
            city = request.form["city"]

            # loctions into longitude and latititude
            geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
            geo_data = requests.get(geo_url).json()

            if geo_data:
                lat = geo_data[0]["lat"]
                lon = geo_data[0]["lon"]
                
                aqi_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
                aqi_data=requests.get(aqi_url).json()
                aqi = aqi_data["list"][0]["main"]["aqi"]

                weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
                weather = requests.get(weather_url).json()

                category, advice = classify_aqi()

                data = {
                    "city": city,
                    "aqi": aqi,
                    "category": category,
                    "advice": advice,
                    "temp": weather["main"]["temp"],
                    "humidity": weather["main"]["humidity"]
                    "wind": weather["wind"]["speed"]
                }

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)


    
    
