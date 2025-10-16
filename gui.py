import tkinter as tk
from tkinter import font 
import customtkinter as ctk
from PIL import Image
import datetime
import random as rd
import pygame as pg
import os

pg.mixer.init()
click_sound = pg.mixer.Sound(os.path.join("icons","keyboard-typing-one-short-1-292590.mp3"))
frame_switch_sound = pg.mixer.Sound(os.path.join("icons","soft-transition-338894_ziSUAWbT.mp3"))




#colors
BG_COLOR = "#1E2A36"
TEXT_COLOR1 = "#FFFFFF"
TEXT_COLOR2 = '#C7D2DC'
BUTTON_COLOR = "#64FFDA"
FRAME_COLOR = "#26333F"
WEATHER_FRAME_COLOR = "#2A3D4F"
NEWS_FRAME_COLOR = "#383C35"
FINANCE_FRAME_COLOR = "#2B3F36"

BUTTON_HOVER_COLOR = "#394B59"
DROPDOWN_HOVER_COLOR = "#2F3D4A"
CONFIRM_BTN_HOVER = "#34495E"


#icons
icon_url = os.path.join("icons","icon-removebg-preview.png")
info_url = os.path.join("icons","info_icon-removebg-preview.png")
temperature_url = os.path.join("icons","temperature_icon-removebg-preview (1).png")
weather_url = os.path.join("icons","weather icon.png")
humidity_url = os.path.join("icons","OIP-removebg-preview.png")
wind_speed_url = os.path.join("icons","wind-speed-icon-5-removebg-preview.png")
sunrise_url = os.path.join("icons","sunrise.png")
sunset_url = os.path.join("icons","sunset.png")
moon_phase_url = os.path.join("icons","moon.png")
max_temp_url = os.path.join("icons","max_temp.png")
min_temp_url = os.path.join("icons","min_temp.png")
back_button_url = os.path.join("icons","back_icon-removebg-preview.png")
science_daily_url = os.path.join("icons","Science-Daily-logo-removebg-preview.png")
stock_line_url = os.path.join("icons","stock_line.png")
refresh_icon_url = os.path.join("icons","refresh icon.png")


title_icon = ctk.CTkImage(Image.open(icon_url),size=(64,64))
about_button_icon = ctk.CTkImage(Image.open(info_url),size =(32,32))
temperature_icon = ctk.CTkImage(Image.open(temperature_url),size =(32,32))
weather_icon = ctk.CTkImage(Image.open(weather_url),size = (32,32))
humidity_icon = ctk.CTkImage(Image.open(humidity_url),size = (32,32))
windspeed_icon = ctk.CTkImage(Image.open(wind_speed_url),size = (32,32))
sunrise_icon = ctk.CTkImage(Image.open(sunrise_url),size = (32,32))
sunset_icon = ctk.CTkImage(Image.open(sunset_url),size = (32,32))
moonphase_icon = ctk.CTkImage(Image.open(moon_phase_url),size = (32,32))
max_temp_icon = ctk.CTkImage(Image.open(max_temp_url),size = (32,32))
min_temp_icon = ctk.CTkImage(Image.open(min_temp_url),size = (32,32))
back_button_icon = ctk.CTkImage(Image.open(back_button_url),size = (64,64))
science_daily_icon = ctk.CTkImage(Image.open(science_daily_url),size = (128,128))
stock_line_icon = ctk.CTkImage(Image.open(stock_line_url),size = (64,64))
refresh_icon = ctk.CTkImage(Image.open(refresh_icon_url),size = (50,50))

current_time = datetime.date.today()


class Frame:

    def __init__(self):
        self.widgets = None

    @classmethod
    def set_window(cls,win):
        cls.win = win
    
        
    

