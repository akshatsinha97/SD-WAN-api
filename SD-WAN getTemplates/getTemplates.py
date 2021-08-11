import json
import requests

def getTemplates(base_url, headers):

    api_endpoint = '/dataservice/template/feature?templateType=aaa'
    url=base_url+api_endpoint
    response = requests.get(url=url, headers=headers, verify=False).json()
    filter = response['data']
    # print(json.dumps(filter, indent=2))
    
    list=[]
    for items in filter:
        
        if 'templateDefinition' in items:
            
            new_dict = {key:val for key, val in items.items()
                        if key != 'templateDefinition' and key != 'deviceType'}
            print(new_dict)
            
            list.append(new_dict)
            print(json.dumps(list, indent=2))