from django.shortcuts import render

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier

def home(request):
    return render(request,'home.html')

def predict(request):
    return render(request,'predict.html')

def result(request):
    data = pd.read_csv(r'C:\Users\ADMIN\Downloads\diabetes.csv')
    X=data.drop("Outcome", axis=1) 
    Y=data['Outcome']

    scaler = MinMaxScaler()
    X[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']] = scaler.fit_transform(X)
    x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size = 0.2, random_state = 32)
    
    model = RandomForestClassifier()
    model.fit(x_train,y_train)

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    prediction = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])  

    result1="" 
    if prediction==[0]:
        result1="Diabetic"
    else:
        result1="Not Diabetic" 

    return render(request,'result.html', {"result1":result1})