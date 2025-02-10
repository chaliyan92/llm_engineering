import requests


class RequestUtil:
    @staticmethod
    def get(url, params=None, headers=None):
        try:
            response = requests.get(url, params=params, headers=headers, verify=False)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"GET request failed: {e}")
            return None

    @staticmethod
    def post(url, data=None, json=None, headers=None):
        try:
            response = requests.post(url, data=data, json=json, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"POST request failed: {e}")
            return None

    @staticmethod
    def put(url, data=None, json=None, headers=None):
        try:
            response = requests.put(url, data=data, json=json, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"PUT request failed: {e}")
            return None

    @staticmethod
    def delete(url, headers=None):
        try:
            response = requests.delete(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"DELETE request failed: {e}")
            return None
