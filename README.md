# Student Management Backend

A beginner-friendly Student Management Backend System built using Flask, SQLAlchemy, and MySQL.

---

# Features

- Create Student
- Get All Students
- Get Single Student
- Update Student
- Delete Student
- Gmail Validation
- Branch Validation
- Age Validation

---

# Tech Stack

- Python
- Flask
- SQLAlchemy
- MySQL
- Postman

---

# Project Structure

backend/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── config.py
│   ├── database.py
│   └── main.py
│
├── requirements.txt
├── run.py
└── README.md

---

# Installation

```bash
git clone https://github.com/chethan-kumar-021/student-management-backend.git
```

```bash
cd student-management-backend
```

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

---

# Configure Environment Variable

Create `.env`

```env
DATABASE_URL=mysql+pymysql://root:yourpassword@localhost/student_db
```

---

# Run Application

```bash
python run.py
```

Server:

```text
http://127.0.0.1:5000
```

---

# API Endpoints

| Method | Endpoint       | Description        |
|--------|----------------|--------------------|
| POST   | /students      | Create Student     |
| GET    | /students      | Get All Students   |
| GET    | /students/<id> | Get Single Student |
| PUT    | /students/<id> | Update Student     |
| DELETE | /students/<id> | Delete Student     |

---

# Author

Chethan Kumar