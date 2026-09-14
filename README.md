# 🐾 Feliz Pet Hospital Web Platform

A full-stack web application designed and deployed for **Feliz Pet Hospital** (Veterinary Clinic, Bangalore). This platform bridges the gap between pet owners and clinic administration by automating customer onboarding and backend appointment logging.

## 🚀 Impact & Performance Metrics
* **Client Engagement:** Generated **5,000+ unique digital views** during the launch phase.
* **Business Outcomes:** Directly drove **multiple new client acquisitions** for the hospital.
* **Process Automation:** Eliminated manual booking friction by connecting web inputs directly to administrative schedules.

---

## 🛠️ Tech Stack & Architecture

| Layer | Technologies Used | Description |
| :--- | :--- | :--- |
| **Frontend** | HTML5, CSS3, JavaScript | Responsive user interface tailored for seamless desktop and mobile navigation. |
| **Backend** | Python, Flask | Robust routing logic, clean request handling, and dynamic template rendering. |
| **Database/Automation** | Google Sheets API | Serves as a live administrative ledger to securely sync and store booking records. |
| **Version Control** | Git, GitHub | Managed deployment branches and clean production asset pipelines. |

---

## ✨ Core Features

* **Full-Stack Form Processing:** Captures customer detail payloads securely through custom frontend interfaces.
* **Google Sheets Automation Bot:** Uses backend Python scripts and service account keys to append booking data to internal spreadsheets in real-time.
* **Dynamic Route Management:** Implements organized, clean URL patterns via Flask blueprints to ensure maximum site stability.

---

## 💻 Local Setup & Installation

To run this project locally on your machine, follow these simple steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd feliz-pet-hospital
   ```

2. **Set up a Python Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install flask google-auth google-api-python-client
   ```

4. **Run the local development server:**
   ```bash
   python app.py
   ```
   Open `http://127.0.0` in your web browser.

---

## 📈 Upcoming Roadmap
- [ ] Migrate the Google Sheets backend data ledger to a native **MySQL relational database**.
- [ ] Implement secure student and administrative portal authentications.
- [ ] Add real-time automated email confirmations for successfully processed bookings.
