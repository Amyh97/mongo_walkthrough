import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "task_manager"
app.config["MONGO_URI"] = "mongodb+srv://avhollis97:Re67Whj@myfirstcluster.cz5rs.mongodb.net/task_manager?retryWrites=true&w=majority"

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    return render_template("tasks.html", tasks=mongo.db.tasks.find())

@app.route("/add_tasks")
def add_task():
    return render_template("addtasks.html",
                            categories =mongo.db.categories.find())


@app.route("/insert_task", methods=["POST"])
def insert_task():
    tasks =mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
