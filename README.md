# Looks-and-Crosses

This is a proof of concept design of how Looker can be used for bi-directional communication with the help of a webserver.  Not recommended for production Tic Tac Toe :)

More serious implementations of the design include:

* allowing users to mark companies
* correcting data in databases
* MMO Battleships 

### How does it work

Looker allows you to use custom HTML in fields like 

```
  html: |
    <a href="http://localhost:5000/{{ value }}" target="_new"><span style='color:green'>{{ value }}</span></a>
```

Pretty useful for linking to external sources, but not much else right?  Wrong.  If we set up a webserver and populate each cell with a unique idenitifer, then clicking on the link acts as a REST call to the server with unique parameters.  This can be picked up by soemthing like

``` python
@app.route("/<string:update_info>", methods=["GET"])
def update(update_info):
    game.update_position(update_info[0], update_info[1])
    return jsonify({"Success":True})
```

### How to install

1 - Add the model and view in the repo to your looker instance 

2 - Add your connection details to `run.py`

3 - Run `run.py`

4 - Explore looksandcrosses

### How to play

Take turns clicking on the square you want to play.  After each turn you will need to refresh the cache.  The game will naturally iterated between x and os.  The winner is the first with three in a row.

When the game is over, you will need to restart the web server to play again
