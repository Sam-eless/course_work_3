import requests


class Transactions:
    def __init__(self, dict_info):
        self.state = dict_info["state"]
        self.date = dict_info["date"]

    def __repr__(self):
        pass

    def get_status(self):
        pass

    def get_date(self):
        pass

    def get_description(self):
        pass


def get_data(url):

    try:
        data = requests.get(url)
        if data.status_code == 200:
            return data.json(), "INFO: Данные получены успешно"
        return None, f"ERROR: status_code: {data.status_code}"
    except requests.exceptions.ConnectionError:
        return None, "ERROR: requests.exceptions.ConnectionError"
    except requests.exceptions.JSONDecodeError:
        return None, "ERROR: requests.exceptions.JSONDecodeError"


def get_filtered_data(data, filtred_from_empty=False):
    print(len(data))
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    print(len(data))
    if filtred_from_empty:
        data = [x for x in data if "from" in x]
    print(len(data))
    return data
