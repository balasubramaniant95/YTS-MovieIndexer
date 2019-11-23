import json
from urllib import request

url = "https://yts.tl/api/"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
}


def list_movies():
    global headers
    try:
        uri = url + "v2/list_movies.json"
        req = request.Request(method="GET", url=uri, headers=headers)
        req = request.urlopen(req)
        print(json.loads(req.read()))
    except Exception as e:
        print(str(e))


def main():
    list_movies()


if __name__ == '__main__':
    main()
