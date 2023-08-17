import pandas as pd
data = pd.read_csv("C:/Users/SPTINT-24/Desktop/data set mn/elon_musk_tweets.csv")
print (data)
print(data.head(5))
print(data.tail(10))
print (data.info())
print(data.dtypes)
print(data.count())
print(data["retweets"])


