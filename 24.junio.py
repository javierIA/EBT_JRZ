import requests


def getcats():
    url = "https://cataas.com/cat"
    # https://dog.ceo/dog-api/breeds-list
    response = requests.get(url, stream=True)
    print(response.status_code)


if __name__ == "__main__":
    getcats()
