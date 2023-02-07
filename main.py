from utils.func import get_data, get_filtered_data
from pprint import pprint


def main():
    OPERATIONS_URL = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1675862397490&signature=dYHgxv-izPaHxNM4UA_KmBd9VFOxw7vh2G-Zz2F5hho&downloadName=operations.json"
    FILTERED_EMPTY_FROM = True

    data, info = get_data(OPERATIONS_URL)
    if not data:
        exit(info)
    else:
        print(data)

    data = get_filtered_data(data, filtred_from_empty=FILTERED_EMPTY_FROM)


if __name__ == '__main__':
    main()
