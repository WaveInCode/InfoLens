import requests
import bs4
import random

BASE_URL = "https://www.sciencedaily.com/"

class News_Fetcher:
   

    def __init__(self):
        self.BASE_URL = BASE_URL
        self.divs = None
        self.fetched = False
        
    def fetch_news(self):
        
        if not self.fetched:
            self.http = requests.get(self.BASE_URL)
            self.soup = bs4.BeautifulSoup(self.http.content,"html.parser")
            self.divs = self.soup.find_all("div",class_ = "col-md-6")
            self.fetched = True
            return self.divs
        
        elif self.fetched:
            return self.divs
             

        

news_finder = News_Fetcher()    

class News_Detail_Fetcher:

    def __init__(self,news):
        self.news = news
        a_tag = news.find("div",class_ = "latest-head").find("a")
        self.headline = a_tag.get_text()
        self.news_url = BASE_URL + a_tag["href"]
        self.main_story = find_main_story(self.news_url)

def find_main_story(news_url):
        response = requests.get(news_url)
        soup2 = bs4.BeautifulSoup(response.content,"html.parser")
        main_article = soup2.find("div",class_ = "hyphenate underline")
        main_text = main_article.find("p").get_text(strip = True)
        MAX_LINES = 2
        #removing excess lines

        count = 0
        main_story  = ""
        lines = main_text.split(".")
        for line in lines:
            if count < MAX_LINES:
                main_story += line + "."
                count += 1

 
        return main_story
        

 
class General_News_Provider:

    def __init__(self):
        self.news_dictionary = {}
        self.count = 0
        self.index_count = 0
        self.news_indexes = []
    
    def generate_news_indexes(self,mode = None):
        limit = 4
        if not mode == "add":
             return
        
        for i in range(limit):
                rand_num = random.sample([i for i in range(11)],4)
                self.news_indexes.append(rand_num)
               

    def parse_news(self):
        MAX_NEWS_LIMIT = 4
        self.divs = news_finder.fetch_news()
        if self.divs == None:
            return
        
        self.generate_news_indexes(mode = "add")

        for news in self.divs:
            if not self.count >= MAX_NEWS_LIMIT:
                self.index_count = self.news_indexes[self.count][0]
                news_item = self.divs[self.index_count]
                news_details = News_Detail_Fetcher(news_item)
                news_id = "news" + str(self.count)
                self.news_dictionary[news_id] = {}
                self.news_dictionary[news_id]["headlines"] = news_details.headline
                self.news_dictionary[news_id]["news_url"] = news_details.news_url
                self.news_dictionary[news_id]["main_story"] = news_details.main_story
                self.count += 1

        self.news_indexes = []
        self.count = 0 
        return self.news_dictionary
        

