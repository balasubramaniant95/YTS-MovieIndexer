import json
import sys
import argparse
from urllib import request
from urllib import parse
import textwrap

url = "https://yts.tl/api/"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
}


def call_api(uri):
    global headers
    print(uri)
    try:
        req = request.Request(method="GET", url=uri, headers=headers)
        req = request.urlopen(req)
        return json.loads(req.read())
    except Exception as e:
        print("YTS.LT api call failed with exception- ", end="")
        print(str(e))
        sys.exit(1)


def get_movie_info(movie_id):
    try:
        uri = url + "v2/movie_details.json?movie_id={}&with_cast=true".format(movie_id)
        req_resp = call_api(uri=uri)

        if req_resp["status"] != 'ok':
            print("YTS.LT Api Failure at page {}".format(page_counter))
            print("Returned Status = {}".format(req_resp["status"]))
            print("Returned Status Message = {}".format(req_resp["status_message"]))
            sys.exit(1)

        if req_resp["data"]["movie"]:
            return req_resp["data"]["movie"]

    except Exception as e:
        print("get_movie_info() failed with exception- ", end="")
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

            if req_resp["data"]["movie_count"] == 0:
                print("\n{-> No Results Found <-}")
                sys.exit(1)

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
    print("{:<5} - {:<10} - {:<50} - {:<10} - {:<15} - {:<15} - {:<15} - {:<100}".format("sl.no", "index_id", "title",
                                                                                         "year",
                                                                                         "imdb_rating",
                                                                                         "mpa_rating", "language",
                                                                                         "download options"))
    sl_no = 0
    for entry in data:
        sl_no += 1
        index_id = entry["id"]
        title = entry["title"]
        year = entry["year"]
        imdb_rating = entry["rating"]
        mpa_rating = entry["mpa_rating"]
        language = entry["language"]
        available_quality = []
        for option in entry["torrents"]:
            quality = option["quality"] + '|' + option["type"] + ' - ' + option["size"]
            available_quality.append(quality)

        print("{:<5} - {:<10} - {:<50} - {:<10} - {:<15} - {:<15} - {:<15} - {}".format(sl_no, index_id, title, year,
                                                                                        imdb_rating, mpa_rating,
                                                                                        language,
                                                                                        available_quality))


def pretty_print_movie_info(data):
    movie_id = data["id"]
    movie_url = "https://yts.tl" + data["url"]
    movie_title = data["title_long"]
    movie_year = data["year"]
    movie_rating = data["rating"]
    movie_runtime = data["runtime"]
    movie_genre = ' | '.join(map(str, data["genres"]))
    movie_download_count = data["download_count"]
    movie_like_count = data["like_count"]
    movie_dec = data["description_full"]
    movie_lang = data["language"]
    movie_mpa_rating = data["mpa_rating"]
    movie_poster = "https://yts.tl" + data["large_cover_image"]
    movie_cast = data["cast"]
    movie_torrents = data["torrents"]

    print(movie_title.center(106, '-'))
    print("{:<30}: {:>74}".format("yts.lt link", movie_url))
    print("{:<30}: {:>74}".format("Movie genre", movie_genre))
    print("{:<30}: {:>74}".format("poster", movie_poster))
    print("~~~~~~~~~~~~~~~~~~~~".center(106, ' '))
    print("{:<15}: {:<34} | {:<15}: {:>35}".format("Total Downloads", movie_download_count, "Likes", movie_like_count))
    print("{:<15}: {:<34} | {:<15}: {:>35}".format("MPA rating", movie_mpa_rating, "IMDb rating", movie_rating))
    print("{:<15}: {:<34} | {:<15}: {:>35}".format("Language", movie_lang, "Year Released", movie_year))
    print("{:<15}: {:<34} | {:<15}: {:>35}".format("Movie ID", movie_id, "Runtime (mins)", movie_runtime))
    print("~~~~~~~~~~~~~~~~~~~~".center(106, ' '))
    print("Synopsis: ")
    print(textwrap.fill(movie_dec, width=106))
    print("~~~~~~~~~~~~~~~~~~~~".center(106, ' '))
    print("Cast: ")
    for actors in movie_cast:
        print("   |-> {:>42} ~ AS ~ {:<42} <-|   ".format(actors["name"], actors["character_name"]))
    print("~~~~~~~~~~~~~~~~~~~~".center(106, ' '))
    print("Download Options: ")
    for option in movie_torrents:
        print(
            " Quality: {:<7} | Type: {:<15} | Seeds: {:>7} |   Peers: {:<15} |  Size: {:>10}".format(option["quality"],
                                                                                                     option["type"],
                                                                                                     option["seeds"],
                                                                                                     option["peers"],
                                                                                                     option["size"]))
        torrent_file_link = " https://yts.tl" + option["url"] + " "
        print(torrent_file_link.center(106, '~'))
        print("")
    print(''.center(106, '-'))


