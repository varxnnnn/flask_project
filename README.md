# Flask DevOps Deployment Project

## 🛠 Tech Stack
- Python (Flask)
- Docker
- Kubernetes (Minikube)
- GitHub Actions (CI/CD)

## 📄 Description
This project demonstrates a complete DevOps workflow by:

- Creating a simple Flask web app
- Containerizing the app with Docker
- Deploying to a local Kubernetes cluster using Minikube
- Automating image build/push using GitHub Actions

## 🚀 Run Locally

```bash
git clone https://github.com/yourusername/flask-devops-app.git
cd flask-devops-app
docker build -t yourdockerhub/flask-devops-app .
docker run -p 5000:5000 yourdockerhub/flask-devops-app
