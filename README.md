🎵 Music Backend API

Backend service for managing users, tracks, and playlists with authentication and full CRUD functionality. Built using FastAPI, MongoDB, and Docker.

🚀 Overview

This project demonstrates a production-style backend system with:

RESTful API design
JWT-based authentication
NoSQL data modeling with MongoDB
Containerized services using Docker
⚙️ Tech Stack
Backend: FastAPI (Python)
Database: MongoDB (Beanie ODM, Motor)
Authentication: JWT + bcrypt
Infrastructure: Docker, Docker Compose
Docs: Swagger UI
📂 Structure
app/
├── core/        # Configuration
├── models/      # Database models
├── routers/     # API routes
├── schemas/     # Request/response schemas
└── main.py      # Entry point
🛠 Running Locally
# 1. Clone repo
git clone https://github.com/your-username/music-backend.git
cd music-backend

# 2. Setup environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start services
docker compose up -d mongo elasticsearch

# 5. Run server
uvicorn app.main:app --reload
📖 API Docs

Available at:

http://127.0.0.1:8000/docs
🔑 Core Endpoints
Method	Endpoint	Description
POST	/auth/signup	Create user
POST	/auth/login	Authenticate user
GET	/tracks	List tracks
POST	/tracks	Create track
GET	/tracks/{id}	Get track
DELETE	/tracks/{id}	Delete track
GET	/playlists	List playlists
POST	/playlists	Create playlist
📸 Demo
API Overview

Authentication

Track CRUD

🔐 Security
Passwords hashed using bcrypt
Authentication via JWT tokens
Sensitive configs stored in .env
📌 Future Work
Update (PUT/PATCH) endpoints
Search integration with Elasticsearch
Pagination & filtering
Role-based access control
Test coverage
👨‍💻 Author

Vaibhav Rikhy
Backend / Full Stack Engineer
LinkedIn
