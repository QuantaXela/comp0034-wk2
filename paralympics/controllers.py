from flask import current_app as app

@app.route('/')
def hello():
  return f"Hello!"

if __name__ == "__main__":
    app.run(debug=True)