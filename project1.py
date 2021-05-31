# -*- coding: utf-8 -*-
"""project1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/173QCYzIIZwEsxEQu1MJJkvlgRGc7WlX1
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

dataset = pd.read_csv("matches.csv")

dataset.info()

dataset.head()

dataset[dataset['winner'].isnull() == True]

dataset['winner'].fillna('Draw', inplace=True)

dataset[dataset['winner'].isnull() == True]

team_encodings = {'Mumbai Indians': 1, 'Kolkata Knight Riders': 2, 'Royal Challengers Bangalore': 3, 'Deccan Chargers': 4, 'Chennai Super Kings': 5, 'Rajasthan Royals': 6,
    'Delhi Daredevils': 7, 'Gujarat Lions': 8, 'Kings XI Punjab': 9, 'Sunrisers Hyderabad': 10, 'Rising Pune Supergiants': 11, 'Rising Pune Supergiant': 11, 'Kochi Tuskers Kerala':12,
    'Pune Warriors': 13,'Delhi Capitals': 14,'Draw': 15 }

team_encode_dict = {'team1': team_encodings, 'team2': team_encodings, 'toss_winner': team_encodings, 'winner': team_encodings }

dataset.replace(team_encode_dict, inplace=True)

dataset.info()

dataset['city'].value_counts()

dataset[dataset['city'].isnull() == True ]

dataset['city'].fillna('Dubai',inplace=True)

dataset = dataset[['id', 'team1','team2','city','toss_decision','toss_winner','venue','winner']]

dataset.head()

dataset.describe()

ftr_list = ['city', 'toss_decision', 'venue']

encoder = LabelEncoder()
for x in ftr_list:
    dataset[x] = encoder.fit_transform(dataset[x])
    print(encoder.classes_)

dataset

train_ds, test_ds = train_test_split(dataset, test_size=0.3, random_state=42)

print(train_ds.shape)
print(test_ds.shape)

model = RandomForestClassifier(n_estimators=100)
target = ['winner']
predictors = ['team1', 'team2', 'venue', 'toss_winner','city','toss_decision']
model.fit(dataset[predictors], dataset[target])
predictions = model.predict(dataset[predictors])
accuracy = accuracy_score(predictions,dataset[target])
print('Accuracy : %s' % '{0:.2%}'.format(accuracy))

import pickle

project1_model = "project1.pkl"
with open(project1_model, 'wb') as file:
    pickle.dump(model, file)

with open(project1_model, 'rb') as file:
    trained_model = pickle.load(file)


team1 = input('Enter team 1 : ')
team2 = input('Enter team 2 : ')
toss_winner=input('Toss Winner : ')
venue = ['ACA-VDCA Stadium' , 
         'Barabati Stadium' , 
         'Brabourne Stadium' , 
         'Buffalo Park' ,
         'De Beers Diamond Oval' , 
         'Dr DY Patil Sports Academy' ,
         'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium' ,
         'Dubai International Cricket Stadium' , 
         'Eden Gardens' , 'Feroz Shah Kotla' ,
         'Feroz Shah Kotla Ground' , 'Green Park' ,
         'Himachal Pradesh Cricket Association Stadium' , 
         'Holkar Cricket Stadium' ,'IS Bindra Stadium' , 'JSCA International Stadium Complex' , 
         'Kingsmead' , 'M Chinnaswamy Stadium' , 'M. A. Chidambaram Stadium' ,
         'M. Chinnaswamy Stadium' , 'MA Chidambaram Stadium, Chepauk',
         'Maharashtra Cricket Association Stadium' , 'Nehru Stadium' ,
         'New Wanderers Stadium' , 'Newlands' , 'OUTsurance Oval' ,
         'Punjab Cricket Association IS Bindra Stadium, Mohali' ,
         'Punjab Cricket Association Stadium, Mohali' ,
         'Rajiv Gandhi International Stadium, Uppal' ,
         'Rajiv Gandhi Intl. Cricket Stadium' , 'Sardar Patel Stadium, Motera',
         'Saurashtra Cricket Association Stadium' , 'Sawai Mansingh Stadium',
         'Shaheed Veer Narayan Singh International Stadium' ,
         'Sharjah Cricket Stadium' , 'Sheikh Zayed Stadium' , "St George's Park" ,
         'Subrata Roy Sahara Stadium' , 'SuperSport Park',
         'Vidarbha Cricket Association Stadium, Jamtha' , 'Wankhede Stadium']
print("------ VENUE LIST ------")
for x in range(len(venue)):
  print("   ",end=" ")
  print(x,end = " : ")
  print(venue[x],sep="\n")
match_venue = int(input('Enter venue number from above list : '))
print("------ CITY LIST ------")
city = ['Abu Dhabi','Ahmedabad','Bangalore','Bengaluru','Bloemfontein',
 'Cape Town','Centurion','Chandigarh','Chennai','Cuttack','Delhi',  
 'Dharamsala','Dubai','Durban','East London','Hyderabad','Indore','Jaipur',
 'Johannesburg','Kanpur','Kimberley','Kochi','Kolkata','Mohali','Mumbai',
 'Nagpur','Port Elizabeth','Pune','Raipur','Rajkot','Ranchi','Sharjah',
 'Visakhapatnam']
toss = ['bat','field']
for x in range(len(city)):
  print("   ",end=" ")
  print(x,end = " : ")
  print(city[x],sep="\n")
match_city = int(input('Enter city number from above list : '))
print(" ")
print("------ TOSS DECISION ------")
for x in range(len(toss)):
  print("   ",end=" ")
  print(x,end = " : ")
  print(toss[x],sep="\n")
toss_d = int(input('Enter toss decision from above list : '))
inp = [team_encode_dict['team1'][team1],team_encode_dict['team2'][team2],match_venue,team_encode_dict['toss_winner'][toss_winner],match_city,toss_d]
inp = np.array(inp).reshape((1, -1))
output=trained_model.predict(inp)
print(f"The winner would be: {list(team_encodings.keys())[list(team_encode_dict['team1'].values()).index(output)]}")