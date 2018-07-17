#! python3
# weather.py - Open browser to show weather using a zip code from the
# command line or current location.

import webbrowser, sys, geocoder
if len(sys.argv) > 1:
    # Get address from command line.
    zipcode = ' '.join(sys.argv[1:])
else:
    # Get current location.
    g = geocoder.ip('me')
    zipcode = g.postal

# Open weather web page.
webbrowser.open('https://weather.com/weather/today/l/' + zipcode)