def main():
    parser = argparse.ArgumentParser(description='Specify input arguments...')
    parser.add_argument('--most_downloaded', action="store_true", default=False,
                        help='specifier to print the most downloaded movies')
    parser.add_argument('--recently_added', action="store_true", default=False,
                        help='specifier to print the most recently added movies')
    parser.add_argument('--movie_index', type=int, default=False,
                        help='specifier to print details about the movie')
    parser.add_argument('--limit', type=int, default=10,
                        help="specify the number of results. the value must be an integer and also greater than zero \
                        (0). by default, it's value is set to 10")
    parser.add_argument('--quality', type=str, default='all', choices=["720p", "1080p", "3D", "All"],
                        help="specifier to filter the results by quality. to be used along with --query_term specifier. by default, it's value is set to 'All'")
    parser.add_argument('--query_term', type=str, default=False,
                        help='specify word to query movies.')
    parser.add_argument('--sort_by', type=str, default='date_added',
                        choices=["title", "year", "rating", "peers", "seeds", "download_count", "like_count",
                                 "date_added"],
                        help="specifier to filter results by available sorting methods. to be used along with --query_term specifier.  by default, it's value is set to 'date_added'")
    parser.add_argument('--min_rating', type=int, default='0', choices=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                        help="specifier to filter results by IMDb rating. to be used along with --query_term specifier.  by default, it's value is set to '0'")
    parser.add_argument('--order_by', type=str, default='desc', choices=['desc', 'asc'],
                        help='specifier to sort the results by top-bottom or bottom-top. to be used along with --query_term specifier. default is bottom-top')
    parser.add_argument('--genre', type=str, default='all',
                        choices=['action', 'adventure', 'animation', 'biography', 'comedy', 'crime', 'documentary',
                                 'drama', 'family', 'fantasy', 'film-noir', 'game-show', 'history', 'horror', 'music',
                                 'musical', 'mystery', 'news', 'reality-tv', 'romance', 'sci-fi', 'sport', 'talk-show',
                                 'thriller', 'war', 'western'],
                        help="specifier to filter results by available genres. to be used along with --query_term specifier. by default, it's value is set to 'all'")

    args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)

    if args.most_downloaded and True not in {args.movie_index, args.recently_added, args.query_term}:
        data = get_movies(req_uri="v2/list_movies.json?sort_by=download_count&genre={}".format(args.genre),
                          limit=args.limit)
        pretty_print_movies(data=data)
        sys.exit(1)

    if args.recently_added and True not in {args.movie_index, args.most_downloaded, args.query_term}:
        data = get_movies(req_uri="v2/list_movies.json?sort_by=date_added&genre={}".format(args.genre),
                          limit=args.limit)
        pretty_print_movies(data=data)
        sys.exit(1)

    if args.query_term and True not in {args.most_downloaded, args.recently_added, args.movie_index}:
        print("Query Options:")
        print("--quality, --sort_by, --min_rating, --genre, --order_by", end="\n\n")
        parser.print_usage()
        print("")
        args.limit = 50
        data = get_movies(
            req_uri="v2/list_movies.json?quality={}&query_term={}&sort_by={}&minimum_rating={}&genre={}&order_by={}".format(
                args.quality, parse.quote(args.query_term), args.sort_by, args.min_rating, args.genre, args.order_by),
            limit=args.limit)
        pretty_print_movies(data=data)
        sys.exit(1)

    if args.movie_index and True not in {args.most_downloaded, args.recently_added, args.query_term}:
        data = get_movie_info(movie_id=args.movie_index)
        pretty_print_movie_info(data=data)
        sys.exit(1)

    else:
        parser.print_usage()
        sys.exit(1)


if __name__ == '__main__':
    main()
