import time
import csv
import os
import requests


START_INDEX = 0
END_INDEX = 538000
API_KEYS = []

count = 0
i = 0


def api_json(lat_lng):
    global count
    global i
    count = count+1
    API_KEY = API_KEYS[0]
    if(count == 599):
        i = i+1
        API_KEY = API_KEYS[i]
    url = 'https://api.mapbox.com/geocoding/v5/mapbox.places/' + \
        lat_lng+'.json?access_token='+API_KEY
    result = requests.get(url).json()
    locality = ''
    district = ''
    try:
        a = 0
        for i in result["features"]:
            a = a+1
        for i in range(0, a):
            if result["features"][i]['place_type'][0] == 'locality':
                locality = result["features"][i]['text']
        for i in range(0, a):
            if result["features"][i]['place_type'][0] == 'district':
                district = result["features"][i]['text']
    except Exception as e:
        print(e)
        return api_json(lat_lng)
    address = [locality, district]
    return address


with open("./location_details.csv", "at") as outfile:
    writer = csv.writer(outfile, delimiter=",")
    #writer.writerow(["image_filename", "lat","long","full_address","locality","pincode"])
    with open("./output_1.csv", "rt") as f:
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
            latlng = str(lon)+','+str(lat)
            print(latlng)
            address = api_json(latlng)
            # print(address)
            print("Processing row {}".format(START_INDEX+index))
            writer.writerow([row[0], lat, lon]+address)
