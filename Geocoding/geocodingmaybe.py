from collections import defaultdict
import time
import csv
import json
import urllib3

http = urllib3.PoolManager()
API_TOKEN = ""
START_INDEX = 100
END_INDEX = 200
necessary_details = [
        "hamlet",
        "suburb",
        "village",
        "town",
        "city_district",
        "city",
        "region",
        "county",
        "state_district",
        "state",
        "postcode",
        "country",
        "country_code"]

# pylint: disable=redefined-outer-name
def api_call(lat, lon):
    """Make the API call in a separate function to use recursion if it fails"""
    r = http.request(
        "GET",
        "https://us1.locationiq.com/v1/reverse.php",
        fields={
            "key": API_TOKEN,
            "lat": lat,
            "lon": lon,
            "format": "json",
            "zoom": 14
            }
        )
    resp_data = json.loads(r.data.decode("utf-8"))
    # print(resp_data)
    try:
        address = resp_data["address"]
    except KeyError:
        print("Error in response, received:", resp_data)
        print("Trying again")
        return api_call(lat, lon)
    return address

with open("./location_details.csv", "at") as outfile:
    writer = csv.writer(outfile, delimiter=",")
    writer.writerow(["image_filename", "lat", "lon"] + necessary_details)
    with open("./details.csv", "rt") as f:
        reader = csv.reader(f, delimiter=",")
        headers = next(reader)
        # skip some rows
        for index, row in zip(range(START_INDEX), reader):
            pass
        print("Skipped first {} rows".format(START_INDEX))
        # print(headers)
        for index, row in zip(range(END_INDEX-START_INDEX), reader):
            start_time = time.time()
            # print(index, row)
            # calculate average latitude longitude
            lon = (float(row[1]) + float(row[2])) / 2.0
            lat = (float(row[3]) + float(row[4])) / 2.0
            # print(lat, lon)
            address = api_call(lat, lon)
            address = defaultdict(lambda: "", address)
            # print(address)
            print("Processing row {}".format(START_INDEX+index))
            writer.writerow([row[0], lat, lon] + [address[detail] for detail in necessary_details])
            # to avoid rate limit of 2 requests per second
            if (time.time() - start_time) < 0.5:
                time.sleep(0.5 - (time.time() - start_time))

