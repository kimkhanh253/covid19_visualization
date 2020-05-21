from django.db import models
from django import forms

state = (
    ('Baton Rouge', 'Baton Rouge, USA'),
    ('Delhi','Delhi, India'),
    ('Fresno','Fresno, USA'),
    ('New York', 'New York, USA'),

    ('Alabama','Alabama'),
    ('Alaska','Alaska'),
    ('Arizona','Arizona'),
    ('Arkansas','Arkansas'),
    ('California','California'),
    ('Colorado','Colorado'),
    ('Connecticut','Connecticut'),
    ('Delaware','Delaware'),
    ('Florida','Florida'),
    ('Georgia','Georgia'),
    ('Hawaii','Hawaii'),
    ('Idaho','Idaho'),
    ('Illinois','Illinois'),
    ('Indiana','Indiana'),
    ('Iowa','Iowa'),
    ('Kansas','Kansas'),
    ('Kentucky','Kentucky'),
    ('Louisiana','Louisiana'),
    ('Maine','Maine'),
    ('Maryland','Maryland'),
    ('Massachusetts','Massachusetts'),
    ('Michigan','Michigan'),
    ('Minnesota','Minnesota'),
    ('Mississippi','Mississippi'),
    ('Missouri','Missouri')


)

class spreadForm (forms.Form):
    state = forms.CharField(widget=forms.Select(choices=state))