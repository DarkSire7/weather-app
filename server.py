from flask import Flask, request, render_template
from weather import get_weather_data
from waitress import serve

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/weather")
def get_weather():
    city = request.args.get("city")
    if not bool(city.strip()):
        city = "Hyderabad"

    weather_data = get_weather_data(city)

    if weather_data["cod"] != 200:
        return render_template("city_not_found.html")

    return render_template(
        "weather.html",
        title=weather_data["name"],
        temp=f"{weather_data['main']['temp']:.1f}",
        description=weather_data["weather"][0]["description"].capitalize(),
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
