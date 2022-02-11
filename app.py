from flask import Flask, render_template
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host=os.environ.get("REDIS_HOST", "redis"), db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
  try:
    visits = redis.incr("counter")
  except RedisError:
    visits = "cannot connect to Redis, counter disabled"

  return render_template("index.html", name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

@app.route("/version")
def version():
  return render_template("version.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
