from flask import Flask, render_template, request, redirect
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
load_dotenv()

app = Flask(__name__)

# Google Sheets setup
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = "feliz-pet-hopsital-4954b2987afa.json"

# Create credentials + client
creds = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)
client = gspread.authorize(creds)

SHEET_ID = os.getenv("SHEET_ID")
sheet = client.open_by_key(SHEET_ID).sheet1


# Home page
@app.route("/")
def home():
    return render_template("index.html")

# About page
@app.route("/about")
def about():
    return render_template("about.html")

# Book an Appointment
@app.route("/appointment", methods=["GET", "POST"])
def appointment():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        message = request.form["message"]

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.append_row([timestamp, name, phone, message])

        return redirect("/success")

    return render_template("appointment.html")

# Success page
@app.route("/success")
def success():
    return render_template("thank.html")

# Blogs
@app.route("/blogs")
def blog():
    return render_template("blog.html")

@app.route("/vac")
def vac():
    return render_template("vac.html")


if __name__ == "__main__":
    app.run(debug=True, port = 8080)
