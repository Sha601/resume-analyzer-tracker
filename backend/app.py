from flask import Flask, render_template, request
from routes import views
import os
from tracker.database import init_db 

init_db()

app = Flask(__name__)
app.register_blueprint(views)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