class Home_Page(Frame):

    def __init__(self,optionvar,values):
        super().__init__()
        
        self.frame_type = "Home"
        self.frame = ctk.CTkFrame(self.win,width = 700,height = 750,fg_color=FRAME_COLOR)
        self.option_variable = optionvar
        self.values = values
        self.label_text = ""
        self.title = "InfoLens"
        self.count = 0
        
        self.widgets = {

            "Title" : ctk.CTkLabel(self.frame,text = "",font = ("Calibri",100),text_color=TEXT_COLOR1,image = title_icon,compound = "left"),
            "Quote" : ctk.CTkLabel(self.frame,text = "Your daily dose of news, weather and finance; In just a click!",
                           font = ("Arial",25),text_color = TEXT_COLOR2),
            "text2": ctk.CTkLabel(self.frame,text = "Genre: ",font = ("Arial",40),text_color= TEXT_COLOR1),
            "Dropdown" : tk.OptionMenu(self.frame,self.option_variable,*values),
            "Confirmbutton" : ctk.CTkButton(self.frame,text = "Confirm",font = ("Calibri",40),text_color= TEXT_COLOR2, fg_color = BG_COLOR,
                                    hover_color=CONFIRM_BTN_HOVER,border_color="#70A1FF",border_width= 2) ,
            "currentdate"  : ctk.CTkLabel(self.frame,text = f"Today's date: {current_time}",font = ("Arial" ,25), text_color = TEXT_COLOR2) ,
            "aboutbutton" : ctk.CTkButton(self.frame, text = "About",font = ("Calibri",25),text_color = TEXT_COLOR1,fg_color = BG_COLOR
                                  ,image = about_button_icon,compound="right",hover_color = BUTTON_HOVER_COLOR,border_color="#70A1FF",
                                  border_width= 2),
            "creditslabel" : ctk.CTkLabel(self.frame,text = "Created with ♡ by - Code: Garvit | Docs:  Vivek",font = ("Fira Code",20),
                                          text_color = "#7D5FFF")

            }
        
       
    def place_widgets(self):
        self.widgets["Title"].place(relx = 0.25,rely = 0.04)
        self.widgets["Quote"].place(relx = 0.1,rely = 0.25)
        self.widgets["text2"].place(relx = 0.142, rely= 0.4)
        self.widgets["Dropdown"].place(relx = 0.35,rely = 0.4)
        self.widgets["Dropdown"].config(bg = BG_COLOR,font = "Arial 30",fg = TEXT_COLOR1,width = 20
                                       ,highlightthickness = 0)
        self.widgets["Dropdown"]["menu"].config(font = "Arial 20",bg = BG_COLOR,fg = TEXT_COLOR2,)
        self.widgets["Confirmbutton"].place(relx = 0.42,rely = 0.6)
        self.widgets["currentdate"].place(relx = 0.32,rely = 0.521)
        self.widgets["aboutbutton"].place(relx = 0.087,rely = 0.75)
        self.widgets["creditslabel"].place(relx = 0.087,rely = 0.94)
        
    
    def remove_cursor(self):

        self.label_text = self.label_text.replace("|","")
        self.widgets["Title"].configure(text = self.label_text)
    

    def change_text(self):
    
        if self.count <= len(self.title)-1:
            self.label_text = self.label_text.replace("|","")
            self.widgets["Title"].configure(text= self.label_text)
            click_sound.play()
            self.label_text += self.title[self.count] + "|"
            self.widgets["Title"].configure(text = self.label_text)
            delay = rd.randint(180,240)
            self.win.after(delay,self.change_text)
            self.count += 1

        else:
            self.widgets["Title"].configure()
            self.win.after(500,self.remove_cursor)
            return


