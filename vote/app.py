from flask import Flask, render_template_string, request, redirect, url_for
import redis
import os
import socket

app = Flask(__name__)

# Redis config
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

HTML = """
<!doctype html>
<title>Vote App</title>
<h1>Vote for your favorite!</h1>
<p>Container: {{ hostname }}</p>

<form method="POST">
  <button type="submit" name="vote" value="Cats">🐱 Cats</button>
  <button type="submit" name="vote" value="Dogs">🐶 Dogs</button>
</form>

<h2>Results</h2>
<ul>
  <li>Cats: {{ cats }}</li>
  <li>Dogs: {{ dogs }}</li>
</ul>
"""

@app.route("/", methods=["GET", "POST"])
def vote():
    if request.method == "POST":
        vote = request.form.get("vote")
        if vote:
            r.incr(vote)
        return redirect(url_for("vote"))

    cats = r.get("Cats") or 0
    dogs = r.get("Dogs") or 0

    return render_template_string(
        HTML,
        cats=cats,
        dogs=dogs,
        hostname=socket.gethostname()
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
