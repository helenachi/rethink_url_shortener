# Rethink URL Shortener Challenge [Helena Chi]

A python program that shortens a given valid url.


To run:

- Clone or download this repo and `cd rethink_url_shortener`
- Run `python3 shortener.py`
- Enter a valid url


Assumptions:

- JSON file initialized to `{ "counter": 0, "directory": {} }` and gets updated every time you run shortener.py
- The shortened url will not actually redirect to the given url input if entered in a browser
- Input URL must be copied and pasted from the url bar in your preferred browser. (i.e. https://www.google.com/)
- Will not return result for URL's to nonexistent webpages.


Limitations:

- The format of the shortened URL will be: `https://hele.na/` + `[an 8-10 digit number]`, and this may be longer than some inputs 

Helena Chi