import requests
from datetime import datetime


def get_data(url):
    """
    Здесь могла быть ваша документация
    return: data.json
    """

    try:
        data = requests.get(url)
        if data.status_code == 200:
            return data.json(), "INFO: Данные получены успешно"
        return None, f"ERROR: status_code: {data.status_code}"
    except requests.exceptions.ConnectionError:
        return None, "ERROR: requests.exceptions.ConnectionError"
    except requests.exceptions.JSONDecodeError:
        return None, "ERROR: requests.exceptions.JSONDecodeError"


def get_filtered_data(data, filtered_empty_from=False):
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    if filtered_empty_from:
        data = [x for x in data if "from" in x]
    return data


def get_last_values(data, count_last_values):
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    data = data[:count_last_values]
    return data


def get_formatted_data(data):
    formatted_data = []
    for x in data:
        date = datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = x["description"]
        from_info, from_bill = "", ""

        if "from" in x:
            sender = x["from"].split()
            from_bill = sender.pop(-1)
            from_bill = f'{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}'
            from_info = " ".join(sender)

        to = f"{x['to'].split()[0]} **{x['to'][-4:]}"
        operation_amount = f"{x['operationAmount']['amount']} {x['operationAmount']['currency']['name']}"

        formatted_data.append(f'{date} {description} \n'
                              f'{from_info} {from_bill} --> {to}\n'
                              f'{operation_amount}')

    return formatted_data
