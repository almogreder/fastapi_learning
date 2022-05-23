
import pandas as pd

countries=pd.read_html('https://www.geonames.org/countries/')[1]

countries.columns=[col.replace(' ','_') for col in countries.columns]

countries=countries.rename(columns={'Area_in_km²':'Area_in_km'})

countries.index=countries['Country'].str.lower()
countries_json=countries.to_json('countries.json',orient='index')
#json.load(open('countries.json'))