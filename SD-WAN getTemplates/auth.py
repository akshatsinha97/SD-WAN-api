import requests

class Authentication:

    @staticmethod
    def get_jsessionid(base_url, username, password):
        api = "/j_security_check"
        url = base_url + api
        payload = {'j_username' : username, 'j_password' : password}

        response = requests.post(url=url, data=payload, verify=False)
        try:
            cookies = response.headers["Set-Cookie"]
            jsessionid = cookies.split(";")
            return(jsessionid[0])
        except:
            print("No valid JSESSION ID returned\n")
            exit()

    @staticmethod
    def get_token(base_url, jsessionid):
        headers = {'Cookie': jsessionid}
        api = "/dataservice/client/token"
        url = base_url + api      
        response = requests.get(url=url, headers=headers, verify=False)

        if response.status_code == 200:
            return(response.text)
        else:
            return None