"""
Flask will look for the folders called "templates" and "static" in the root folder of the project automatically.

You can change the name of the folders Flask looks for by doing:
app = Flask(__name__, template_folder="other_templates", static_folder="other_static")
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# importing module
from routes import all_routes

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)


# Model for database
class Example(db.Model):
    example_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"<Example {self.name}>"


with app.app_context():
    db.create_all()

# Passing app above to all_routes function in routes.py module
all_routes(app)

if __name__ == "__main__":
    app.run()
