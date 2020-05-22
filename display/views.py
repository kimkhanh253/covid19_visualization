from django.http import HttpResponse
from django.shortcuts import render
from .models import spreadForm
import pandas as pd
import requests
import json

def index(request):
    return render(request,'display/index.html/')

def spread(request):
    if request.method == 'POST':
        form = spreadForm(request.POST or None, initial={'state': 'New York, USA'})
        if form.is_valid():
            state = str(form['state'].data)
            df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')
            df_state = df[df['state'].str.contains(state)] 
            df_state = df_state.reset_index(drop=True)
            cases=[]
            cases.append(0)
            deaths=[]
            deaths.append(0)
            for i in df_state.index[1:]:
                cases.append(df_state['cases'][i]-df_state['cases'][i-1]) #calculate the change
                deaths.append(df_state['deaths'][i]-df_state['deaths'][i-1])
            date = [df_state['date'][i] for i in df_state.index]
            return render(request,'display/spread.html/', {
                'form': form,
                'state': state, 
                'date': date,
                'cases': cases,
                'deaths': deaths,
                })

    else:
        form = spreadForm()
        return render(request,'display/spread.html/', {'form': form})


def deathrate(request):
    req = requests.get('https://geog4046.github.io/assignment-resources/data/us_state_demographics_ESRI_2010A.geojson')
    r = req.json()
    states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','District of Columbia','Florida','Georgia','Hawaii','Idaho',
        'Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi',
        'Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio'
        ,'Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia',
        'Washington','West Virginia','Wisconsin','Wyoming']
    df = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv')
    for s in range (0,51):
        state_name = states[s]
        for i in range (0,51):
            df_state = df[df['state'].str.contains(state_name)] 
            df_state = df_state.reset_index(drop=True)
            index = len(df_state.index)-1
            totalDeaths = df_state['deaths'][index]
            totalCases = df_state['cases'][index]
            deathrate = totalDeaths/totalCases * 100
            if str(r['features'][i]['properties']['STATE_NAME']) == state_name:
                r['features'][i]['properties']['deathrate'] = round(deathrate,2)
    return render(request,'display/deathrate.html/',{'data': json.dumps(r)})