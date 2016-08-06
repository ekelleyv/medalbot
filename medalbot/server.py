from flask import Flask, jsonify

from medalbot.get_counts import get_counts, get_counts_by_country_id
from medalbot.slack import get_slack_counts

app = Flask(__name__)


@app.route("/")
def docs():
    return app.send_static_file('endpoints.html')


@app.route("/slack_medals")
def slack_medals():
    """Formatted endpoint to be used as slash command in slack."""
    return get_slack_counts()


@app.route("/api/v1/medals")
def medals():
    return jsonify(get_counts())


@app.route("/api/v1/medals/<country_id>")
def medals_by_country(country_id):
    country_counts = get_counts_by_country_id(country_id)

    if not country_counts:
        response = jsonify({"error_msg": "No medal results found for {0}".format(country_id)})
        response.status_code = 404
        return response

    return jsonify(country_counts)

if __name__ == "__main__":
    app.debug = True
    app.run()
