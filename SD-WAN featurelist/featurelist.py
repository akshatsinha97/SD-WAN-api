import requests
import json

class Feature_list:

    def device_details(self, base_url, headers):
        
        endpoint = '/dataservice/device'
        url = base_url + endpoint
        response = requests.get(url=url, headers=headers, verify=False).json()
        
        print(json.dumps(response['data'][0]['deviceId'], indent=2))
        return response['data'][0]['deviceId']

    def features(self, base_url, headers, DeviceId):

        endpoint = '/dataservice/device/featurelist'
        url = base_url + endpoint
        print(DeviceId)
        response = requests.get(url=url, headers=headers, params={'deviceId':DeviceId}, verify=False).json()

        print(json.dumps(response['data'], indent=2))