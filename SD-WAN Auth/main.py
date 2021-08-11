from auth import Authentication
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

creds = {'vmanage_host': 'https://sandbox-sdwan-1.cisco.com',
        'vmanage_username': 'devnetuser',
        'vmanage_password': 'RG!_Yw919_83'
        }

Auth = Authentication()
jsessionid = Auth.get_jsessionid(creds['vmanage_host'],
                                creds['vmanage_username'], creds['vmanage_password'])

token = Auth.get_token(creds['vmanage_host'], jsessionid)

if token is not None:
    print(f'The token is: {token}')
else:
    print(f'The session id is: {jsessionid}')