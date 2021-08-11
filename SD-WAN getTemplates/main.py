from auth import Authentication
from getTemplates import getTemplates
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

creds = {'vmanage_host': 'https://sandbox-sdwan-1.cisco.com',
        'vmanage_username': 'devnetuser',
        'vmanage_password': 'RG!_Yw919_83'
        }

base_url = creds['vmanage_host']

Auth = Authentication()
jsessionid = Auth.get_jsessionid(base_url,
                                creds['vmanage_username'], creds['vmanage_password'])

token = Auth.get_token(base_url, jsessionid)

if token is not None:
    headers = {'Content-Type': "application/json",'Cookie': jsessionid, 'X-XSRF-TOKEN': token}
else:
    headers = {'Content-Type': "application/json",'Cookie': jsessionid}

getTemplates(base_url, headers)