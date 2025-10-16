import requests


class Weather_Details_Fetcher:

    def __init__(self,state_name,html):
        state_name = state_name.strip()
        response = html
        file_content = response.json()


        self.temp_c = file_content["current_condition"][0]['temp_C']
        self.weather_desc = file_content["current_condition"][0]["weatherDesc"][0]["value"]
        self.humidity = file_content["current_condition"][0]["humidity"]
        self.wind_speed = file_content["current_condition"][0]["windspeedKmph"]
        self.sunrise = file_content["weather"][0]["astronomy"][0]["sunrise"]
        self.sunset = file_content["weather"][0]["astronomy"][0]["sunset"]
        self.moon_phase = file_content["weather"][0]["astronomy"][0]["moon_phase"]
        self.max_temp = file_content["weather"][0]["maxtempC"]
        self.min_temp = file_content["weather"][0]["mintempC"]


class Weather_Details_Provider:

    def __init__(self):
        self.weather_details_dict = {}


    def provide_details(self,state_name,html):
        self.details = Weather_Details_Fetcher(state_name,html)

        self.weather_details_dict["temp_c"] =  self.details.temp_c
        self.weather_details_dict["weather_desc"] =  self.details.weather_desc
        self.weather_details_dict["humidity"] =  self.details.humidity
        self.weather_details_dict["wind_speed"] =  self.details.wind_speed
        self.weather_details_dict["sunrise"] =  self.details.sunrise
        self.weather_details_dict["sunset"] =  self.details.sunset
        self.weather_details_dict["moon_phase"] =  self.details.moon_phase
        self.weather_details_dict["max_temp"] = self.details.max_temp
        self.weather_details_dict["min_temp"] = self.details.min_temp

        return self.weather_details_dict
