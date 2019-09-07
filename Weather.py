import requests
import urllib.request
from tkinter import Tk
import tkinter as tk
from tkinter import *
import sys
import json
import datetime
from tkinter import ttk
from tkinter import messagebox
import urllib.parse


class WeatherReporter:

    weather_data = None
    APIKEY = '7b19fb9cec9e569b19449a0b46193826'

    def __init__(self, root):
        self.root = root
        self.create_top_frame()
        self.create_weather_display_frame()
        root.resizable (0,0)

    def create_top_frame(self):
        frame = Frame(self.root)
        frame.pack(side="top")
        Label(frame, text='Unesi grad:').pack(side="left")
        self.location = StringVar()
        Entry(frame, textvariable=self.location).pack(side="left")
        ttk.Button(frame, text='Go', command=self.on_show_weather_button_clicked).pack(
            side="left")

    def create_weather_display_frame(self):
        self.canvas = Canvas(
            self.root, height='425', width='340', background='black')
        self.canvas.create_rectangle(10, 10, 330, 415, fill='blue')
        self.canvas.pack(side="bottom")

    def on_show_weather_button_clicked(self):
        if not self.location.get():
            return
        self.clear_canvas()
        self.get_weather_data()
        self.format_data()
        self.display_data()

    def get_weather_data(self):
        self.weather_data = self.podaci()
        self.weather_data = self.json_to_dict(self.weather_data)

    def clear_canvas(self):
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(10, 10, 330, 415, fill='blue')

    def format_data(self):
        data = self.weather_data
        self.name = data['name']
        self.latitude = self.str2num(data['lat'], 3)
        self.longitude = self.str2num(data['lon'], 3)
        self.country = data['country']
        self.time_now = self.time_stamp_to_data(data['dt'])
        self.description = data['description']
        self.icon_name = "weatherimages/{}.png".format(data['icon'].lower())
        self.clouds = data['all'] + ' %'
        self.sunrise_time = self.time_stamp_to_time(data['sunrise'])
        self.sunset_time = self.time_stamp_to_time(data['sunset'])
        self.temp_now_in_celcius = self.str2num(
            self.kelvin_to_celsius(float(data['temp'])), 2) + u' \u2103'
        self.temp_now_in_fahrenheit = self.str2num(
            self.kelvin_to_fahrenheit(float(data['temp'])), 2) + u' \u2109'
        self.temp_min_in_celcius = self.str2num(
            self.kelvin_to_celsius(float(data['temp_min'])), 2) + u' \u2103'
        self.temp_max_in_celcius = self.str2num(
            self.kelvin_to_celsius(float(data['temp_max'])), 2) + u' \u2103'

    def kelvin_to_celsius(self, k):
        return k - 273.15

    def kelvin_to_fahrenheit(self, k):
        return (k * 9 / 5 - 459.67)

    def str2num(self, string, precision):
        return "%0.*f" % (precision, float(string))

    def display_data(self):
        if not self.weather_data:
            messagebox.showerror(
                'Name not found', 'Unable to fetch record - Name not found')
            return
        data = self.weather_data
        opts = {'fill': 'white', 'font': 'Helvetica 12'}
        self.canvas.create_text(52, 30, text = self.name, **opts)
        self.canvas.create_text(
            245, 35, text='Latitude:' + self.latitude, **opts)
        self.canvas.create_text(
            245, 53, text='Longitude: ' + self.longitude, **opts)
        self.canvas.create_text(
            55, 50, text='Država: ' + self.country, **opts)
        self.canvas.create_text(155, 80, text=self.time_now, **opts)
        self.canvas.create_text(85, 105, text='Trenutno:', **opts)
        self.img = PhotoImage(file=self.icon_name)
        self.canvas.create_image(140, 105, image=self.img)
        self.canvas.create_text(240, 105, text=self.description, **opts)
        self.canvas.create_text(80, 155, text='Temperatura:', **opts)
        self.canvas.create_text(
            87, 175, text=self.temp_min_in_celcius + ' ~ ' + self.temp_max_in_celcius, **opts)
        self.canvas.create_text(
            225, 140, text=self.temp_now_in_celcius, **opts)
        self.canvas.create_text(
            225, 180, text=self.temp_now_in_fahrenheit, **opts)
        self.canvas.create_text(89, 215, text='Relativna vlažnost:', **opts)
        self.canvas.create_text(198, 215, text=data['humidity'] + ' %', **opts)
        self.canvas.create_text(72, 235, text='Brzina vjetra:', **opts)
        self.canvas.create_text(205, 235, text=data['speed'] + ' m/s ', **opts)
        self.canvas.create_text(71, 255, text='Jačina vjetra', **opts)
        self.canvas.create_text(
            223, 255, text=data['deg'] + ' stepeni', **opts)
        self.canvas.create_text(55, 275, text='Pritisak:', **opts)
        self.canvas.create_text(
            225, 275, text=data['pressure'] + ' millibara', **opts)
        if '3h' in data:
            self.canvas.create_text(83, 293, text='Rain (Last 3h)', **opts)
            self.canvas.create_text(
                200, 293, text=data['3h'] + ' mm', **opts)  # rain
        self.canvas.create_text(58, 310, text='Oblačnost', **opts)
        self.canvas.create_text(200, 310, text=self.clouds, **opts)  # clouds
        self.canvas.create_text(70, 328, text='Izlazak sunca', **opts)
        self.canvas.create_text(200, 328, text=self.sunrise_time, **opts)
        self.canvas.create_text(73, 343, text='Zalazak sunca', **opts)
        self.canvas.create_text(200, 343, text=self.sunset_time, **opts)
        self.canvas.create_text(159, 378, text='Preuzeto sa:', **opts)
        self.canvas.create_text(
            159, 398, text='www.openweathermap.org', **opts)

    def time_stamp_to_time(self, ts):
        return (datetime.datetime.fromtimestamp(int(ts)).strftime('%H:%M:%S'))

    def time_stamp_to_data(self, ts):
        return (datetime.datetime.fromtimestamp(int(ts)).strftime('%Y-%m-%d %H:%M:%S'))

    def podaci(self):
        try:
            params = urllib.parse.urlencode(
                {'q': self.location.get(), 'APPID': self.APIKEY}, encoding="utf-8")
            api_url = (
                'http://api.openweathermap.org/data/2.5/weather?{}'
                .format(params)
            )
            with urllib.request.urlopen(api_url) as f:
                json_data = f.read()
                return json_data
        except IOError as e:
            messagebox.showerror(
                'Unable to connect', 'Unable to connect %s' % e)
            sys.exit(1)

    def json_to_dict(self, json_data):
        decoder = json.JSONDecoder()
        decoded_json_data = decoder.decode(json_data.decode("utf-8"))
        flattened_dict = {}
        for key, value in decoded_json_data.items():
            if key == 'weather':
                for ke, va in value[0].items():
                    flattened_dict[str(ke)] = str(va).upper()
                continue
            try:
                for k, v in value.items():
                    flattened_dict[str(k)] = str(v).upper()
            except:
                flattened_dict[str(key)] = str(value).upper()
        return flattened_dict


def main():
    root = Tk()
    WeatherReporter(root)
    root.mainloop()

if __name__ == '__main__':
    main()
