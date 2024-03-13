import requests
def get_location():
    ip = requests.get('https://ipinfo.io/').text
    data = requests.get('https://ipinfo.io/').json()
    city = data['city']
    country = data['country']
    ip_address = data['ip']
    region = data['region']
    org = data['org']
    timezone = data['timezone']
    postal_code = data['postal']
    a = f'City you are in is {city}\nCountry is {country}\nip address is {ip_address}\nregion is {region}\Organization is {org}\nTimezone is {timezone}\n and postal code is {postal_code}'
    print(a)
    return a