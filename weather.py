from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=ea17916d1a6c52530ac56201c06f9ca0").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])


win = Tk ()
win.title(" Today's weather ")
win.config(bg = "pink")
win.geometry("500x580")


name_label = Label (win,text="Weather App",
                    font=("Algerian",30,"bold"))
name_label.place (x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="Weather App",values=list_name,
                    font=("Algerian",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)


w_label = Label(win,text="Weather climate",
                    font=("Algerian",20))
w_label.place(x=25,y=260,height=50,width=210)

w_label1 = Label(win,text="",
                    font=("Algerian",20))
w_label1.place(x=255,y=260,height=50,width=210)



wb_label = Label(win,text="Weather Description",
                    font=("Algerian",17))
wb_label.place(x=25,y=330,height=50,width=210)

wb_label1 = Label(win,text="",
                    font=("Algerian",17))
wb_label1.place(x=255,y=330,height=50,width=210)



temp_label = Label(win,text="Temperature",
                    font=("Algerian",20))
temp_label.place(x=25,y=400,height=50,width=210)

temp_label1 = Label(win,text="",
                    font=("Algerian",20))
temp_label1.place(x=255,y=400,height=50,width=210)



per_label = Label(win,text="Pressure",
                    font=("Algerian",20))
per_label.place(x=25,y=470,height=50,width=210)

per_label1 = Label(win,text="",
                    font=("Algerian",20))
per_label1.place(x=255,y=470,height=50,width=210)


submit_button = Button(win,text="Submit",
                    font=("Algerian",20,"bold"),command=data_get)
submit_button.place(y=190,height=50,width=100,x=200)



win.mainloop()