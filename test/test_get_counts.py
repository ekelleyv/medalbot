# -*- coding: utf-8 -*-

import json

from nose.tools import assert_equals

from medalbot.get_counts import format_extraction_response


def test_format_response():
    ustr_to_load = unicode(EXAMPLE_RESPONSE, 'latin-1')
    raw_response = json.loads(ustr_to_load)
    count_response = format_extraction_response(raw_response)

    assert_equals(FORMATTED_RESPONSE_FIRST, count_response[0])

FORMATTED_RESPONSE_FIRST = {
    "id": "australia",
    "place": 1,
    "country_name": "Australia",
    "gold_count": 2,
    "silver_count": 0,
    "bronze_count": 1,
    "total_count": 3
}


EXAMPLE_RESPONSE = """
{
  "extractorData" : {
    "url" : "https://www.google.com/search?q=medal+count&oq=medal+count&gs_l=serp.3..0i71l8.3974.4133.0.4342.2.2.0.0.0.0.0.0..0.0....0...1c.1.64.serp..2.0.0.WgaO4zL3wF4#mie=oly%2C%5B%22%2Fm%2F03tnk7%22%2C1%2C%22m%22%2C1%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C0%5D",
    "resourceId" : "04e71ea60a4bf15a9328d3e4420b282b",
    "data" : [ {
      "group" : [ {
        "Rank" : [ {
          "text" : "1"
        } ],
        "Country" : [ {
          "text" : "Australia"
        } ],
        "Gold" : [ {
          "text" : "2"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "1"
        } ],
        "Total" : [ {
          "text" : "3"
        } ]
      }, {
        "Rank" : [ {
          "text" : "2"
        } ],
        "Country" : [ {
          "text" : "Hungary"
        } ],
        "Gold" : [ {
          "text" : "2"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "2"
        } ]
      }, {
        "Rank" : [ {
          "text" : "3"
        } ],
        "Country" : [ {
          "text" : "United States"
        } ],
        "Gold" : [ {
          "text" : "1"
        } ],
        "Silver" : [ {
          "text" : "4"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "5"
        } ]
      }, {
        "Rank" : [ {
          "text" : "4"
        } ],
        "Country" : [ {
          "text" : "South Korea"
        } ],
        "Gold" : [ {
          "text" : "1"
        } ],
        "Silver" : [ {
          "text" : "1"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "2"
        } ]
      }, {
        "Rank" : [ {
          "text" : "5"
        } ],
        "Country" : [ {
          "text" : "Japan"
        } ],
        "Gold" : [ {
          "text" : "1"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "4"
        } ],
        "Total" : [ {
          "text" : "5"
        } ]
      }, {
        "Rank" : [ {
          "text" : "6"
        } ],
        "Country" : [ {
          "text" : "Argentina"
        } ],
        "Gold" : [ {
          "text" : "1"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "1"
        } ]
      }, {
        "Rank" : [ {
          "text" : "6"
        } ],
        "Country" : [ {
          "text" : "Belgium"
        } ],
        "Gold" : [ {
          "text" : "1"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "1"
        } ]
      }, {
        "Rank" : [ {
          "text" : "6"
        } ],
        "Country" : [ {
          "text" : "Russia"
        } ],
        "Gold" : [ {
          "text" : "1"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "1"
        } ]
      }, {
        "Rank" : [ {
          "text" : "6"
        } ],
        "Country" : [ {
          "text" : "Thailand"
        } ],
        "Gold" : [ {
          "text" : "1"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "1"
        } ]
      }, {
        "Rank" : [ {
          "text" : "6"
        } ],
        "Country" : [ {
          "text" : "Vietnam"
        } ],
        "Gold" : [ {
          "text" : "1"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "1"
        } ]
      }, {
        "Rank" : [ {
          "text" : "11"
        } ],
        "Country" : [ {
          "text" : "China"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "2"
        } ],
        "Bronze" : [ {
          "text" : "3"
        } ],
        "Total" : [ {
          "text" : "5"
        } ]
      }, {
        "Rank" : [ {
          "text" : "12"
        } ],
        "Country" : [ {
          "text" : "Italy"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "1"
        } ],
        "Bronze" : [ {
          "text" : "1"
        } ],
        "Total" : [ {
          "text" : "2"
        } ]
      }, {
        "Rank" : [ {
          "text" : "12"
        } ],
        "Country" : [ {
          "text" : "Kazakhstan"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "1"
        } ],
        "Bronze" : [ {
          "text" : "1"
        } ],
        "Total" : [ {
          "text" : "2"
        } ]
      }, {
        "Rank" : [ {
          "text" : "14"
        } ],
        "Country" : [ {
          "text" : "Brazil"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "1"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "1"
        } ]
      }, {
        "Rank" : [ {
          "text" : "14"
        } ],
        "Country" : [ {
          "text" : "Denmark"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "1"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "1"
        } ]
      }, {
        "Rank" : [ {
          "text" : "14"
        } ],
        "Country" : [ {
          "text" : "Indonesia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "1"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "1"
        } ]
      }, {
        "Rank" : [ {
          "text" : "17"
        } ],
        "Country" : [ {
          "text" : "Canada"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "1"
        } ],
        "Total" : [ {
          "text" : "1"
        } ]
      }, {
        "Rank" : [ {
          "text" : "17"
        } ],
        "Country" : [ {
          "text" : "Spain"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "1"
        } ],
        "Total" : [ {
          "text" : "1"
        } ]
      }, {
        "Rank" : [ {
          "text" : "17"
        } ],
        "Country" : [ {
          "text" : "Poland"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "1"
        } ],
        "Total" : [ {
          "text" : "1"
        } ]
      }, {
        "Rank" : [ {
          "text" : "17"
        } ],
        "Country" : [ {
          "text" : "Uzbekistan"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "1"
        } ],
        "Total" : [ {
          "text" : "1"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Benin"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "American Samoa"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Afghanistan"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Aruba"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Burkina Faso"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Andorra"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Belize"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Armenia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Mali"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Malaysia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Bangladesh"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Refugee Olympic Athletes"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "British Virgin Islands"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Brunei"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Kiribati"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Liberia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Papua New Guinea"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Seychelles"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Marshall Islands"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Somalia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Iraq"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Sierra Leone"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "South Sudan"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Gambia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "United Arab Emirates"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "FYR Macedonia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Ghana"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Cameroon"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Congo"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Bhutan"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Cook Islands"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Comoros"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Georgia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Guinea-Bissau"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Central African Republic"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Cape Verde"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Jordan"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Great Britain"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Equatorial Guinea"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Guinea"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Micronesia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "DR Congo"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Chad"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Guyana"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Cambodia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Malta"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Sao Tome & Principe"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Togo"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Haiti"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Samoa"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Tonga"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Mauritania"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Maldives"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Swaziland"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Libya"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Suriname"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Nicaragua"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Tuvalu"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Senegal"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Nepal"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Lebanon"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Madagascar"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Solomon Islands"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Vanuatu"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Pakistan"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "St Vincent & the Grenadines"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Cayman Islands"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Niger"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Uruguay"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Palestine"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Hong Kong, China"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Malawi"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Syria"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Liechtenstein"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Monaco"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Mozambique"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Montenegro"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Sudan"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Turkmenistan"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Laos"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Honduras"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Rwanda"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Kyrgyzstan"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "South Africa"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Tanzania"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Palau"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Timor-Leste"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Yemen"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Independent Olympic Athletes"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Dominica"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Nauru"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Oman"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Guam"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Netherlands"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Germany"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Ireland"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "France"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Belarus"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "India"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Serbia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Slovakia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Sweden"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Bulgaria"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Norway"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Portugal"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Cyprus"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Guatemala"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Singapore"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Tunisia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Croatia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Ukraine"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Lithuania"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Finland"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Turkey"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Slovenia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Estonia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Mexico"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Greece"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Israel"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Switzerland"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Egypt"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Austria"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Colombia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Cuba"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Ecuador"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Kosovo"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "North Korea"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "El Salvador"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Dominican Republic"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Czech Republic"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "New Zealand"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "US Virgin Islands"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Chinese Taipei"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Iran"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Ethiopia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Qatar"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Bahamas"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "San Marino"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Angola"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Costa Rica"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Azerbaijan"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Mongolia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Myanmar"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Kenya"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Moldova"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Morocco"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Venezuela"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Chile"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Peru"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Sri Lanka"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Puerto Rico"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Paraguay"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Romania"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Saint Kitts & Nevis"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Lesotho"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Eritrea"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Zimbabwe"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Botswana"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Jamaica"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Uganda"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Namibia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Bahrain"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Burundi"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Trinidad & Tobago"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Latvia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Bolivia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Nigeria"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Algeria"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Fiji"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Mauritius"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Iceland"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Zambia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Côte d'Ivoire"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Gabon"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Antigua & Barbuda"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Albania"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Djibouti"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Saudi Arabia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Panama"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Philippines"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Luxembourg"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Tajikistan"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Bosnia & Herzegovina"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Saint Lucia"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Grenada"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Barbados"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      }, {
        "Rank" : [ {
          "text" : "-"
        } ],
        "Country" : [ {
          "text" : "Bermuda"
        } ],
        "Gold" : [ {
          "text" : "0"
        } ],
        "Silver" : [ {
          "text" : "0"
        } ],
        "Bronze" : [ {
          "text" : "0"
        } ],
        "Total" : [ {
          "text" : "0"
        } ]
      } ]
    } ]
  },
  "pageData" : {
    "statusCode" : 200,
    "timestamp" : 1470539802828
  }
}
"""
