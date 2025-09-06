'''
This project is not mine. I have taken the code from pythongeeks,org, link of the project is : https://pythongeeks.org/python-live-weather-desktop-notifications
I've made some changes in the source code, however, to match my programming style.
'''

import time
import tkinter as tk
from tkinter import messagebox as mb
from ttkbootstrap import Style
import requests
from plyer import notification as notif
import json



# Base & Icon URL to access weather data, will add to the URLs later
baseURL =  "http://api.openweathermap.org/data/2.5/weather?"
# iconURL = "http://openweathermap.org/img/wn/"

class weatherAlert(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Weather Alert")
        self.geometry("700x200")
        style = Style(theme="flatly")
        style.configure("Custom.TEntry", foreground="gray")

        tk.Label(self, text="Weather Alert", font=('Georgia', 15), fg='grey19', bg='azure').place(x=100, y=15)
        tk.Label(self, text='Location:', font=("Georgia", 13),bg='azure').place(relx=0.05, rely=0.3)

        self.place = tk.StringVar(self)
        self.place_entry = tk.Entry(self, width=50, textvariable=self.place)
        self.place_entry.place(relx=0.5, rely=0.3)

        btn = tk.Button(self, text="Get Alert", font=7, fg='grey19', command=self.getNotification).place(relx=0.4, rely=0.75)

    
    def getNotification(self):
        cityName = self.place.get()

        try:
            data = self.requestData(cityName)
        
            main = data["main"]
            temp = main["temp"]
            temp-=273
            pres = main["pressure"]
            hum = main["humidity"]
            weather_data = data["weather"]
            weather_desc = weather_data[0]["description"]
            # icon = weather_data[0]["icon"]
            # iconURL += f"{icon}@2x.png"

            info = f"Weather for {cityName.upper()} is {weather_desc}" + \
                   f"\nTemperature = {round(temp, 1)}°C" + \
                   f"\nAtmospheric Pressure = {pres} hPa" + \
                   f"\nHumidity = {hum}%"
            self.give_notification(cityName, info)
        
        except Exception:
            mb.showerror('Error', f"Place \"{cityName}\" is not found")

    def requestData(self, city):
        url = baseURL + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city
        response = requests.get(url)
        return response.json()
    
    def give_notification(self, place, info):
        notif.notify(title=f"WEATHER REPORT for {place.upper()}", message=info, timeout=2)
        time.sleep(7)

if __name__ == '__main__':
    app = weatherAlert()
    app.mainloop()