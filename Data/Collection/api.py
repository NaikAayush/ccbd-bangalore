import time
import csv
import os
import requests

def api_json(lat_lng, API_KEY):
    url = 'https://revgeocode.search.hereapi.com/v1/revgeocode?at='+lat_lng+'&lang=en-US&apiKey='+API_KEY
    result = requests.get(url).json()
    print(result)
    county = ''
    district = ''
    city = ''
    postalCode = ''
    subdistrict = ''
    try:
        try:
            district=result['items'][0]['address']['district']
        except Exception:
            pass
        try:
            county=result['items'][0]['address']['county']
        except Exception:
            pass
        try:
            city=result['items'][0]['address']['city']
        except Exception:
            pass
        try:
            postalCode=result['items'][0]['address']['postalCode']
        except Exception:
            pass
        try:
            subdistrict=result['items'][0]['address']['subdistrict']
        except Exception:
            pass
    except Exception as e:
        print(e)
        return api_json(lat_lng)
    address = [postalCode,district,subdistrict,county,city]
    return address


def start(START_INDEX, END_INDEX, API_KEY, INPUT, OUTPUT):
    with open(OUTPUT, "at") as outfile:
        writer = csv.writer(outfile, delimiter=",")
        with open(INPUT, "rt") as f:
            reader = csv.reader(f, delimiter=",")
            headers = next(reader)
            for index, row in zip(range(START_INDEX), reader):
                pass
            print("Skipped first {} rows".format(START_INDEX))
            # print(headers)
            for index, row in zip(range(END_INDEX-START_INDEX), reader):
                # print(index, row)
                # calculate average latitude longitude
                lon = (float(row[1]) + float(row[2])) / 2.0
                lat = (float(row[3]) + float(row[4])) / 2.0
                # print(lat, lon)
                latlng = str(lat)+'%2C'+str(lon)
                print(latlng)
                address = api_json(latlng, API_KEY)
                # print(address)
                print("Processing row {}".format(START_INDEX+index))
                writer.writerow([row[0], lat, lon]+address)
