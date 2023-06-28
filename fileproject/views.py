import csv
import pandas as pd
from django.shortcuts import render

def index(request):
    # Define the path to your CSV file
    csv_file_path = 'fileproject/static/SampleCSVFile_556kb.csv'
    
    df = pd.read_csv(csv_file_path, encoding='latin-1')
    return render(request, 'index.html', {'columns': df.columns, 'rows': df.to_dict('records')})

