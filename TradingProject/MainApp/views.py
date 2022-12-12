from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

# Create your views here.

def read_cvs_(request):
    file_=pd.read_csv("NIFTY_F1_Xm8mAtb.csv")
    pass