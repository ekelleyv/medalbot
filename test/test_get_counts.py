import json

from nose.tools import assert_equals

from medalbot.get_counts import format_extraction_response


def test_format_response():
    raw_response = json.loads(EXAMPLE_RESPONSE)
    count_response = format_extraction_response(raw_response)

    assert_equals(FORMATTED_RESPONSE, count_response)

FORMATTED_RESPONSE = [
    {
        "id": "china",
        "place": 1,
        "country_name": "China",
        "gold_count": 0,
        "silver_count": 1,
        "bronze_count": 1,
        "total_count": 2
    },
    {
        "id": "united-states",
        "place": 2,
        "country_name": "United States",
        "gold_count": 1,
        "silver_count": 0,
        "bronze_count": 0,
        "total_count": 1
    }
]


EXAMPLE_RESPONSE = """
{
  "extractorData" : {
    "url" : "http://www.nbcolympics.com/medals",
    "resourceId" : "18ead6ba7867e1b36ae0bfde721462c2",
    "data" : [ {
      "group" : [ {
        "Place" : [ {
          "text" : "1"
        } ],
        "Country image" : [ {
          "src" : "http://assets.rio2016.nbcolympics.com/country-flags/52x35/CHN.png",
          "alt" : "China"
        } ],
        "Country value" : [ {
          "text" : "China"
        } ],
        "Gold number" : [ {
          "text" : "0"
        } ],
        "Silver number" : [ {
          "text" : "1"
        } ],
        "Bronze number" : [ {
          "text" : "1"
        } ],
        "Total number" : [ {
          "text" : "2"
        } ]
      }, {
        "Place" : [ {
          "text" : "2"
        } ],
        "Country image" : [ {
          "src" : "http://assets.rio2016.nbcolympics.com/country-flags/52x35/USA.png",
          "alt" : "United States"
        } ],
        "Country value" : [ {
          "text" : "United States"
        } ],
        "Gold number" : [ {
          "text" : "1"
        } ],
        "Silver number" : [ {
          "text" : "0"
        } ],
        "Bronze number" : [ {
          "text" : "0"
        } ],
        "Total number" : [ {
          "text" : "1"
        } ]
      } ]
    } ]
  },
  "pageData" : {
    "statusCode" : 200,
    "timestamp" : 1470503398334
  }
}
"""
