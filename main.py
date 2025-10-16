import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image
import webbrowser
import datetime
import pygame
import requests as rq
from gui import Frame,Frame_Switcher,Home_Page,Weather_Frame,News_Page_Frame,Finance_Page_Frame,Notification
from weather_scraper import Weather_Details_Provider
from news_scraper import General_News_Provider
from finance_scraper import Finance_News_Finder,Stock_Detail_Fetcher
import ctypes

#adding dpi awareness
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass


OFFLINE = False


pygame.mixer.init()
button_click_sound = pygame.mixer.Sound(r"icons\ui-button-click-5-327756.mp3")
post_transition_sound = pygame.mixer.Sound(r"icons\level-up-02-199574.mp3")
post_transition_sound.set_volume(0.4)

#gui_attributes
BG_COLOR = "#1E2A36"
TEXT_COLOR1 = "#FFFFFF"
TEXT_COLOR2 = '#C7D2DC'
BUTTON_COLOR = "#3BA3FC"
FRAME_COLOR = "#26333F"
BUTTON_HOVER_COLOR = "#3493e5"
DROPDOWN_HOVER_COLOR = "#2F3D4A"
CONFIRM_BTN_HOVER = "#3189d1"
NEWS_FRAME_COLOR = "#3B4C5C"
GAIN_COLOR = "#4CAF50"
LOSS_COLOR = "#E53935"


win = ctk.CTk(fg_color=BG_COLOR)
win.wm_title("InfoLens")
SCREEN_WIDTH = win.winfo_screenwidth()
SCREEN_HEIGHT = win.winfo_screenheight()
geometry = f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}-25+10"
option_variable = tk.StringVar(win,value = "News")
values = ["                       News                     ","                   Finance             ","                 Weather         "]

def check_internet_connectivity():
    global OFFLINE
    try:
        response = rq.get("https://www.google.com")
        OFFLINE = False
    except rq.exceptions.ConnectionError:
        OFFLINE = True
    
    win.after(5000,check_internet_connectivity)

check_internet_connectivity()
#scraper_objects
weather_provider = Weather_Details_Provider()
news_provider = General_News_Provider()
stock_provider = Stock_Detail_Fetcher()
finance_news_provider = Finance_News_Finder()

#objects

frames = Frame()
frames.set_window(win)
home_page_frame = Home_Page(option_variable,values)

weather_page_frame = Weather_Frame()
news_page_frame = News_Page_Frame()
finance_page_frame = Finance_Page_Frame()
notification = Notification()

frame_list = [home_page_frame,weather_page_frame,news_page_frame,finance_page_frame]
frame_selector = Frame_Switcher()
frame_selector.set_frame_list(frame_list)
frame_selector.set_frame("Home")

#commandsfor button functions
def show_notification():
    
    text = '''InfoLens is your personalized, real-time information hub — built for clarity, speed, and simplicity.

            Whether you're tracking the latest headlines, monitoring stock market updates, or checking live weather conditions, InfoLens delivers focused content in one unified dashboard — without distractions, without clutter.

            Simply choose your desired category, click Confirm, and let InfoLens fetch, format, and display data tailored just for you.'''

    notification = messagebox.showinfo(title = "InfoLens Guide",message = text)



def switch_frame():
    frame_name = option_variable.get().strip()
    frame_selector.set_frame(frame_name)


def update_weather():
    if OFFLINE:
        notification.notify("Offline")
    else:
        button_click_sound.play()
        weather_page_frame.widgets["progressbar"].place(x = 335, y= 225)
        win.update()
        win.after(100,fetch_weather)
        win.after(100,post_transition_sound.play)
        weather_page_frame.widgets["search_button"].configure(state = "disabled")
        win.after(2000,lambda: weather_page_frame.widgets["search_button"].configure(state = "normal"))
        win.after(100,weather_page_frame.widgets["progressbar"].place_forget())

