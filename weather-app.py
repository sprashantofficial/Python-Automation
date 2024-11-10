import tkinter as tk
from io import BytesIO
from tkinter import messagebox
import requests
from PIL import Image, ImageTk


API_KEY = "PUT YOUR API KEY HERE"


def get_city_coordinates(city):
    geocoding_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
    response = requests.get(geocoding_url)

    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['lat'], data[0]['lon']
        else:
            messagebox.showerror("Error", f"City '{city}' not found.")
    else:
        messagebox.showerror("Error", f"Geocoding API error: {response.status_code}")
    return None


def get_weather_data(lat, lon):
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(weather_url)

    if response.status_code == 200:
        return response.json()
    else:
        messagebox.showerror("Error", f"Weather API error: {response.status_code}")
        return None


def get_air_pollution(lat, lon):
    pollution_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(pollution_url)

    if response.status_code == 200:
        return response.json()['list'][0]
    else:
        messagebox.showerror("Error", f"Air Pollution API error: {response.status_code}")
        return None


def show_weather_and_air_pollution():
    city = city_entry.get()
    if city:
        coordinates = get_city_coordinates(city)
        if coordinates:
            lat, lon = coordinates

            weather_data = get_weather_data(lat, lon)
            if weather_data:
                update_weather_display(weather_data)

            pollution_data = get_air_pollution(lat, lon)
            if pollution_data:
                update_air_pollution_display(pollution_data)
        else:
            messagebox.showerror("Error", "City not found.")
    else:
        messagebox.showerror("Error", "Please enter a city name.")


def update_weather_display(weather_data):
    temp = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    icon_code = weather_data['weather'][0]['icon']

    weather_label.config(text=f"{temp}°C, {description.title()}")

    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
    icon_response = requests.get(icon_url)
    icon_image = Image.open(BytesIO(icon_response.content))
    icon_image = icon_image.resize((100, 100), Image.Resampling.LANCZOS)

    icon_photo = ImageTk.PhotoImage(icon_image)
    weather_icon_label.config(image=icon_photo)
    weather_icon_label.image = icon_photo


def classify_air_quality(aqi):
    if aqi == 1:
        return "Good"
    elif aqi == 2:
        return "Moderate"
    elif aqi == 3:
        return "Unhealthy for Sensitive Groups"
    elif aqi == 4:
        return "Unhealthy"
    else:
        return "Hazardous"


def update_air_pollution_display(pollution_data):
    aqi = pollution_data['main']['aqi']
    pollutants = pollution_data['components']

    air_quality_class = classify_air_quality(aqi)

    air_quality_label.config(text=f"Air Quality Index (AQI): {aqi} ({air_quality_class})")
    pollutants_label.config(
        text=f"PM2.5: {pollutants['pm2_5']} µg/m³\nPM10: {pollutants['pm10']} µg/m³\nNO2: "
             f"{pollutants['no2']} µg/m³\nSO2: {pollutants['so2']} µg/m³\nCO: "
             f"{pollutants['co']} µg/m³")


# Parent Window
root = tk.Tk()
root.title("Weather & Air Pollution App")
root.geometry("400x650")
root.configure(bg="#2A2A2A")

# Top Frame
top_frame = tk.Frame(root, bg="#2A2A2A", bd=10)
top_frame.pack(pady=20)
title_label = tk.Label(top_frame, text="Weather & Air Pollution App", font=("Helvetica", 20, "bold"), fg="white",
                       bg="#2A2A2A")
title_label.pack()

# City Entry
input_frame = tk.Frame(root, bg="#2A2A2A")
input_frame.pack(pady=10)
city_entry = tk.Entry(input_frame, font=("Helvetica", 14), width=20, bd=2, relief="flat", fg="white", bg="#333333",
                      insertbackground="white")
city_entry.pack(side=tk.LEFT, padx=10)

# Search Button
search_btn = tk.Button(input_frame, text="Search", font=("Helvetica", 12), bg="#00AAFF", fg="white",
                       activebackground="#00CCFF",
                       relief="flat", padx=10, pady=5, command=show_weather_and_air_pollution)
search_btn.pack(side=tk.LEFT)

# Weather Display Section
weather_frame = tk.Frame(root, bg="#2A2A2A")
weather_frame.pack(pady=20)
weather_label = tk.Label(weather_frame, text="Weather: --", font=("Helvetica", 16), fg="white", bg="#2A2A2A")
weather_label.pack()
weather_icon_label = tk.Label(weather_frame, bg="#2A2A2A")
weather_icon_label.pack(pady=10)

# Air Pollution Section
pollution_frame = tk.Frame(root, bg="#2A2A2A")
pollution_frame.pack(pady=20)
air_quality_label = tk.Label(pollution_frame, text="Air Quality Index (AQI): --", font=("Helvetica", 16), fg="white",
                             bg="#2A2A2A")
air_quality_label.pack(pady=10)
pollutants_label = tk.Label(pollution_frame, text="PM2.5: --, PM10: --, NO2: --, SO2: --, CO: --",
                            font=("Helvetica", 14), fg="white", bg="#2A2A2A", justify="left")
pollutants_label.pack()

root.mainloop()