class Weather_Frame(Frame):

    def __init__(self):
        super().__init__()
  
        self.frame = ctk.CTkFrame(self.win,width = 700,height = 750,fg_color=WEATHER_FRAME_COLOR)
        self.frame_type = "Weather"
        self.optionvar = tk.StringVar(self.frame,value = "Haldwani")
        self.back_button =  ctk.CTkButton(self.win,image = back_button_icon,fg_color = BUTTON_COLOR,width = 10,height = 10,text = "")
           
        self.generalframe =  ctk.CTkFrame(self.frame,width = 220,height = 300,fg_color= "#22313F")
        self.astrologyframe = ctk.CTkFrame(self.frame,width = 220,height = 300,fg_color = "#22313F")
        self.forecastframe = ctk.CTkFrame(self.frame,width = 220,height = 300,fg_color = "#22313F")
        self.widgets = {
            
            "label" : ctk.CTkLabel(self.frame,text = "SkyCast",font = ("Bahnschrift",75,"bold"),text_color = TEXT_COLOR1),
            "quote" : ctk.CTkLabel(self.frame,text = "Powered by wttr.in", font = ("Arial",20),text_color= TEXT_COLOR2),
            "progressbar" : ctk.CTkLabel(self.frame,text = "LOADING...",font = ("Arial",25,"bold"),text_color = "#00FFEE"),
            "entryfield" : ctk.CTkEntry(self.frame,font = ("Arial",25,"bold"),text_color= TEXT_COLOR2,width = 325,fg_color = "#235F42"),
            "text2" : ctk.CTkLabel(self.frame,text = "Enter Place: ",text_color = TEXT_COLOR2,font = ("Bahnscrift",27)),
            "search_button" : ctk.CTkButton(self.frame,text = "Search",text_color= TEXT_COLOR1,font = ("Calibri",20)),
            "generalframe" : self.generalframe,
            "astrologyframe":self.astrologyframe,
            "forecastframe":self.forecastframe,
            "general_text" : ctk.CTkLabel(self.generalframe,text = "General",font = ("Bahnschrift",30),text_color=TEXT_COLOR1),
            "astrology_text" : ctk.CTkLabel(self.astrologyframe,text = "Astrology",font = ("Bahnschrift",30),text_color=TEXT_COLOR1),
            "forecast_text" : ctk.CTkLabel(self.forecastframe,text = "Forecast",font = ("Bahnschrift",30),text_color=TEXT_COLOR1),
            "temperature" : ctk.CTkLabel(self.generalframe,text = "Temperature: ",text_color= TEXT_COLOR2,image = temperature_icon,
                                         font = ("Segoe UI",17),compound="left"),
            "temperature" : ctk.CTkLabel(self.generalframe,text = "Temperature: ",text_color= TEXT_COLOR2,image = temperature_icon,
                                         font = ("Segoe UI",17),compound="left"),
            "weatherdesc" : ctk.CTkLabel(self.generalframe,text = "Condition: ",text_color= TEXT_COLOR2,image = weather_icon,
                                         font = ("Segoe UI",17),compound="left"),
            "humidity" : ctk.CTkLabel(self.generalframe,text = "Humidity: ",text_color= TEXT_COLOR2,image = humidity_icon,
                                         font = ("Segoe UI",17),compound="left"),
            "wind_speed" : ctk.CTkLabel(self.generalframe,text = "Wind Speed: ",text_color= TEXT_COLOR2,image = windspeed_icon,
                                         font = ("Segoe UI",17),compound="left"),
            "sunrise" : ctk.CTkLabel(self.astrologyframe,text = "Sunrise: ",text_color= TEXT_COLOR2,image = sunrise_icon,
                                         font = ("Segoe UI",17),compound="left"),
            "sunset" : ctk.CTkLabel(self.astrologyframe,text = "Sunset ",text_color= TEXT_COLOR2,image = sunset_icon,
                                         font = ("Segoe UI",17),compound="left"),
            "moonphase" : ctk.CTkLabel(self.astrologyframe,text = "Moon Phase ",text_color= TEXT_COLOR2,image = moonphase_icon,
                                         font = ("Segoe UI",17),compound="left",wraplength=160),
            "max_temp" : ctk.CTkLabel(self.forecastframe,text = "Max Temp: ",text_color= TEXT_COLOR2,image = max_temp_icon,
                                         font = ("Segoe UI",17),compound="left"),
            "min_temp" : ctk.CTkLabel(self.forecastframe,text = "Min Temp: ",text_color= TEXT_COLOR2,image = min_temp_icon,
                                         font = ("Segoe UI",17),compound="left"),
           
        }

    def place_widgets(self):
        
        self.widgets["label"].place(relx = 0.29,rely = 0.04)
        self.widgets["quote"].place(relx = 0.35,rely = 0.185)
        self.widgets["generalframe"].place(relx = 0.05,rely = 0.41)
        self.widgets["generalframe"].pack_propagate(False)
        self.widgets["text2"].place(relx = 0.15,rely = 0.25)
        self.widgets["entryfield"].place(relx = 0.4,rely = 0.25)
        
        self.widgets["search_button"].place(relx = 0.64,rely = 0.31)

        self.widgets["astrologyframe"].place(relx = 0.365,rely = 0.41)
        self.widgets["astrologyframe"].pack_propagate(False)

        self.widgets["forecastframe"].place(relx = 0.675,rely = 0.41)
        self.widgets["forecastframe"].pack_propagate(False)

        self.widgets["general_text"].place(relx = 0.2,rely = 0.03)
        self.widgets["astrology_text"].place(relx = 0.2,rely = 0.03)
        self.widgets["forecast_text"].place(relx = 0.2,rely = 0.03)
        self.widgets["temperature"].place(relx = 0.1,rely = 0.17)
        self.widgets["weatherdesc"].place(relx = 0.1,rely = 0.35)
        self.widgets["humidity"].place(relx = 0.1,rely = 0.5)
        self.widgets["wind_speed"].place(relx = 0.1,rely = 0.69)
    
        self.widgets["sunrise"].place(relx = 0.1,rely = 0.17)
        self.widgets["sunset"].place(relx = 0.1,rely = 0.35)
        self.widgets["moonphase"].place(relx = 0.1,rely = 0.5)

        self.widgets["max_temp"].place(relx = 0.1,rely = 0.17)
        self.widgets["min_temp"].place(relx = 0.1,rely = 0.35)
        self.back_button.place(relx = 0.755,rely = 0.810)


