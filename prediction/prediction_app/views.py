from django.shortcuts import render
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from django.conf import settings
import os

def home(request):
    return render(request,'home.html')

def predict(request):
    return render(request,'predict.html')

def result(request):
    ## csv_file_path = os.path.join(settings.BASE_DIR, 'prediction', 'diabetes.csv')
    csv_file_path = os.path.join(settings.BASE_DIR, 'diabetes.csv')

    data = pd.read_csv(csv_file_path)
    x = data.drop('Outcome',axis=1)
    y  = data['Outcome']

    x_train , x_test, y_train,y_test = train_test_split(x,y,test_size=0.2)
    model = LogisticRegression()
    model.fit(x_train,y_train)
    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6']) 
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    
    result1 = ""
    pred = model.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])
    if pred==[1]:
        result1= "Positive"
    else:
        result1 = "Negative"
    
    return render (request,'predict.html',{"result2":result1})

