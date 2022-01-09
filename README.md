# yts-movie-indexer
A fun and very basic repo exploring yts.lt's api capabilities for movie indexing and search. Uses basic api calls through python's urllib and pretty prints the results.

API Documentation:
https://yts.mx/api

***
### Capabilities
* List most recently added to yts filterable by genre
* List most downloaded moved at yts filterable by genre
* Query movies by keyword and filter them by quality, rating, genre, etc
* Print details about the movie along with .torrent file download links

***
### Usage
```
$ docker run yts-api-v1:latest --help
usage: index.py [-h] [--most_downloaded] [--recently_added]
                [--movie_index MOVIE_INDEX] [--limit LIMIT]
                [--quality {720p,1080p,3D,All}] [--query_term QUERY_TERM]
                [--sort_by {title,year,rating,peers,seeds,download_count,like_count,date_added}]
                [--min_rating {0,1,2,3,4,5,6,7,8,9}] [--order_by {desc,asc}]
                [--genre {action,adventure,animation,biography,comedy,crime,documentary,drama,family,fantasy,film-noir,game-show,history,horror,music,musical,mystery,news,reality-tv,romance,sci-fi,sport,talk-show,thriller,war,western}]

Specify input arguments...

optional arguments:
  -h, --help            show this help message and exit
  --most_downloaded     specifier to print the most downloaded movies
  --recently_added      specifier to print the most recently added movies
  --movie_index MOVIE_INDEX
                        specifier to print details about the movie
  --limit LIMIT         specify the number of results. the value must be an
                        integer and also greater than zero (0). by default,
                        it's value is set to 10
  --quality {720p,1080p,3D,All}
                        specifier to filter the results by quality. to be used
                        along with --query_term specifier. by default, it's
                        value is set to 'All'
  --query_term QUERY_TERM
                        specify word to query movies.
  --sort_by {title,year,rating,peers,seeds,download_count,like_count,date_added}
                        specifier to filter results by available sorting
                        methods. to be used along with --query_term specifier.
                        by default, it's value is set to 'date_added'
  --min_rating {0,1,2,3,4,5,6,7,8,9}
                        specifier to filter results by IMDb rating. to be used
                        along with --query_term specifier. by default, it's
                        value is set to '0'
  --order_by {desc,asc}
                        specifier to sort the results by top-bottom or bottom-
                        top. to be used along with --query_term specifier.
                        default is bottom-top
  --genre {action,adventure,animation,biography,comedy,crime,documentary,drama,family,fantasy,film-noir,game-show,history,horror,music,musical,mystery,news,reality-tv,romance,sci-fi,sport,talk-show,thriller,war,western}
                        specifier to filter results by available genres. to be
                        used along with --query_term specifier. by default,
                        it's value is set to 'all'

```

### Examples
```
$ docker run yts-api-v1:latest --most_downloaded --limit 5
sl.no - index_id   - title                                              - year       - imdb_rating     - mpa_rating      - language        - download options
1     - 8462       - Avengers: Infinity War                             - 2018       - 8.5             - PG-13           - English         - ['3D|bluray - 2.39 GB', '720p|bluray - 1.25 GB', '1080p|bluray - 2.39 GB', '720p|web - 1.24 GB', '1080p|web - 2.39 GB']
2     - 7709       - Black Panther                                      - 2018       - 7.3             - PG-13           - English         - ['3D|bluray - 2.16 GB', '720p|bluray - 1.13 GB', '1080p|bluray - 2.17 GB']
3     - 8539       - Deadpool 2                                         - 2018       - 7.7             - R               - English         - ['720p|bluray - 1.11 GB', '1080p|bluray - 2.14 GB', '720p|web - 1.1 GB', '1080p|web - 2.13 GB']
4     - 7025       - Thor: Ragnarok                                     - 2017       - 7.9             - PG-13           - English         - ['3D|bluray - 2.19 GB', '720p|bluray - 1.04 GB', '1080p|bluray - 1.96 GB', '720p|web - 954.46 MB', '1080p|web - 1.98 GB']
5     - 470        - Big Hero 6                                         - 2014       - 7.8             - PG              - English         - ['3D|bluray - 1.65 GB', '720p|bluray - 810.17 MB', '1080p|bluray - 1.65 GB']
```

```
$ docker run yts-api-v1:latest --recently_added --limit 5
sl.no - index_id   - title                                              - year       - imdb_rating     - mpa_rating      - language        - download options
1     - 14344      - Criminal                                           - 2004       - 6.4             - R               - English         - ['720p|web - 770.48 MB', '1080p|web - 1.36 GB']
2     - 14343      - Snow Falling on Cedars                             - 1999       - 6.7             - PG-13           - English         - ['720p|bluray - 1.1 GB', '1080p|bluray - 1.99 GB']
3     - 14342      - House of the Long Shadows                          - 1983       - 6.3             -                 - English         - ['720p|bluray - 870.72 MB', '1080p|bluray - 1.56 GB']
4     - 14341      - The Courier                                        - 2019       - 0               - R               - English         - ['720p|web - 889.04 MB', '1080p|web - 1.56 GB']
5     - 14340      - 3022                                               - 2019       - 0               - R               - English         - ['720p|web - 814.12 MB', '1080p|web - 1.43 GB']
```

