from flask import Flask, request, redirect
import redis
import os
import socket

app = Flask(__name__)

# Redis connection
redis_host = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=redis_host, port=6379)

option_a = os.getenv("OPTION_A", "Cats")
option_b = os.getenv("OPTION_B", "Dogs")
hostname = socket.gethostname()

@app.route("/", methods=["GET", "POST"])
def vote():
    if request.method == "POST":
        vote = request.form["vote"]
        r.rpush("votes", vote)
        return redirect("/")

    return f"""
    <h2>Vote App</h2>
    <form method="POST">
        <button name="vote" value="{option_a}">{option_a}</button>
        <button name="vote" value="{option_b}">{option_b}</button>
    </form>
    <p>Served by: {hostname}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
