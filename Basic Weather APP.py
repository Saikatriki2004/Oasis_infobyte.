#Basic Weather App
from tkinter import *
from tkinter import ttk
import urllib.request
import json

def data_get():
    city = city_name.get()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=5acfb57dadd3bcbe5cd6cb2d9be299d2"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            w_label1.config(text=data["weather"][0]["main"])
            wb_label1.config(text=data["weather"][0]["description"])
            temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
            per_label1.config(text=data["main"]["pressure"])
    except Exception as e:
        print(f"Error: {e}")
        w_label1.config(text="N/A")
        wb_label1.config(text="N/A")
        temp_label1.config(text="N/A")
        per_label1.config(text="N/A")

win = Tk()

win.title("RIKI")
win.config(bg="blue")
win.geometry("500x570")  # Corrected the geometry format

name_label = Label(win, text="RIKI Weather App",
                   font=("Times New Roman", 30, "bold"))  # Corrected the font name
name_label.place(x=25, y=50, height=50, width=450)
city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com = ttk.Combobox(win, text="RIKI Weather App", values=list_name,
                   font=("Times New Roman", 20, "bold"), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

w_label = Label(win, text="Weather Climate", font=("Times New Roman", 20))  
w_label.place(x=25, y=260, height=50, width=210)

w_label1 = Label(win, text="", font=("Times New Roman", 20))  
w_label1.place(x=250, y=260, height=50, width=210)

wb_label = Label(win, text="Weather Description", font=("Times New Roman", 17))  
wb_label.place(x=25, y=330, height=50, width=210)

wb_label1 = Label(win, text="", font=("Times New Roman", 17))  
wb_label1.place(x=250, y=330, height=50, width=210)

temp_label = Label(win, text="Temperature", font=("Times New Roman", 20))  
temp_label.place(x=25, y=400, height=50, width=210)

temp_label1 = Label(win, text="", font=("Times New Roman", 20))  
temp_label1.place(x=250, y=400, height=50, width=210)

per_label = Label(win, text="Pressure", font=("Times New Roman", 20))  
per_label.place(x=25, y=470, height=50, width=210)

per_label1 = Label(win, text="", font=("Times New Roman", 20))  
per_label1.place(x=250, y=470, height=50, width=210)

done_button = Button(win, text="Done", font=("Times New Roman", 20, "bold"), command=data_get)
done_button.place(y=190, height=40, width=100, x=200)

win.mainloop()
