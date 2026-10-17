# 🐾 Feliz Pet Hospital

A responsive Flask website built for a veterinary clinic in Bengaluru, India. Visitors can learn about the clinic and submit appointment requests, the application records those requests in a Google Sheet for clinic staff.

## 🌐 Live demo

[View the website](https://george12.pythonanywhere.com)

The clinic previously used [felizpethospital.in](https://felizpethospital.in). That domain is currently not live during hosting changes and new features, the link above shows the existing website.

## 🚀 What I built

- Developed mobile and desktop pages for clinic information, blog content, vaccination information, and appointment requests.
- Built Flask routes to display pages and process the appointment form.
- Integrated the Google Sheets API to record submitted contact details, messages, and timestamps for clinic staff.

## 📊 Results

Google Search Console recorded **5,300+ impressions and 170+ clicks over approximately eight months**. The clinic also reported gaining new clients after the website launched. The Search Console figures measure search visibility and clicks; they do not establish how many clients came from the site.

## 🛠️ Tech stack

Python ┃ Flask ┃ HTML ┃ CSS ┃ JavaScript ┃ Google Sheets API ┃ PythonAnywhere

## 💻 Run locally

1. Clone the repository and create a virtual environment:

   ```bash
   git clone https://github.com/george-robin/feliz-pet-hospital.git
   cd feliz-pet-hospital
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure your own Google Sheets API credentials and spreadsheet ID for the appointment integration. Do not commit a service-account key or your `.env` file. The application currently expects a service-account JSON file at the filename specified in `app.py`.

4. Start the development server:

   ```bash
   python app.py
   ```

   Open **http://127.0.0.1:8080**.

## 📈 Planned roadmap

- Replace Google Sheets appointment storage with a MySQL database.
- Improve form validation and handling of Google Sheets API errors.
- Explore appointment confirmation emails/whatsapp messages.
