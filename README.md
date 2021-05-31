# ipl-winner-prediction-ml-python

This is the ipl winner prediction which is made using machine learnig and the algorithm used here is RandomForestClassifier with the accuracy of 88 %.
The user can pass 5 parameters such as team 1 , team 2 , venue , city , toss won and toss decision on the basis of these parameter the model predict the winner.


----INSTALL THESE BEFORE RUNNING THE PROJECT----

import numpy as np    
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

RUN project1.py TO EXECUTE AND CAN BE EXECUTE USING main.py

HERE main.py uses pre-trained saved model using pickle (project1.pkl)

FOR ANY ERROR WITH main.py FIRST EXECUTE project1.py
