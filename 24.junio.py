import requests


def getcats():
    url = "https://cataas.com/cat"
    # https://dog.ceo/dog-api/breeds-list
    response = requests.get(url, stream=True)
    print(response.status_code)
    if response.status_code == 200:
        with open("cat.jpg", "wb") as f:
            f.write(response.content)
            


if __name__ == "__main__":
    getcats()