class News_Page_Frame(Frame):

    def __init__(self):
        super().__init__()
        self.frame = ctk.CTkFrame(self.win,width = 700,height = 750,fg_color=NEWS_FRAME_COLOR)
        self.back_button =  ctk.CTkButton(self.win,image = back_button_icon,fg_color = BUTTON_COLOR,width = 10,height = 10,text = "")
        self.frame_type = "News"
        self.widgets = {

                "Title" :  ctk.CTkLabel(self.frame,text ="LabLine", font = ("Bahnschrift",75,"bold"),text_color = TEXT_COLOR1,
                                        image = science_daily_icon,compound = "left"),
                "quote" : ctk.CTkLabel(self.frame,text = "Your daily dose of discovery.", font = ("Arial",22),text_color = TEXT_COLOR2),
                "FindNews" : ctk.CTkButton(self.frame,text = "Find", font = ("Calibri",25),text_color = TEXT_COLOR1,fg_color = BG_COLOR),
                "progressbar":ctk.CTkLabel(self.frame,text = "LOADING.....",font = ("Arial",25,"bold"),text_color = "#00FFEE"),
                "news_frame": ctk.CTkFrame(self.frame,fg_color = "#2F3542")
                        
                    }
        
        self.news_frame_widgets = {}

    def place_widgets(self):

        self.widgets["Title"].place(relx = 0.21,rely = 0.02)
        self.widgets["quote"].place(relx = 0.32,rely = 0.20)
        self.widgets["FindNews"].place(relx = 0.4,rely = 0.27)
        self.back_button.place(relx = 0.755,rely = 0.810)

        

