from tabulate import tabulate

from medalbot.get_counts import get_counts


def get_slack_counts():
    counts = get_counts()[:10]
    headers = ["#", "Country", "Gold", "Silver", "Bronze", "Total"]
    response_table = []

    for count in counts:
        response_table.append([
            count["place"],
            count["country_name"],
            count["gold_count"],
            count["silver_count"],
            count["bronze_count"],
            count["total_count"]
        ])

    return tabulate(response_table, headers)
