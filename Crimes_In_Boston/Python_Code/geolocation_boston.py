#Import libraries 
from geopy.geocoders import Nominatim
import pandas as pd

#Set credentials
geolocator = Nominatim(user_agent="boston-location")

#Read the Dataset with the latitude, longitude and location
boston_location = pd.read_csv('loc_lat_long.csv')

#Changes the Latitude and Longitude type to string
boston_location['Lat'] = boston_location['Lat'].astype(str)
boston_location['Long'] = boston_location['Long'].astype(str)

#Fill the Dataset with the street names and the suburbs
location_index = boston_location[(boston_location['Street'].isna()) | (boston_location['Suburb'].isna())].index

for index in location_index:
    try:
        Latitude = boston_location.loc[index, 'Lat'] #Get the Latitude 
        Longitude = boston_location.loc[index, 'Long'] #Get the Longitude

        location = geolocator.reverse(Latitude+","+Longitude)
        address = location.raw['address']
        
        boston_location.loc[index, 'Street'] = address.get('road', '') #Put the correct name of the street in the dataset
        boston_location.loc[index, 'Suburb'] = address.get('suburb', '') #Create a new column with the suburb
        
    except:
        continue;

boston_location.to_csv('loc_lat_long.csv', index=False) #Saves the changes in csv file using the same name