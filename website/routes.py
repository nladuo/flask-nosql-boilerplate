from website import app, mongo, redis


@app.route("/")
def hello():
    if mongo.db.users.find({}).count() == 0:
        mongo.db.users.insert({"name": "Hello World"})
    return mongo.db.users.find_one()["name"]

