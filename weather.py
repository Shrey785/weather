from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

#creating an window using tkinter
root = Tk()
root.title("Weather App")
root.geometry("900x500+200+100")

def getWeather():
    city = textfield.get()
    
    geolocator = Nominatim(user_agent="geoapiExersice")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    
    print(result)

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="TIME:")
#using api to help get info of any area a user wants to find
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=fe5fbea56e8cc85a78e6cbfa56205b25"
    
    json_data = requests.get(api).json()
    condition = json_data["weather"][0]["main"]
    description = json_data["weather"][0]["description"]
    temp = int(json_data["main"]["temp"] - 273.15)
    pressure =json_data["main"]["pressure"]
    humidity = json_data["main"]["humidity"]
    wind = json_data["wind"]["speed"]


    t.config(text=(temp,"°"))
    c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))
    
    w.config(text=(wind,"km/h"))
    h.config(text=(humidity,"%"))
    d.config(text=description)
    p.config(text=(pressure,"hPa"))

#to create a search bar
search_tab = PhotoImage(file="tab.png")
myimage = Label(image=search_tab)
myimage.place(x=20,y=15)

textfield= tk.Entry(root,width=17,font=('Arial', 15, 'bold'),bg="#404040", border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

#search icon
search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=search_icon, borderwidth=0,cursor="hand2",bg="#404040", border=0,fg="white", command=getWeather)
myimage_icon.place(x=400,y=28)

Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

#using to find time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 15))
clock.place(x=30,y=130)

label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg ="white",bg="#1ab5ef")
label1.place(x=110,y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg ="white",bg="#1ab5ef")
label2.place(x=240, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg ="white",bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg ="white",bg="#1ab5ef")
label4.place(x=650, y=400)

t=Label(font=("arial", 70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial", 15, "bold"))
c.place(x=400,y=250)

#setting up wind ,humidity,pressure and description
w=Label(text="...",font=("arial", 15,"bold"),bg="#1ab5ef")
w.place(x=110,y=430)
h=Label(text="...",font=("arial", 15,"bold"),bg="#1ab5ef")
h.place(x=280, y=430)
d=Label(text="...",font=("arial", 15,"bold"),bg="#1ab5ef")
d.place(x=450, y=430)
p=Label(text="...",font=("arial", 15,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)

text_box = tk.Entry()
root.mainloop()