def fetch_weather():
    state_name = weather_page_frame.widgets["entryfield"].get()
    weather_url = f"https://wttr.in/{state_name}?format=j1"
    html = rq.get(weather_url)
    if html.status_code == 404 or state_name == "":
        messagebox.showerror(title = "Invalid Input",message = "The following data is invalid. Please try again.")
        return
    else:
        wd = weather_provider.provide_details(state_name,html)

        widgets = weather_page_frame.widgets

        widgets["temperature"].configure(text = f"Temperature: {wd["temp_c"]}")
        widgets["weatherdesc"].configure(text = f"Condition: {wd["weather_desc"]}",wraplength = 160)
        widgets["humidity"].configure(text = f"Humidity: {wd["humidity"]}")
        widgets["wind_speed"].configure(text = f"Temperature: {wd["wind_speed"]}")
        widgets["sunrise"].configure(text = f"Sunrise: {wd["sunrise"]}")
        widgets["sunset"].configure(text = f"Sunset: {wd["sunset"]}")
        widgets["max_temp"].configure(text = f"Max Temp(C): {wd["max_temp"]}")
        widgets["min_temp"].configure(text = f"Min Temp(C): {wd["min_temp"]}")
        widgets["moonphase"].configure(text = f"Moon Phase:{wd["moon_phase"]}")


def show_news():
    if OFFLINE:
        notification.notify("Offline")
    else:
        button_click_sound.play()
        news_page_frame.widgets["progressbar"].place(x = 285, y= 235)
        win.update()
        win.after(100,actual_news_fetch)
        win.after(100,post_transition_sound.play)
        news_page_frame.widgets["FindNews"].configure(state = "disabled")
        win.after(2000,lambda: news_page_frame.widgets["FindNews"].configure(state = "normal"))
        win.after(100,lambda: news_page_frame.widgets["progressbar"].place_forget())

def actual_news_fetch():
    data = news_provider.parse_news()
    if news_page_frame.news_frame_widgets:
        for item in news_page_frame.news_frame_widgets.values():
            for widget in item.values():
                widget.destroy()
        news_page_frame.news_frame_widgets.clear()

    for i in range(4):
        key = f"news{i}"
        news = data[key]
        news_frame = ctk.CTkFrame(news_page_frame.frame,width = 650,height = 120,fg_color = "#2F3542")
        headline = ctk.CTkLabel(news_frame,text = news["headlines"],text_color = TEXT_COLOR1,
                                font = ("Segoe UI",15,"bold"),wraplength= 550)
        summary = ctk.CTkLabel(news_frame,text = news["main_story"],text_color= TEXT_COLOR2,
                               font = ("Arial",15),wraplength = 600,justify = "left")
        view_button = ctk.CTkButton(news_frame,text = "View More",text_color= TEXT_COLOR2,font = ("Arial",15,"bold"),fg_color= BG_COLOR,
                                command = lambda url = news["news_url"]: webbrowser.open(url))
        
        id = f"news"+ key
        news_page_frame.news_frame_widgets[id] = {}
        news_page_frame.news_frame_widgets[id]["frame"] =  news_frame
        news_page_frame.news_frame_widgets[id]["summary"] =  summary
        news_page_frame.news_frame_widgets[id]["btn"] =  view_button
        rel_y = 0.32 + i * 0.169
        
        news_frame.place(relx = 0.05,rely = rel_y,relwidth = 0.9,relheight = 0.2)
        news_frame.pack_propagate(False)
        headline.pack()
        summary.pack()
        view_button.place(relx = 0.8,rely = 0.7)



def clear_finance_widgets():

    for widgets in finance_page_frame.stock_details_widgets:
        finance_page_frame.stock_details_widgets[widgets].grid_forget()

    for widgets in finance_page_frame.news_widgets:
            finance_page_frame.news_widgets[widgets].place_forget()
    finance_page_frame.news_widgets["title2"].place(relx = 0.035,rely = 0.05)

