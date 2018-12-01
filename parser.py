# import pandas as pd
import json
# from sklearn.model_selection import train_test_split

# data = pd.read_json('C:/Users/Shashank/Desktop/UTArlington/Sem1/Data Mining/Assignment 3/movie.json')
# # print(data)
# train, test = train_test_split(data, train_size=0.8 ,test_size=0.2)
# print(type(train))

with open('C:/Users/Shashank/Desktop/UTArlington/Sem1/Data Mining/Assignment 3/movie.json', 'r') as f:
    data = json.load(f)

movie_data = []
for movie in data:
	obj = {}
	obj['asin'] = movie['asin']
	obj['overall'] = movie['overall']
	obj['reviewerID'] = movie['reviewerID']
	movie_data.append(obj)

with open('C:/Users/Shashank/Desktop/UTArlington/Sem1/Data Mining/Assignment 3/movie_data.json', 'w') as f:
    json.dump(movie_data, f)