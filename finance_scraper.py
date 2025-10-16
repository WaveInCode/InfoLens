import requests
import bs4
import yfinance as yf


NEWS_URL = "https://economictimes.indiatimes.com/news/latest-news"

class Finance_News_Finder:

    def __init__(self):
        self.finance_news_dictionary = {}
        self.keywords = ["stocks","shares","market","tax","business","economy","sensex","nifty50","budget","finance","inflation",
                         "investment","IPO","currency","crypto","index","equity","dollar","rupee","mutual fund","IPO","dividend"]

    def find_details(self):
        response = requests.get(NEWS_URL)
        self.soup = bs4.BeautifulSoup(response.content,"html.parser")
        ul_tag= self.soup.find("ul",class_ = "data")    
        li_tags = ul_tag.find_all("li")
        count = 1

        for news in li_tags:

            if count >= 4:
                break    
            
            news_id = "news" + str(count)
            a_tag = news.find("a")
            headline = a_tag.get_text()

            for keyword in self.keywords:
                if keyword in headline.lower():
                    self.finance_news_dictionary[news_id] = {}
                    self.finance_news_dictionary[news_id]['headline'] = headline
                    self.finance_news_dictionary[news_id]['url'] = a_tag["href"]
                    count+= 1
                else:
                    continue

        return self.finance_news_dictionary

class Stock_Detail_Fetcher:

    def __init__(self):
        self.stocks = ["AAPL","AMZN","MSFT","TSLA","ICICIBANK.NS","SBIN.NS"]
        self.stock_details = {}
    
    def provide_details(self):
        for stock in self.stocks:
            data = yf.Ticker(stock)
            latest_details = data.history(period = "1d",interval = "1m",prepost = True)
            curr_closing_price = latest_details["Close"].iloc[-1]
            prev_closing_price = latest_details["Close"].iloc[-2]

            change = curr_closing_price - prev_closing_price
            percent_change = change/prev_closing_price * 100
            

            self.stock_details[stock] = {}
            self.stock_details[stock]['stock_price'] = float(curr_closing_price)
            self.stock_details[stock]['change'] = float(change)
            self.stock_details[stock]['percent_change'] = float(percent_change)

        return self.stock_details


