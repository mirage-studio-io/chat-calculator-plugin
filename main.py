import os
import math
import quart
import quart_cors
from quart import Quart, jsonify, request

PORT = 5002
# Get authentication key from environment variable
SERVICE_AUTH_KEY = os.environ.get("SERVICE_AUTH_KEY")

# Create a Quart app and enable CORS
app = quart_cors.cors(Quart(__name__),
                      allow_origin=[
                        f"http://localhost:{PORT}",
                        "https://chat.openai.com",
                      ])

# Add a before_request hook to check for authorization header
# @app.before_request
# def assert_auth_header():
#   auth_header = request.headers.get("Authorization")
#   print(auth_header)
#   # check if the header is missing or incorrect, and return an error if needed
#   if not auth_header or auth_header != f"Bearer {SERVICE_AUTH_KEY}":
#     return jsonify({"error": "Unauthorized"}), 401


# Add a route to perform addition
@app.route("/calculator/add/<float:a>/<float:b>", methods=["GET"])
async def add(a, b):
  result = a + b
  return jsonify({"result": result})


# Add a route to perform subtraction
@app.route("/calculator/subtract/<float:a>/<float:b>", methods=["GET"])
async def subtract(a, b):
  result = a - b
  return jsonify({"result": result})


# Add a route to perform multiplication
@app.route("/calculator/multiply/<float:a>/<float:b>", methods=["GET"])
async def multiply(a, b):
  result = a * b
  return jsonify({"result": result})


# Add a route to perform division
@app.route("/calculator/divide/<float:a>/<float:b>", methods=["GET"])
async def divide(a, b):
  if b == 0:
    return jsonify({"error": "Division by zero is not allowed"}), 400
  result = a / b
  return jsonify({"result": result})


# Add a route to find the power of a number
@app.route("/calculator/power/<float:a>/<float:b>", methods=["GET"])
async def power(a, b):
  result = math.pow(a, b)
  return jsonify({"result": result})


# Add a route to find the square root of a number
@app.route("/calculator/sqrt/<float:a>", methods=["GET"])
async def sqrt(a):
  if a < 0:
    return jsonify(
      {"error": "Square root of negative numbers is not supported"}), 400
  result = math.sqrt(a)
  return jsonify({"result": result})
  

@app.get("/logo.png")
async def plugin_logo():
  filename = 'logo.png'
  return await quart.send_file(filename, mimetype='image/png')


@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
  host = request.headers['Host']
  with open("manifest.json") as f:
    text = f.read()
    text = text.replace("PLUGIN_HOSTNAME", f"https://{host}")
    return quart.Response(text, mimetype="text/json")


@app.get("/openapi.yaml")
async def openapi_spec():
  host = request.headers['Host']
  with open("openapi.yaml") as f:
    text = f.read()
    text = text.replace("PLUGIN_HOSTNAME", f"https://{host}")
    return quart.Response(text, mimetype="text/yaml")


@app.get("/openapi.json")
async def openapi_spec_json():
  host = request.headers['Host']
  with open("openapi.json") as f:
    text = f.read()
    text = text.replace("PLUGIN_HOSTNAME", f"https://{host}")
    return quart.Response(text, mimetype="text/json")


def main():
  app.run(debug=True, host="0.0.0.0", port=PORT)


if __name__ == "__main__":
  main()
