import streamlit as st 

import pickle 
import pandas as pd
teams = [ 'Royal Challengers Bangalore', 'Kings XI Punjab',
       'Delhi Daredevils', 'Mumbai Indians', 'Kolkata Knight Riders',
       'Rajasthan Royals', 'Deccan Chargers', 'Chennai Super Kings',
       'Kochi Tuskers Kerala', 'Pune Warriors', 'Sunrisers Hyderabad',
       'Gujarat Lions', 'Rising Pune Supergiants',
       'Rising Pune Supergiant', 'Delhi Capitals', 'Punjab Kings',
       'Lucknow Super Giants', 'Gujarat Titans',
       'Royal Challengers Bengaluru']

cities = ['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
       'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
       'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune']

pipe = pickle.load(open('pipe.pkl','rb'))
st.title('IPL WINNER PREDICTOR')

col1, col2 =st.columns(2)

with col1:
    batting__team = st.selectbox('select the batting team', sorted(teams))

with col2:
    bowling__team = st.selectbox('select the bowling team', sorted(teams))

selected_city = st.selectbox('select the host city',sorted(cities))

target = st.number_input('Target')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
    
with col4:
    overs = st.number_input('Overs Completed')

with col5:
    wickets = st.number_input('Wickets Out')

if st.button('Predict Probabilty'):
    runs_left = target - score 
    balls_left = 120 - (overs*6)
    wickets = 10-wickets
    current_run_rate =score/overs
    required_run_rate = (runs_left*6)/balls_left            

input_df=pd.DataFrame({
    'batting_team': [batting__team],
    'bowling_team': [bowling__team],
    'city': [selected_city],
    'runs_left': [runs_left],
    'balls_left': [balls_left],
    'wickets': [wickets],
    'total_runs_x': [target],
    'curr': [current_run_rate],
    'rrr': [required_run_rate]
})
st.table(input_df)

result = pipe.predict_proba(input_df)

loss = result[0][0]
win = result[0][1]
st.header(batting__team + "- " + str(round(win*100)) + "%")
st.header(bowling__team + "- " + str(round(loss*100)) + "%")