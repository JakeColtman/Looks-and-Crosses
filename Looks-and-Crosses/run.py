from flask import Flask, jsonify
from Connections.Redshift import RedshiftConnection
from Game import Game

import os

app = Flask(__name__)


@app.route("/<string:update_info>", methods=["GET"])
def update(update_info):
    print(update_info)
    game.update_position(update_info[0], update_info[1])
    return jsonify({"Status":True})

if __name__ == "__main__":
    conn_string = os.environ.get("REDSHIFT_CONN_STRING")
    table = "looks_and_crosses"
    schema = "tests"

    game = Game(RedshiftConnection(conn_string), schema, table)
    app.run(debug=True)