##############################################################################
#   Helena Chi 2020
#   Rethink URL Shortener Challenge
##############################################################################

import json
import requests
import zlib
from urllib.parse import urlparse

DIRECTORY_FILE = "directory.json"
SHORTENED_HEADER = "https://hele.na/"
ENCODING = "utf-8"

CDIRECTORY = {}
CCOUNTER = 0
with open(DIRECTORY_FILE, "r") as openfile:
  data = json.load(openfile)
  CDIRECTORY = data["directory"]
  CCOUNTER = data["counter"]


# isValid
#
# RETURNS whether or not the given url leads to an existing webpage
#
# Parameters
# ----------
# input_url: str
#   the url to check validity
#
# Returns
# -------
# bool
def isValid(input_url):
  request = requests.get(input_url)
  return request.status_code == 200

# shortenedURLFormatter
#
# RETURNS a url formatted with the shortened header and unique id, which is obtained
#   by using the Adler-32 checksum algorithm on the given url and its incremented id.
#
# Parameters
# ----------
# input_url: str
#   the url to shorten
#
# Returns
# -------
# str
#   the complete url in shortened format
def shortnenedURLFormatter(input_url):
  input_str = str(CCOUNTER) + input_url
  adlered = zlib.adler32(bytearray(input_str, ENCODING))
  return SHORTENED_HEADER + str(adlered)

# shorten
#
# RETURNS the shortened url for the input url's entry in the directory
#
# Parameters
# ----------
# input_url: str
#   the url to shorten
#
# Returns
# -------
# str:
#   a formatted shortened url
def shorten(input_url) :
  if (input_url in CDIRECTORY):
    return CDIRECTORY[input_url]
  else:
    new_directory = CDIRECTORY
    new_directory[input_url] = shortnenedURLFormatter(input_url)
    new_counter = CCOUNTER + 1
    new_data = { 
        "counter": new_counter,
        "directory": new_directory
      }
    with open(DIRECTORY_FILE, "w") as outfile:
      json.dump(new_data, outfile)
    return new_directory[input_url]


if __name__ == "__main__":
  input_url = input("Pass in the url you want shortened (eg: \"https://www.google.com\", \"https://www.youtube.com/user/crashcourse\"):\n")
  if (isValid(input_url)):
    print("Your shortened url is: ", shorten(input_url))
  else:
    print("Your url is not valid, please enter a valid url.")
