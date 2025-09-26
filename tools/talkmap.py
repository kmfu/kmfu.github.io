

# # Leaflet cluster map of talk locations
#
# (c) 2016-2017 R. Stuart Geiger, released under the MIT license
#
# Run this from anywhere; the script reads markdown files from content/_talks/
# and scrapes the location YAML field from each .md file, geolocating it with
# geopy/Nominatim. It then uses the getorg library to output data, HTML,
# and Javascript for a standalone cluster map under tools/talkmap/.
#
# Requires: glob, getorg, geopy

from pathlib import Path

import getorg
from geopy import Nominatim


REPO_ROOT = Path(__file__).resolve().parents[1]
TALKS_DIR = REPO_ROOT / "content" / "_talks"
OUTPUT_DIR = REPO_ROOT / "tools" / "talkmap"


geocoder = Nominatim()
location_dict = {}
location = ""
permalink = ""
title = ""


for file in TALKS_DIR.glob("*.md"):
    with open(file, 'r') as f:
        lines = f.read()
        if lines.find('location: "') > 1:
            loc_start = lines.find('location: "') + 11
            lines_trim = lines[loc_start:]
            loc_end = lines_trim.find('"')
            location = lines_trim[:loc_end]
                            
           
        location_dict[location] = geocoder.geocode(location)
        print(location, "\n", location_dict[location])


m = getorg.orgmap.create_map_obj()
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
getorg.orgmap.output_html_cluster_map(location_dict, folder_name=str(OUTPUT_DIR), hashed_usernames=False)



