#Import libraries 
from geopy.geocoders import Nominatim
import pandas as pd
import difflib

#Set credentials
geolocator = Nominatim(user_agent="boston-location")

#Read the Dataset with the latitude, longitude and location
boston_location = pd.read_csv('../Crimes_In_boston/DataSets/loc_lat_long.csv')

#Changes the Latitude and Longitude type to string
boston_location['Lat'] = boston_location['Lat'].astype(str)
boston_location['Long'] = boston_location['Long'].astype(str)

#Fill the Dataset with the street names and the suburbs
location_index = boston_location.index

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

#Load Streetbook
file = open('../Txt/streetbook.txt', 'r')
streetbook = file.readlines()
streetbook = [st.replace("\n", '') for st in streetbook]
file.close()

#Create a new list of streets that are not in the streetbook, or are different
unique_st = boston_location['Street'].unique() #Unique Streets
out_streetbook = [st for st in unique_st if st not in streetbook]

#Correcting writing differences
correction = {}
for out in out_streetbook:
    if difflib.get_close_matches(out, streetbook, cutoff=0.8):
        correcttion[out] = difflib.get_close_matches(out, streetbook, cutoff=0.8)[0]

#Streets that difflib get wrong
correction['Airport Road'] = 'Service Road'
correction['Alton Court'] = 'Turquoise Way'
correction['Beechland Street'] = 'Beechland Circle'
correction['Central Square North'] = 'Saratoga Street'
correction['Constitution Beach Road'] = 'Barnes Avenue'
correction['Constitution Plaza'] = 'Constitution Wharf'
correction['Dalton Road'] = 'Campanella Way'
correction['Edgeworth Street'] = 'First Avenue'
correction['Fish Pier Road'] = 'Boston Fish Pier'
correction['Franklin Park Service Road'] = 'Circuit Drive'
correction['Garfield Avenue Extension'] = 'Garfield Avenue'
correction['Green Park'] = 'Campanella Way'
correction['Oakdale Square'] = 'Oakdale Street'
correction['Ping On Street'] = 'Ping On Alley'
correction['Public Alley 904'] = 'Public Alley No 903'
correction['Terminal Road'] = 'Terminal E Arrivals'

#Set the changes
boston_location.loc[boston_location['Street'].isin(correction), 'Street'] = boston_location['Street'].map(correction)

boston_location.to_csv('../Crimes_In_Boston/DataSets/loc_lat_long_suburb.csv', index=False) #Saves the changes in csv file using the same name