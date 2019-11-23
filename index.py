import json
import sys
from urllib import request
import argparse

url = "https://yts.tl/api/"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
}


def call_api(uri):
    global headers
    try:
        req = request.Request(method="GET", url=uri, headers=headers)
        req = request.urlopen(req)
        return json.loads(req.read())
    except Exception as e:
        print("YTS.LT api call Failed with exception- ", end="")
        print(str(e))
        sys.exit(1)


def get_movies(req_uri, limit=50):
    # setting limit to 50 which is yts.lt api's limit on list movies api call.
    page_limit_counter_list = [50] * divmod(limit, 50)[0]
    if divmod(limit, 50)[1] != 0:
        page_limit_counter_list.append(divmod(limit, 50)[1])

    page_counter = 1

    return_data = []
    for result_count in page_limit_counter_list:
        try:
            uri = url + "{}&page={}&limit={}".format(req_uri, page_counter, result_count)
            req_resp = call_api(uri=uri)

            if req_resp["status"] != 'ok':
                print("YTS.LT Api Failure at page {}".format(page_counter))
                print("Returned Status = {}".format(req_resp["status"]))
                print("Returned Status Message = {}".format(req_resp["status_message"]))
                page_counter += 1
                continue

            if req_resp["data"]["movies"]:
                return_data.extend(req_resp["data"]["movies"])
            page_counter += 1

        except Exception as e:
            page_counter += 1
            print("get_movies() failed at page {} with exception- ".format(page_counter - 1), end="")
            print(str(e))
            continue

    return return_data


def pretty_print_movies(data):
    print("{:<10} - {:<50} - {:<10} - {:<15} - {:<15} - {:<100}".format("index_id", "title", "year", "imdb_rating", "mpa_rating", "download options"))
    for entry in data:
        index_id = entry["id"]
        title = entry["title"]
        year = entry["year"]
        imdb_rating = entry["rating"]
        mpa_rating = entry["mpa_rating"]
        available_quality = []
        for option in entry["torrents"]:
            quality = option["quality"] + '|' + option["type"] + ' - ' + option["size"]
            available_quality.append(quality)

        print("{:<10} - {:<50} - {:<10} - {:<15} - {:<15} - {}".format(index_id, title, year, imdb_rating, mpa_rating, available_quality))


def main():
    data = get_movies(req_uri="v2/list_movies.json?sort_by=download_count", limit=10)
    pretty_print_movies(data=data)


if __name__ == '__main__':
    main()
