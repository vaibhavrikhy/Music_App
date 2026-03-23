🎵 Music Backend API (FastAPI + MongoDB + Docker)

A scalable backend service for managing music data including users, tracks, and playlists. Built using FastAPI, MongoDB (NoSQL), and Docker, with JWT-based authentication and full CRUD support.

🚀 Features

🔐 User Authentication (Signup & Login with JWT)

🎧 Track Management (Create, Read, Delete)

📁 Playlist Management

⚡ FastAPI with async support

🗄 MongoDB (NoSQL) using Beanie ODM

🐳 Dockerized services (MongoDB + Elasticsearch)

📄 Interactive API docs with Swagger UI

🛠 Tech Stack

Backend: FastAPI (Python)

Database: MongoDB (Beanie ODM, Motor)

Search (optional): Elasticsearch

Auth: JWT + bcrypt (passlib)

Containerization: Docker & Docker Compose

📂 Project Structure
Musicapp/
├── app/
│   ├── core/        # Config & settings
│   ├── models/      # MongoDB models (User, Track, Playlist)
│   ├── routers/     # API routes (auth, tracks, playlists)
│   ├── schemas/     # Request/response schemas (optional)
│   ├── main.py      # FastAPI entry point
│   └── __init__.py
├── docker-compose.yml
├── .env
├── .gitignore
└── README.md
⚙️ Setup & Run Locally
1️⃣ Clone the repository
git clone https://github.com/your-username/music-backend.git
cd music-backend
2️⃣ Create virtual environment
python3 -m venv .venv
source .venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Start Docker services
docker compose up -d mongo elasticsearch
5️⃣ Run the backend server
uvicorn app.main:app --reload
📖 API Documentation

Once running, access Swagger UI:

👉 http://127.0.0.1:8000/docs

🔑 Example API Flow
Signup
POST /auth/signup
Create Track
POST /tracks/
Get Tracks
GET /tracks/
Delete Track
DELETE /tracks/{track_id}
📸 Demo Screenshots
Swagger Overview

Authentication (Signup)

Track CRUD




🔐 Security Notes

Passwords are hashed using bcrypt

JWT tokens are used for authentication

Environment variables are stored in .env (not committed)

🧠 Key Learnings

Building RESTful APIs using FastAPI

Working with NoSQL databases (MongoDB)

Structuring scalable backend architecture

Implementing authentication and security

Dockerizing backend services

📌 Future Improvements

Add PUT/UPDATE endpoints

Integrate Elasticsearch search endpoints

Add role-based authentication

Pagination & filtering for tracks

Unit and integration testing


Vaibhav Rikhy
Software Engineer | Backend & Full Stack
LinkedIn
