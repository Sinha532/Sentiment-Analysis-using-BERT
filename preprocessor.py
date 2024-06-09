import re
import pandas as pd
from googletrans import Translator
from transformers import pipeline

model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
sentiment_analysis = pipeline("sentiment-analysis", model=model_name, tokenizer=model_name)

def get_sentiment_score(message):
    sentiment = sentiment_analysis(message)[0]
    return sentiment['label'], sentiment['score']


def preprocess(data,max_lines=200):
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
    messages=re.split(pattern, data)[1:max_lines+1]
    dates=re.findall(pattern, data)[1:max_lines+1]
    df=pd.DataFrame({'user_message': messages, 'message_date': dates})
    df['message_date']=pd.to_datetime(df['message_date'], format="%m/%d/%y, %H:%M - ")
    df.rename(columns={'message_date':'date'},inplace=True)
    

    users=[]
    messages=[]
    for message in df['user_message']:
        entry=re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns = ['user_message'], inplace = True)
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df['sentiment'] = df['message'].apply(lambda x: get_sentiment_score(x)[0])

    sentiment_mapping = {
    '5 stars': 'Very positive statement',
    '4 stars': 'Positive statement',
    '3 stars': 'Neutral statement',
    '2 stars': 'Negative statement',
    '1 star': 'Very negative statement'
    }
    df['sentiment_label'] = df['sentiment'].map(sentiment_mapping)


    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour)+"-"+str('00'))
        elif hour == 0:
            period.append(str('00')+"-"+str(hour+1))
        else:
            period.append(str(hour)+"-"+str(hour+1))

    df['period'] = period

    return df
