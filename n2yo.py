import requests

def satellite_info(satIDs, observer_lat, observer_lng, observer_alt, seconds, api_key):
    base_url = "https://api.n2yo.com/rest/v1/satellite/positions/"

    for satID in satIDs:
        url = f"{base_url}{satID}/{observer_lat}/{observer_lng}/{observer_alt}/{seconds}/&apiKey={api_key}"
        response = requests.get(url)
        data = response.json()

        if 'positions' in data:
            position = data["positions"][0]
            print(f"\nSatellite Name ({satID}):", data["info"]["satname"])
            print("Latitude:", position["satlatitude"])
            print("Longitude:", position["satlongitude"])
            print("Azimuth:", position["azimuth"])
            print("Elevation:", position["elevation"])
            print("RA:", position["ra"])
            print("DEC:", position["dec"])
            print("TimeStamp:", position["timestamp"])
        else:
            print(f"\nError for Satellite ID {satID}:", data.get("Error", "Unknown Error"))


satIDs = [25544, 25543]
observer_lat = 40.7127492
observer_lng = -74.0059945
observer_alt = 0
seconds = 1
api_key = "Your API Key Here"

satellite_info(satIDs, observer_lat, observer_lng, observer_alt, seconds, api_key)

