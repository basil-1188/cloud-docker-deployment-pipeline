# Automated Docker CI/CD Deployment Pipeline on AWS EC2

![Status](https://img.shields.io/badge/Status-Live-brightgreen)
![Docker](https://img.shields.io/badge/Docker-Containerised-blue)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-orange)

> A fully automated Docker deployment pipeline on AWS EC2. Push code to GitHub — the app rebuilds and redeploys automatically via GitHub Actions SSH in ~60 seconds.

🌐 **Live:** http://13.201.46.178:5000

---

## Architecture

Developer pushes code to GitHub
↓
GitHub Actions triggers automatically
↓
SSH connects to EC2 using ed25519 key
↓
Stops old Docker container
↓
Rebuilds Docker image
↓
Starts new container on port 5000
↓
Health check verifies deployment
↓
App live in ~60 seconds---

## Tech Stack

| Tool | Role |
|------|------|
| AWS EC2 t2.micro | Hosts the Docker container |
| Docker + Gunicorn | Containerises Python Flask app |
| GitHub Actions | CI/CD pipeline — SSH deploy on push |
| IAM + Security Groups | Secure access control |
| CloudWatch | CPU and network monitoring |

---

## Key Features

- ✅ Fully automated deployment on every GitHub push
- ✅ Docker containerisation with Gunicorn WSGI server
- ✅ Secure SSH deployment using dedicated ed25519 key pair
- ✅ EC2 Security Groups — SSH restricted to specific IP
- ✅ CloudWatch monitoring with CPU alarm at 80%
- ✅ Health check endpoint for deployment verification

---

## Project Structure
aws-docker-ec2/
├── app/
│   ├── app.py              # Flask web application
│   └── requirements.txt    # Python dependencies
├── Dockerfile              # Container definition
└── .github/
└── workflows/
└── deploy.yml      # GitHub Actions CI/CD pipeline

---

## Author

**Basil MK** — MCA Graduate | Cloud & DevOps Engineer

[![GitHub](https://img.shields.io/badge/GitHub-basil--1188-black?logo=github)](https://github.com/basil-1188)
[![Portfolio](https://img.shields.io/badge/Portfolio-Live-brightgreen)](https://d1ciiv3x1cw79m.cloudfront.net)
