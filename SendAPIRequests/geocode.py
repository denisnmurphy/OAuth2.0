import httplib2
import json

def getGeocodeLocation(inputString):
    google_api_key = "AIzaSyBM6-8IGPA4zThCp-4Vh3rcAWzX1x_eLfk"
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'%
            (locationString, google_api_key))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)

    latitude = results['results'][0]['geometry']['location']['lat']
    longitude = results['results'][0]['geometry']['location']['lng']
    return(latitude, longitude)
