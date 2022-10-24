#Comment lines define the date information. You can enable them in your code
from tkinter import *
import time
from tkinter import Label,Tk

app_window=Tk()
app_window.title("Dijital Saat")
app_window.geometry("400x150")
app_window.resizable(1,1)

text_font=("Times",70,"bold italic")
background="#000000"
foreground="#ffffff"
border_width=25

label=Label(app_window,font= text_font, bg=background,fg=foreground,bd=border_width)
label.grid(row=0,column=1)
#label2=Label(app_window,font= text_font, bg=background,fg=foreground,bd=border_width)
#label2.grid(row=1,column=1)


def digital_clock():
    time_live= time.strftime("%H:%M:%S")
    date_live=time.strftime("%d/%m/%Y")
    label.config(text=time_live)
    #label2.config(text=date_live)
    label.after(200,digital_clock)
    #label2.after(200,digital_clock)

digital_clock()
app_window.mainloop()




