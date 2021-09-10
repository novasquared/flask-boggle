from flask import Flask, request, render_template, jsonify
from uuid import uuid4

from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {}


@app.get("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.post("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""

    # get a unique string id for the board we're creating
    game_id = str(uuid4())
    print(game_id)
    game = BoggleGame()
    games[game_id] = game

    # use that game which has key of board and pass board as variable into dict below
    # print(game_id, game.board)
    game_info = jsonify(gameId=game_id, board=game.board)

    return game_info