class Finance_Page_Frame(Frame):

    def __init__(self):
        super().__init__()
        self.frame_type = "Finance"
        SUBFRAME_COLOR = "#1E2C24"
        self.frame = ctk.CTkFrame(self.win,width = 700,height = 750,fg_color=FINANCE_FRAME_COLOR)
        self.stock_frame = ctk.CTkFrame(self.frame,width = 600,height = 300,fg_color = SUBFRAME_COLOR)
        self.news_frame = ctk.CTkFrame(self.frame,width = 650,height = 350,fg_color = SUBFRAME_COLOR)
        self.back_button =  ctk.CTkButton(self.win,image = back_button_icon,fg_color = BUTTON_COLOR,width = 10,height = 10,text = "")
        self.widgets = {

            "Title" : ctk.CTkLabel(self.frame,text = "MarketLens",font = ("Bahnschrift",75,"bold"),text_color = TEXT_COLOR1),
            "tagline" : ctk.CTkLabel(self.frame,text = "Track prices. See patterns. Stay informed.",
                                     font = ("Arial",25),text_color = TEXT_COLOR2),
            "refresh_btn" : ctk.CTkButton(self.frame,fg_color = None,hover=BUTTON_HOVER_COLOR,text = "",
                                          image = refresh_icon,corner_radius=20,width = 10,height = 10),
            "progressbar" : ctk.CTkLabel(self.frame,text = "LOADING...",text_color = "#00FFEE",font = ("Arial",20,"bold"))
    
        }        
        self.stock_labels = { "stock_name": ctk.CTkLabel(self.stock_frame,text = "Stock Name",text_color = TEXT_COLOR2,
                                                         font = ("Arial",20,"bold")),
                                "price": ctk.CTkLabel(self.stock_frame,text = "Price",text_color = TEXT_COLOR2,
                                                         font = ("Arial",20,"bold")),
                                "change": ctk.CTkLabel(self.stock_frame,text = "Change",text_color = TEXT_COLOR2,
                                                         font = ("Arial",20,"bold")),
                                "per_change": ctk.CTkLabel(self.stock_frame,text = "%Change",text_color = TEXT_COLOR2,
                                                         font = ("Arial",20,"bold")),
        }

        self.stock_names = ["Apple","Amazon","Microsoft","Tesla","ICICI Bank","SBI Bank"]

        self.stock_details_widgets = {}

        self.news_widgets = { "title2" : ctk.CTkLabel(self.news_frame,text = "Finance Highlights",text_color= TEXT_COLOR1,
                                    font = ("Bahnschrift",40),image = stock_line_icon,compound="left")

        }
        
    
    def place_widgets(self):
        
        self.widgets["Title"].place(relx = 0.21,rely = 0.02)
        self.widgets["tagline"].place(relx = 0.17,rely = 0.18)
        self.stock_frame.place(relx = 0.15,rely = 0.25)
        self.widgets["refresh_btn"].place(relx = 0.84,rely =0.47)
        self.news_frame.place(relx = 0.07,rely = 0.56)
        self.news_widgets["title2"].place(relx = 0.035,rely = 0.05)
        self.back_button.place(relx = 0.755,rely = 0.810)


        count = 0
        for item in self.stock_labels:
            self.stock_labels[item].grid(row = 0,column = count,padx = 25,pady = 5)
            count+= 1
        
        for name in self.stock_names:
            index = self.stock_names.index(name)
            label = ctk.CTkLabel(self.stock_frame,text = name,text_color = TEXT_COLOR1,font = ("Arial",20),anchor = "w",width = 100,pady = 5)
            label.grid(row = index+1,column = 0)
        
    


class Frame_Switcher:
  
    def __init__(self):
        pass
    
    @classmethod
    def set_frame_list(cls,list):
        cls.frame_list = list
        cls.current_frame = cls.frame_list[0]

  
    def set_frame(self,frame_name):
        self.current_frame.frame.place_forget()
        frame_switch_sound.play()

        if frame_name == "Home" and self.current_frame.frame_type != "Home":
            #changing from a different frame
            self.current_frame.back_button.place_forget()

        for item in self.frame_list:
            if item.frame_type == frame_name:
                item.place_widgets()
                item.frame.place(relx = 0.5,rely = 0.03,relwidth = 0.5,relheight = 0.865,anchor = "n")
                self.current_frame = item


class Notification(Frame):

    def __init__(self):
        super().__init__()
        self.offline_icon = r"icons\icons8-offline-100.png"
        self.WIN_COLOR = "#008080"
        self.TEXT_COLOR = "#FFFFFF"
        self.offline_img = ctk.CTkImage(Image.open(self.offline_icon),size = (128,128))

    def notify(self,mode):

        if mode == "Offline":
            prompt_win = tk.Toplevel(bg = self.WIN_COLOR)
            x_coords = self.win.winfo_screenwidth()//2 - 400//2
            y_coords = self.win.winfo_screenheight()//2 - 300//2
            prompt_win.geometry(f"400x300+{x_coords+100}+{y_coords}")
            message_label = ctk.CTkLabel(prompt_win,text = "You're Offline",text_color = self.TEXT_COLOR,image= self.offline_img,
                                         compound = "top",font = ("Segoe UI",30,"bold"))
            secondary_label = ctk.CTkLabel(prompt_win,text = "Please check your internet connection",text_color = TEXT_COLOR2,
                                            font = ("Banhschrift",20),wraplength= 270)
            message_label.pack()
            secondary_label.pack()
            self.win.after(5000,prompt_win.destroy)