def update_stocks():
    stock_list = stock_provider.stocks
    details = stock_provider.provide_details()
    frame = finance_page_frame.stock_frame
    widgets = finance_page_frame.stock_details_widgets


    for stock in stock_list:
        index = stock_list.index(stock)
        stock_price = details[stock]["stock_price"]
        change = details[stock]["change"]
        percent_change = details[stock]["percent_change"]
        change_color = None
        per_change_color = None

        if index <= 3:
            stock_price = "$" + str(round(stock_price,2))
        elif index >= 4:
            stock_price = "₹" + str(round(stock_price,2))
        change = str(round(change,2))
        percent_change = str(round(percent_change,2))

        if float(change) >= 0:
            change = "+" + change
            change_color = GAIN_COLOR
        else:
            change_color = LOSS_COLOR

        if float(percent_change) >= 0:
            percent_change = "+" + percent_change + "%"
            per_change_color = GAIN_COLOR
        else:
            percent_change = percent_change + "%"
            per_change_color = LOSS_COLOR

        widgets["stock_price_gui"] = ctk.CTkLabel(frame,text = stock_price,text_color=TEXT_COLOR1,font = ("Arial",20),
                                       anchor = "w",width = 50)
        widgets["change_gui"] = ctk.CTkLabel(frame,text = change,text_color=TEXT_COLOR1,font = ("Arial",20),anchor = "w",width = 50,
                                             fg_color = change_color)
        widgets["per_change_gui"] = ctk.CTkLabel(frame,text= percent_change, text_color = TEXT_COLOR1,font = ("Arial",20),anchor = "w",width = 50,
                                                 fg_color = per_change_color)


        widgets["stock_price_gui"].grid(row = index+1,column = 1)
        widgets["change_gui"].grid(row = index+1,column = 2)
        widgets["per_change_gui"].grid(row = index+1,column = 3)

def update_news():

    news_dict = finance_news_provider.find_details()
    frame = finance_page_frame.news_frame
    count = 1
    for news in news_dict:
        headline = news_dict[news]["headline"]
        news_url = news_dict[news]["url"]
        headline_label = ctk.CTkLabel(frame,text = headline,text_color=TEXT_COLOR2,font = ("Segoe UI",17),wraplength= 600)
        url_btn = ctk.CTkButton(frame,text = "Read full article",text_color = BUTTON_HOVER_COLOR,font = ("Calibri",20,"bold")
                               ,command = lambda url = news_url: webbrowser.open(url),fg_color = FRAME_COLOR)
        y = 0.14 + count * 0.2
        headline_label.place(relx = 0.0345,rely = y)
        url_btn.place(relx = 0.78,rely = y + 0.065)
        count += 1


def update_finance():
    if OFFLINE:
        notification.notify("Offline")
    else:
        button_click_sound.play()
        clear_finance_widgets()
        finance_page_frame.widgets["progressbar"].place(x = 290,y = 160)
        win.update()
        win.after(100,update_details)
        win.after(1000,post_transition_sound.play)
        finance_page_frame.widgets["refresh_btn"].configure(state = "disabled")
        win.after(2000,lambda: finance_page_frame.widgets["refresh_btn"].configure(state = "normal"))
        win.after(100,func = lambda:finance_page_frame.widgets["progressbar"].place_forget())

def update_details():
    update_stocks()
    update_news()




#binding commands
home_page_frame.widgets["Confirmbutton"].configure(command = switch_frame)
home_page_frame.widgets["aboutbutton"].configure(command = show_notification)
weather_page_frame.widgets["search_button"].configure(command = update_weather)
news_page_frame.widgets["FindNews"].configure(command = show_news)
finance_page_frame.widgets["refresh_btn"].configure(command = update_finance)
weather_page_frame.back_button.configure(command = lambda: frame_selector.set_frame("Home"))
news_page_frame.back_button.configure(command = lambda: frame_selector.set_frame("Home"))
finance_page_frame.back_button.configure(command = lambda: frame_selector.set_frame("Home"))
win.bind("<space>",lambda e: home_page_frame.change_text())


win.geometry(geometry)
win.mainloop()

