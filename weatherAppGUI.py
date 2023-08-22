from tkinter import *
import requests
import json
import tkinter.messagebox as tmsg
dic = {}
def on_entry_click(event):
    if cityname.get() == "Enter City Name":
        entry.delete(0, END)
        entry.config(fg="black")

def checkWeather():
    global dic    
    dic.clear() 
    url = f"https://api.weatherapi.com/v1/current.json?key=78d424f8cfd049b0be7185342231008&q={cityname.get()}"
    r = requests.get(url)
    dic = json.loads(r.text)
    printData()
    
def printData():
    global dic 
    for item_id in square.find_withtag("weather"):
        square.delete(item_id)
    try:  
        i=0
        square.create_text(350, 170 * (i+1)/4 , text=dic["location"]["name"], font="lucida 10 bold", anchor="w", tags="weather")
        square.create_text(350, 170 * (i+2)/4 , text=dic["location"]["region"], font="lucida 10 bold", anchor="w", tags="weather")
        square.create_text(350, 170 * (i+3)/4 , text=dic["location"]["lat"], font="lucida 10 bold", anchor="w", tags="weather")
        square.create_text(350, 170 * (i+4)/4 , text=dic["location"]["lon"], font="lucida 10 bold", anchor="w", tags="weather")
        square.create_text(350, 170 * (i+5)/4 , text=dic["current"]["temp_c"], font="lucida 10 bold", anchor="w", tags="weather")
        square.create_text(350, 170 * (i+6)/4 , text=dic["current"]["temp_f"], font="lucida 10 bold", anchor="w", tags="weather")
    except:
       tmsg.showerror("Error", "Invalid Location")


root = Tk()
root.title("  Weather Forecast System")
root.geometry("800x500")
root.wm_iconbitmap("weather.ico")

Label(root, text="Weather Foresact System", font="lucida 30 bold", bg="Light blue").pack(side=TOP, fill=X)

cityname = StringVar()
cityname.set("")
try:
    entry = Entry(root, textvariable=cityname, font="lucida 20", borderwidth=5, fg="grey")
    entry.insert(1, "Enter City Name")
    entry.bind("<FocusIn>", on_entry_click)
    entry.pack(pady=10, ipadx=50)
except EXCEPTION as e:
    print("An error occured", e)

btn = Button(root, text="Check!!", font="lucida 10", bg="light blue", padx=10, pady=5, command=checkWeather)
btn.pack(pady=10)

txt1 = StringVar()
txt1.set("Created By Irtaza Manzoor")
statusbar = Label(root, textvariable = txt1, bg="light blue", fg = "Black",pady=10, font="lucida 10 bold")
statusbar.pack(side=BOTTOM, fill=X)


square = Canvas(root, width=800, height=500)
square.pack()
square.create_rectangle(120,20,700,270)

items = ["Location: ", "Region: ", "Latitude: ", "Longitude: ", "Temperature Celsius: ", "Temperature Farhenheit: "]
for i,item in enumerate(items):
    square.create_text(150, 170 * (i+1)/4 , text=item, font="lucida 10 bold", anchor="w")

root.mainloop()