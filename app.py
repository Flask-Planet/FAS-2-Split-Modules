from flask import Flask

# importing module
from routes import all_routes

app = Flask(__name__)
"""
Flask will look for the folders called "templates" and "static" in the root folder of the project automatically.

You can change the name of the folders Flask looks for by doing:
app = Flask(__name__, template_folder="other_templates", static_folder="other_static")
"""

# Passing app above to all_routes function in routes.py module
all_routes(app)

if __name__ == "__main__":
    app.run()
