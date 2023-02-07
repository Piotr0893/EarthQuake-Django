from django.shortcuts import render
import json
import urllib
import datetime



# Create your views here.
def Last24EarthQuakes(request):
    urlData ="http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"          # URL for the earthquake data API  
    webURL = urllib.request.urlopen(urlData)                                                     
    data = webURL.read()   
                                                                       # Read the data from the URL
    if request.method == 'GET':
        json_data = json.loads(data)
        earthquakes_data = []                               # Initialize the list to store earthquake data
        for earthquake in json_data['features']:            # Loop through each earthquake feature
            place = earthquake['properties']['place']       # Get the place of the earthquake
            magnitude = earthquake['properties']['mag']     # Get the magnitude of the earthquake
                   # Get the time of the earthquake
            earthquakes_data.append({'place': place, 'magnitude': magnitude,})
    return render(request, 'EarthQuakes.html', {'json_data': earthquakes_data})       



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


