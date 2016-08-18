from tabulate import tabulate

from medalbot.get_counts import get_counts, get_counts_by_country_id


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

    india_count = get_counts_by_country_id("india")
    response_table.append([
        india_count["place"],
        india_count["country_name"],
        india_count["gold_count"],
        india_count["silver_count"],
        india_count["bronze_count"],
        india_count["total_count"]
    ])

    # Use block so things align
    return "```{0}```".format(tabulate(response_table, headers))
