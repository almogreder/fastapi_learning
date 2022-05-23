from fastapi import FastAPI,Path
from typing import Optional
import json
from pydantic import BaseModel
import uvicorn

#rewrites the json file containiang all the countries
def rewrite_json(data,file_name='countries.json'):
    with open(file_name, 'w') as f:
        json.dump(data, f)

countries=json.load(open('countries.json'))

app=FastAPI()

class Country(BaseModel):
    Country:Optional[str] = None
    Capital:Optional[str] = None
    Area_in_km:Optional[float] = None
    Population:Optional[int] = None
    Continent:Optional[str] = None


@app.get('/get-country/{country_name}')
def get_country(country_name:str = Path(None, description= "The name of the country you want to view")):
    if(country_name not in countries):
        return {"Error":"Country doesn't exist"}
    return countries[country_name.lower()]


@app.post('/create-country')
def create_country(country_name: str,country: Country):
    country_name=country_name.lower()
    if country_name in countries:
        return {"Error":'Country exists, please refer to the "update_country" function if you would like to add anything.'}
    
    countries[country_name]=country.dict()
    rewrite_json(countries)
    return countries[country_name]


@app.put('/update-values-for-country')
def create_country(country_name: str,country: Country):
    country_name=country_name.lower()
    if(country_name not in countries):
        return {"Error":'Country doesnt exist, please refer to the "create_country" function if you would like to create a country.'}
    
    for key in country.dict().keys():
        if (country.dict()[key]!=None):
            countries[country_name][key]=country.dict()[key]
    
    rewrite_json(countries)
    return countries[country_name]

@app.delete('/delete-country')
def delete_counter(country_name: str):
    country_name=country_name.lower()
    if(country_name not in countries):
        return {"Error":"Country doesn't exist."}
    del (countries[country_name])
    rewrite_json(countries)
    return {'Message':'Country deleted sucessfully.'}

if __name__=='__main__':
    uvicorn.run(app, port=8000, host="0.0.0.0")