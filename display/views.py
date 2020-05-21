from django.shortcuts import render
from django.http import HttpResponse
from .models import spreadForm
import pandas as pd

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
            #return HttpResponse(cases)

    else:
        form = spreadForm()
        return render(request,'display/spread.html/', {'form': form})


def deathrate(request):
    return HttpResponse("deathrate")