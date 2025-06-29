# 🕵️‍♀️ Image Steganography Web App

A simple yet powerful web application to **hide and reveal secret messages** in images using LSB (Least Significant Bit) based steganography.

This project was containerized with **Docker**, deployed using **Render**, and includes Kubernetes manifests for scalable deployment.

---

## 🔍 Features

- 🔐 Hide (encode) secret messages inside image files.
- 🔓 Reveal (decode) hidden messages from images.
- 🖼 Clean web interface built with HTML and Flask.
- 🐳 Dockerized for easy deployment.
- ☁️ Deployed on Render (cloud platform).
- ⚙️ Kubernetes support for production scaling.

---

## 🛠 Tech Stack

- **Frontend**: HTML + CSS (Jinja templates)
- **Backend**: Python Flask
- **Steganography**: PIL & custom image bit manipulation
- **Containerization**: Docker
- **Cloud Deployment**: Render
- **Orchestration**: Kubernetes (optional)

---

## 🚀 Live Demo

🌐 [Click here to try it live](https://image-steganography-web.onrender.com) 

---

## 🐳 Run Locally with Docker

```bash
# Clone the repo
git clone https://github.com/ChandanaDommeti/image-steganography-web.git
cd image-steganography-web

# Build Docker image
docker build -t stegano-app .

# Run container
docker run -p 5000:5000 stegano-app

☸️ Kubernetes (Optional)
You can deploy the app on a Kubernetes cluster using the provided manifests.

# Apply Deployment and Service
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Check pod logs
kubectl logs -l app=stegano-app

# Access using port-forward (if no LoadBalancer)
kubectl port-forward service/stegano-service 5000:5000
📁 Project Structure

image-steganography-web/
├── app.py                 # Flask backend
├── stegano_utils.py       # Steganography logic
├── templates/             # HTML pages (Jinja2)
├── static/                # Uploaded images
├── Dockerfile             # Docker build config
├── requirements.txt       # Python dependencies
├── k8s/
│   ├── deployment.yaml    # Kubernetes deployment
│   └── service.yaml       # Kubernetes service


🙌 Credits
#Developed by Chandana Dommeti

📝 License
#This project is open-source and free to use under the MIT License.
