#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
@Author ---> Bibek Rawat
'''
from flask import Flask, request, render_template
import pickle
import pandas as pd
from datetime import datetime
app = Flask(__name__)
model = pd.read_csv('C:\\Users\\91994\\Downloads\\Housing.csv')
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/', methods=['POST'])
def predict():
    try:
        '''
        Required input for machine learning model
        1. tradeTime
        2. followers
        3. square
        4. livingRoom
        5. drawingRoom
        6. kitchen
        7. bathRoom
        8. constructionTime
        9. communityAverage
        10. renovationCondition
        11. buildingStructure
        12. elevator
        '''
        if query_tradetime < query_constructiontime:
            return render_template('index.html')
        if query_renovationcondition == "renovationCondition_1":
            renovationCondition_2 = 0
            renovationCondition_3 = 0
            renovationCondition_4 = 0
        elif query_renovationcondition == "renovationCondition_2":
            renovationCondition_2 = 1
            renovationCondition_3 = 0
            renovationCondition_4 = 0
        elif query_renovationcondition == "renovationCondition_3":
            renovationCondition_2 = 0
            renovationCondition_3 = 1
            renovationCondition_4 = 0
        else:
            renovationCondition_2 = 0
            renovationCondition_3 = 0
            renovationCondition_4 = 1
        if query_buildingstructure == "buildingStructure_1":
            buildingStructure_2 = 0
            buildingStructure_3 = 0
            buildingStructure_4 = 0
            buildingStructure_5 = 0
            buildingStructure_6 = 0
        elif query_buildingstructure == "buildingStructure_2":
            buildingStructure_2 = 1
            buildingStructure_3 = 0
            buildingStructure_4 = 0
            buildingStructure_5 = 0
            buildingStructure_6 = 0
        elif query_buildingstructure == "buildingStructure_3":
            buildingStructure_2 = 0
            buildingStructure_3 = 1
            buildingStructure_4 = 0
            buildingStructure_5 = 0
            buildingStructure_6 = 0
        elif query_buildingstructure == "buildingStructure_4":
            buildingStructure_2 = 0
            buildingStructure_3 = 0
            buildingStructure_4 = 1
            buildingStructure_5 = 0
            buildingStructure_6 = 0
        elif query_buildingstructure == "buildingStructure_5":
            buildingStructure_2 = 0
            buildingStructure_3 = 0
            buildingStructure_4 = 0
            buildingStructure_5 = 1
            buildingStructure_6 = 0
        else:
            buildingStructure_2 = 0
            buildingStructure_3 = 0
            buildingStructure_4 = 0
            buildingStructure_5 = 0
            buildingStructure_6 = 1
        query_elevator = int(query_elevator == 'True')

        # Prepare the input features for prediction
        features = [
            query_followers,
            query_square,
            query_livingroom,
            query_drawingroom,
            query_kitchen,
            query_bathroom,
            query_constructiontime,
            query_communityaverage,
            renovationCondition_2,
            renovationCondition_3,
            renovationCondition_4,
            buildingStructure_2,
            buildingStructure_3,
            buildingStructure_4,
            buildingStructure_5,
            buildingStructure_6,
            query_elevator
        ]

        # Make the prediction using the loaded model
        predicted_price = model.predict([features])

        return render_template('index.html', prediction_text=f'Predicted Price: {predicted_price[0]:.2f}')
    except:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


# 1

# In[ ]:




