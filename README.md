# Music Backend API

Backend service for managing users, tracks, and playlists with authentication and full CRUD functionality. Built using **FastAPI**, **MongoDB**, and **Docker**.

---

## 🚀 Overview

- RESTful API design  
- JWT-based authentication  
- NoSQL data modeling with MongoDB  
- Containerized services using Docker  

---

## ⚙️ Tech Stack

- **Backend:** FastAPI (Python)
- **Database:** MongoDB (Beanie ODM, Motor)
- **Authentication:** JWT + bcrypt
- **Infrastructure:** Docker, Docker Compose
- **Docs:** Swagger UI

---

## 📂 Project Structure

```bash
app/
├── core/        # Configuration
├── models/      # Database models
├── routers/     # API routes
├── schemas/     # Request/response schemas
└── main.py      # Entry point
```

---

## 🛠 Running Locally

```bash
# Clone repo
git clone https://github.com/your-username/music-backend.git
cd music-backend

# Setup environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start services
docker compose up -d mongo elasticsearch

# Run server
uvicorn app.main:app --reload
```

---

## 📖 API Docs

Open:
```
http://127.0.0.1:8000/docs
```

---

## 🔐 Security

- Passwords hashed using bcrypt  
- JWT-based authentication  
- Secrets stored in `.env`  

---

## 👨‍💻 Author

**Vaibhav Rikhy**  
[LinkedIn](https://www.linkedin.com/in/vaibhavrikhy/)
