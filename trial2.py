# importing the requests library 
import requests 
import ndg-httpsclient

import pyopenssl

import pyasn1
# api-endpoint 
URL = "https://www.kluniversity.in/resprint.aspx?id=1900018&stype=A"

# location given here 
#location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API 
#PARAMS = {'address':location} 
hdrs = {'Host': 'www.kluniversity.in', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1', 'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Mobile Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Cookie': 'visited=true'
}
# sending get request and saving the response as response object 
r = requests.get(url = URL, verify=True, headers=hdrs)
print(r.status_code)
# extracting data in json format 
data = r.json() 

print(data)
"""
# extracting latitude, longitude and formatted address 
# of the first matching location 
latitude = data['results'][0]['geometry']['location']['lat'] 
longitude = data['results'][0]['geometry']['location']['lng'] 
formatted_address = data['results'][0]['formatted_address'] 

# printing the output 
print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
	%(latitude, longitude,formatted_address)) 
"""