```
$ docker run yts-api-v1:latest --query_term "Redemption"
Query Options:
--quality, --sort_by, --min_rating, --genre, --order_by

usage: index.py [-h] [--most_downloaded] [--recently_added]
                [--movie_index MOVIE_INDEX] [--limit LIMIT]
                [--quality {720p,1080p,3D,All}] [--query_term QUERY_TERM]
                [--sort_by {title,year,rating,peers,seeds,download_count,like_count,date_added}]
                [--min_rating {0,1,2,3,4,5,6,7,8,9}] [--order_by {desc,asc}]
                [--genre {action,adventure,animation,biography,comedy,crime,documentary,drama,family,fantasy,film-noir,game-show,history,horror,music,musical,mystery,news,reality-tv,romance,sci-fi,sport,talk-show,thriller,war,western}]

sl.no - index_id   - title                                              - year       - imdb_rating     - mpa_rating      - language        - download options
1     - 13561      - The Combination: Redemption                        - 2019       - 4.2             - R               - English         - ['720p|web - 910.63 MB', '1080p|web - 1.61 GB']
2     - 11736      - Redemption                                         - 2013       - 6.2             - R               - English         - ['720p|bluray - 859.47 MB', '1080p|bluray - 1.61 GB']
3     - 9943       - Unbroken: Path to Redemption                       - 2018       - 5.7             - PG-13           - English         - ['720p|bluray - 837.48 MB', '1080p|bluray - 1.57 GB', '720p|web - 834.16 MB', '1080p|web - 1.57 GB']
4     - 7383       - Redemption Trail                                   - 2013       - 6               -                 - English         - ['720p|web - 763.49 MB', '1080p|web - 1.44 GB']
5     - 4007       - Undisputed 3: Redemption                           - 2010       - 7.4             - R               - English         - ['720p|bluray - 749.61 MB']
6     - 3709       - The Shawshank Redemption                           - 1994       - 9.3             - R               - English         - ['720p|bluray - 848.96 MB', '1080p|bluray - 1.60 GB']
7     - 3701       - The Scorpion King 3: Battle for Redemption         - 2012       - 3.6             - PG-13           - English         - ['720p|bluray - 649.39 MB']
8     - 3651       - The Raid: Redemption                               - 2011       - 7.6             - R               - English         - ['720p|bluray - 796.40 MB', '1080p|bluray - 1.60 GB']
9     - 3521       - The Mark: Redemption                               - 2013       - 3.7             -                 - English         - ['720p|bluray - 750.84 MB', '1080p|bluray - 1.43 GB']
10    - 520        - Blood of Redemption                                - 2013       - 4.4             -                 - English         - ['720p|bluray - 695.82 MB', '1080p|bluray - 1.23 GB']
```

```
$ docker run yts-api-v1:latest --movie_index 3709
-------------------------------------The Shawshank Redemption (1994)--------------------------------------
yts.lt link                   :                         https://yts.tl/movie/the-shawshank-redemption-1994
Movie genre                   :                                                     Action | Crime | Drama
poster                        : https://yts.tl/assets/images/movies/The_Shawshank_Redemption_1994/large-cover.jpg
                                           ~~~~~~~~~~~~~~~~~~~~
Total Downloads: 1197018                            | Likes          :                                1682
MPA rating     : R                                  | IMDb rating    :                                 9.3
Language       : English                            | Year Released  :                                1994
Movie ID       : 3709                               | Runtime (mins) :                                 142
                                           ~~~~~~~~~~~~~~~~~~~~
Synopsis:
Chronicles the experiences of a formerly successful banker as a prisoner in the gloomy jailhouse of
Shawshank after being found guilty of a crime he did not commit. The film portrays the man's unique way of
dealing with his new, torturous life; along the way he befriends a number of fellow prisoners, most
notably a wise long-term inmate named Red.
                                           ~~~~~~~~~~~~~~~~~~~~
Cast:
   |->                             Morgan Freeman ~ AS ~ Ellis Boyd 'Red' Redding                   <-|
   |->                                Tim Robbins ~ AS ~ Andy Dufresne                              <-|
   |->                               Clancy Brown ~ AS ~ Captain Hadley                             <-|
   |->                              Rita Hayworth ~ AS ~ Gilda Mundson Farrell                      <-|
                                           ~~~~~~~~~~~~~~~~~~~~
Download Options:
 Quality: 720p    | Type: bluray          | Seeds:     358 |   Peers: 82              |  Size:  848.96 MB
~~~~~~~~~~~~~~~~ https://yts.tl/torrent/download/AC418DB33FA5CEA4FAB11BC58008FE08F291C9BE ~~~~~~~~~~~~~~~~

 Quality: 1080p   | Type: bluray          | Seeds:     216 |   Peers: 61              |  Size:    1.60 GB
~~~~~~~~~~~~~~~~ https://yts.tl/torrent/download/E0D00667650ABA9EE05AACBBBD8B55EA8A51F534 ~~~~~~~~~~~~~~~~

----------------------------------------------------------------------------------------------------------
```
