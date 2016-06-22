# make sure to install dependencies with pip
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2


# constants
API_KEY = ""  # your api key here
API_URL = ""  # the api url here (as described here: http://tooso.ai/Developers.aspx)
API_METHOD = "Index/index"  # the endpoint
CATALOG_FILE = ""  # the file path to the zip csv catalog file to be uploaded


def main():
    register_openers()
    # prepare data
    datagen, headers = multipart_encode({"catalogue": open(CATALOG_FILE, "rb")})
    # compose final url
    final_url = "{0}/{1}/{2}".format(API_URL, API_KEY, API_METHOD)
    # make the request
    request = urllib2.Request(final_url, datagen, headers)
    response = urllib2.urlopen(request).read()
    # print json response in console
    print response


if __name__ == "__main__":
    main()