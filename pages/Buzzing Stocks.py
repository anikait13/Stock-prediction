import pandas as pd
import requests
import spacy
import streamlit as st
import sentiment

from bs4 import BeautifulSoup
import yfinance as yf

st.title('Buzzing Stocks :zap:')


## get data from RSS feed
def extract_text_from_rss(rss_link):
    """
    Parses the XML and extracts the headings from the
    links in a python list.

    """
    headings = []
    r1 = requests.get('https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms')
    r2 = requests.get(rss_link)
    soup1 = BeautifulSoup(r1.content, features='lxml')
    soup2 = BeautifulSoup(r2.content, features='lxml')
    headings1 = soup1.findAll('title')
    headings2 = (soup2.findAll('title'))
    print(headings2)
    headings = headings1 + headings2
    return headings


stock_info_dict = {
    'Org': [],
    'Symbol': [],
    'Sentiment': [],
    'currentPrice': [],
    'dayHigh': [],
    'dayLow': [],
    'forwardPE': [],
    'dividendYield': []
}
nlp = spacy.load("en_core_web_sm")


def find_sentiement(heading):
    sentiment.sentiment_scores(heading)

def stock_info(headings):
    """
    Goes over each heading to find out the entities
    and link it with the nifty 50 companies data.
    Extracts the data
    """

    stocks_df = pd.read_csv("./data/ind_nifty50list.csv")
    for title in headings:
        doc = nlp(title.text)
        stock_sentiment = find_sentiement(title)
        for token in doc.ents:
            try:
                if stocks_df['Company Name'].str.contains(token.text).sum():
                    symbol = stocks_df[stocks_df['Company Name']. \
                        str.contains(token.text)]['Symbol'].values[0]
                    print(symbol)

                    org_name = stocks_df[stocks_df['Company Name']. \
                        str.contains(token.text)]['Company Name'].values[0]

                    stock_info_dict['Org'].append(org_name)
                    stock_info_dict['Symbol'].append(symbol)
                    stock_info_dict['Sentiment'].append(stock_sentiment)

                    stock_info = yf.Ticker(symbol + ".NS").info

                    stock_info_dict['currentPrice'].append(stock_info['currentPrice'])
                    stock_info_dict['dayHigh'].append(stock_info['dayHigh'])
                    stock_info_dict['dayLow'].append(stock_info['dayLow'])
                    stock_info_dict['forwardPE'].append(stock_info['forwardPE'])
                    stock_info_dict['dividendYield'].append(stock_info['dividendYield'])
                else:
                    pass
            except:
                pass
    output_df = pd.DataFrame(stock_info_dict)
    return output_df


## add an input field to pass the RSS link
user_input = st.text_input("Add your RSS link here!", "https://www.moneycontrol.com/rss/buzzingstocks.xml")

## get the financial  headings
fin_headings = extract_text_from_rss(user_input)

## output the financial info through a dataframe
output_df = stock_info(fin_headings)
output_df.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)
st.dataframe(output_df)

## display the news in an expander section
with st.expander("Expand for Financial News!"):
    for h in fin_headings:
        st.markdown("* " + h.text)
