
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

project1_model = "project1.pkl"

with open(project1.pkl, 'rb') as file:
    trained_model = pickle.load(file)



print("------ TEAM LIST ------")
team_selection = [
    '1 : Mumbai Indians','2 : Kolkata Knight Riders','3 : Royal Challengers Bangalore','4 : Deccan Chargers',
    '5 : Chennai Super Kings','6 : Rajasthan Royals','7 : Delhi Daredevils','8 : Gujarat Lions',
    '9 : Kings XI Punjab','10 : Sunrisers Hyderabad','11 : Rising Pune Supergiants','12 : Kochi Tuskers Kerala',
    '13 : Pune Warriors','14 : Delhi Capitals'
]
for x in range(len(team_selection)):
  print(team_selection[x])
team1 = int(input('Enter team 1 no. from above list : '))
team2 = int(input('Enter team 2 no. from above list : '))
toss_winner=int(input('Enter Toss Winner from above list : '))
venue = ['ACA-VDCA Stadium' , 'Barabati Stadium' , 'Brabourne Stadium' , 'Buffalo Park' ,'De Beers Diamond Oval' , 
         'Dr DY Patil Sports Academy' , 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium' , 'Dubai International Cricket Stadium' , 
         'Eden Gardens' , 'Feroz Shah Kotla' ,'Feroz Shah Kotla Ground' , 'Green Park' ,'Himachal Pradesh Cricket Association Stadium' , 'Holkar Cricket Stadium' ,'IS Bindra Stadium' , 'JSCA International Stadium Complex' , 
         'Kingsmead' , 'M Chinnaswamy Stadium' , 'M. A. Chidambaram Stadium' , 'M. Chinnaswamy Stadium' , 'MA Chidambaram Stadium, Chepauk', 'Maharashtra Cricket Association Stadium' , 'Nehru Stadium' ,
         'New Wanderers Stadium' , 'Newlands' , 'OUTsurance Oval' , 'Punjab Cricket Association IS Bindra Stadium, Mohali' ,
         'Punjab Cricket Association Stadium, Mohali' , 'Rajiv Gandhi International Stadium, Uppal' , 'Rajiv Gandhi Intl. Cricket Stadium' , 'Sardar Patel Stadium, Motera',
         'Saurashtra Cricket Association Stadium','Sawai Mansingh Stadium','Shaheed Veer Narayan Singh International Stadium','Sharjah Cricket Stadium','Sheikh Zayed Stadium', 
         "St George's Park" , 'Subrata Roy Sahara Stadium' , 'SuperSport Park', 'Vidarbha Cricket Association Stadium, Jamtha' , 'Wankhede Stadium']
print("------ VENUE LIST ------")
for x in range(len(venue)):
  print("   ",end=" ")
  print(x,end = " : ")
  print(venue[x],sep="\n")
match_venue = int(input('Enter venue number from above list : '))
print("------ CITY LIST ------")
city = ['Abu Dhabi','Ahmedabad','Bangalore','Bengaluru','Bloemfontein', 'Cape Town','Centurion','Chandigarh','Chennai','Cuttack','Delhi','Dharamsala','Dubai','Durban',
        'East London','Hyderabad','Indore','Jaipur', 'Johannesburg','Kanpur','Kimberley','Kochi','Kolkata','Mohali','Mumbai', 'Nagpur','Port Elizabeth','Pune','Raipur',
        'Rajkot','Ranchi','Sharjah','Visakhapatnam']
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
inp = [team1,team2,match_venue,toss_winner,match_city,toss_d]
inp = np.array(inp).reshape((1, -1))
output=trained_model.predict(inp)
team_encodings = {
    '1':'Mumbai Indians',
    '2':'Kolkata Knight Riders',
    '3':'Royal Challengers Bangalore',
    '4':'Deccan Chargers',
    '5':'Chennai Super Kings',    
    '6':'Rajasthan Royals',
    '7':'Delhi Daredevils',
    '8':'Gujarat Lions',
    '9':'Kings XI Punjab',
    '10':'Sunrisers Hyderabad',
    '11':'Rising Pune Supergiants',
    '12':'Kochi Tuskers Kerala',
    '13':'Pune Warriors',
    '14':'Delhi Capitals',
    '15':'Draw'
}
print("The winner would be : ",team_encodings.get(str(output[0])))