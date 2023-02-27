from django.shortcuts import render, redirect
import json
import urllib
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import pandas as pd


# Create your views here.
def Last1hMap(request):
    m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80,
                    llcrnrlon=-180, urcrnrlon=180, resolution='c')
    m.drawcoastlines()
    m.drawcountries()
    path = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.csv"  # this is the .csv file
    data1 = pd.read_csv(path)             # reading the data set 
    lon = []                            # extracting information from data set
    for i in data1['longitude']:
        lon.append(i)
    lat = []
    for i in data1['latitude']:
        lat.append(i)
    x, y = m(lon, lat)                   #converting longitude ,laitude to x ,y
    sizes = data1['mag'].values ** 2     # different size of plot point
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    sizes = np.array(sizes, dtype=float)
    m.scatter(x, y, marker='o', c=data1['mag'], s=sizes, label=data1['mag'])     #plotting the data
    plt.show()
    return redirect ('Last1Hour')

def Last7dMap(request):
    m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80,
                    llcrnrlon=-180, urcrnrlon=180, resolution='c')
    m.drawcoastlines()
    m.drawcountries()
    path = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.csv"  # this is the .csv file
    data1 = pd.read_csv(path)             # reading the data set 
    lon = []                            # extracting information from data set
    for i in data1['longitude']:
        lon.append(i)
    lat = []
    for i in data1['latitude']:
        lat.append(i)
    x, y = m(lon, lat)                   #converting longitude ,laitude to x ,y
    sizes = data1['mag'].values ** 2     # different size of plot point
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    sizes = np.array(sizes, dtype=float)
    m.scatter(x, y, marker='o', c=data1['mag'], s=sizes, label=data1['mag'])     #plotting the data
    plt.show()
    return redirect ('Last7Days')

def Last24hMap(request):
    m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80,
                    llcrnrlon=-180, urcrnrlon=180, resolution='c')
    m.drawcoastlines()
    m.drawcountries()
    path = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv"  # this is the .csv file
    data1 = pd.read_csv(path)             # reading the data set 
    lon = []                            # extracting information from data set
    for i in data1['longitude']:
        lon.append(i)
    lat = []
    for i in data1['latitude']:
        lat.append(i)
    x, y = m(lon, lat)                   #converting longitude ,laitude to x ,y
    sizes = data1['mag'].values ** 2     # different size of plot point
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    sizes = np.array(sizes, dtype=float)
    m.scatter(x, y, marker='o', c=data1['mag'], s=sizes, label=data1['mag'])     #plotting the data
    plt.show()
    return redirect ('Last24Hours')

def Last24Hours(request):
    urlData ="http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"      # URL for the earthquake data API  
    webURL = urllib.request.urlopen(urlData)                                                     
    data = webURL.read()   
                                                                       # Read the data from the URL
    if request.method == 'GET':
        json_data = json.loads(data)
        earthquakes_data = []                               # Initialize the list to store earthquake data
        for earthquake in json_data['features']:            # Loop through each earthquake feature
            place = earthquake['properties']['place']       # Get the place of the earthquake
            magnitude = earthquake['properties']['mag']     # Get the magnitude of the earthquake
                   
            earthquakes_data.append({'place': place, 'magnitude': magnitude,})
    return render(request, 'Last24Hours.html', {'json_data': earthquakes_data})       


def Last1Hour(request):
    urlData = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson'
    webURL = urllib.request.urlopen(urlData)  
    data = webURL.read()
    if request.method == 'GET':
        json_data = json.loads(data)
        earthquakes_data = [] 
        for earthquake in json_data['features']:            
            place = earthquake['properties']['place']       
            magnitude = earthquake['properties']['mag']
             
            earthquakes_data.append({'place': place,'magnitude': magnitude,})
    return render(request, 'Last1Hour.html', {'json_data': earthquakes_data})  

def Last7Days(request):
    urlData = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson'
    webURL = urllib.request.urlopen(urlData)  
    data = webURL.read()
    if request.method == 'GET':
        json_data = json.loads(data)
        earthquakes_data = [] 
        for earthquake in json_data['features']:            
            place = earthquake['properties']['place']       
            magnitude = earthquake['properties']['mag']
             
            earthquakes_data.append({'place': place,'magnitude': magnitude,})
    return render(request, 'Last7Days.html', {'json_data': earthquakes_data})  


def main(request):
  return render(request, 'home.html')       


