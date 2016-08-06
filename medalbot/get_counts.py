from cachetools.func import ttl_cache
import requests

from medalbot.config import EXTRACTION_URL


def _country_name_to_id(country_name):
    return "-".join(country_name.lower().split(" "))


def format_extraction_response(raw_response):
    medal_count_list = []

    for country in raw_response["extractorData"]["data"][0]["group"]:
        country_name = country["Country value"][0]["text"]
        country_data = {
            "id": _country_name_to_id(country_name),
            "place": int(country["Place"][0]["text"]),
            "country_name": country_name,
            "gold_count": int(country["Gold number"][0]["text"]),
            "silver_count": int(country["Silver number"][0]["text"]),
            "bronze_count": int(country["Bronze number"][0]["text"]),
            "total_count": int(country["Total number"][0]["text"]),

        }

        medal_count_list.append(country_data)

    return medal_count_list


def get_counts_by_country_id(country_id):
    counts = get_counts()
    for count_data in counts:
        if count_data["id"] == country_id:
            return count_data

    return None


@ttl_cache(ttl=300)
def get_counts():
    """
    Gets formatted medal counts.

    Cached because the import.io url is slow and I don't want to
    have to buy a paid plan.
    """
    raw_response = requests.get(EXTRACTION_URL).json()
    return format_extraction_response(raw_response)


if __name__ == '__main__':
    print get_counts()
