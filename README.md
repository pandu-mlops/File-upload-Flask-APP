# Flask File Upload Application Using Docker

## 1. Project Overview

This project is a simple Flask web application that allows users to upload files through a web browser. Uploaded files are saved in a directory inside a Docker container. Docker packages the application and its dependencies so it can be built and run consistently across environments.

## 2. Technologies Used

- **Python** – Programming language
- **Flask** – Web application framework
- **HTML** – Frontend upload form
- **Gunicorn** – WSGI HTTP server
- **Docker** – Containerization platform

## 3. Project Architecture

1. The user opens the Flask application in a web browser.
2. The user selects a file and clicks Upload.
3. Flask receives the file through an HTTP POST request.
4. The application saves the file inside the container at `/app/uploads/`.
5. The uploaded filename is displayed on the web page.

## 4. Project Structure

```text
flask-file-upload/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── README.md
└── templates/
    └── index.html
```

The `uploads` directory is created automatically when the Flask application starts.

## 5. Prerequisites

Install the following software before running the project:

- Python 3.12 or a compatible version
- Docker Desktop
- Visual Studio Code (optional)
- A web browser

Verify Docker installation:

```bash
docker --version
```

## 6. Clone the Repository

If the project is available on GitHub, clone it using:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd flask-file-upload
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with your actual GitHub repository URL.

## 7. Application Configuration

- Application port: `5000`
- Upload directory: `/app/uploads`
- Maximum upload size: `16 MB`
- HTTP methods: `GET` and `POST`

Uploaded files are stored inside the Docker container.

## 8. Build the Docker Image

Open a terminal in the project directory and run:

```bash
docker build -t flask-file-upload .
```

Explanation:

- `docker build` builds the Docker image.
- `-t flask-file-upload` assigns a name to the image.
- `.` specifies the current directory as the build context.

Verify that the image was created:

```bash
docker images
```

## 9. Run the Docker Container

Start the application using:

```bash
docker run -d --name flask-upload-container -p 5000:5000 flask-file-upload
```

- `-d` runs the container in the background.
- `--name` assigns a name to the container.
- `-p 5000:5000` maps host port 5000 to container port 5000.
- `flask-file-upload` specifies the image to run.

## 10. Access the Application

Open a web browser and navigate to:

```text
http://localhost:5000
```

Select a file from your computer and click the Upload button. A success message appears and the uploaded filename is listed on the page.

## 11. Verify Uploaded Files

Check the uploaded files inside the running container:

```bash
docker exec flask-upload-container ls -l /app/uploads
```

To inspect a text file, replace `sample.txt` with the actual uploaded filename:

```bash
docker exec flask-upload-container cat /app/uploads/sample.txt
```

## 12. Persist Uploaded Files Using a Docker Volume

Files stored only in a container's writable layer can be lost when the container is removed. A Docker volume keeps uploads independently of the container lifecycle.

If you need to keep files already uploaded to the original container, back them up before removing it. Then run:

```bash
docker volume create flask-uploads
docker stop flask-upload-container
docker rm flask-upload-container
docker run -d --name flask-upload-container -p 5000:5000 -v flask-uploads:/app/uploads flask-file-upload
```

The named volume stores uploaded files independently of the container lifecycle. Do not delete the volume if you want to preserve those files.

## 13. Useful Docker Commands

List running containers:

```bash
docker ps
```

View application logs:

```bash
docker logs flask-upload-container
```

Stop the container:

```bash
docker stop flask-upload-container
```

Start the existing container:

```bash
docker start flask-upload-container
```

Restart the container:

```bash
docker restart flask-upload-container
```

Remove the container:

```bash
docker rm -f flask-upload-container
```

List Docker images:

```bash
docker images
```

## 14. Features

- Upload files through a web browser.
- Save files inside a Docker container.
- Display uploaded filenames.
- Limit uploads to 16 MB per request.
- Run the application using Docker.
- Preserve uploaded files using a Docker volume.

## 15. Security Considerations

This project is intended for learning and demonstration. Before deploying it publicly:

- Validate permitted file types.
- Prevent unintended overwriting of existing files.
- Add authentication and authorization where appropriate.
- Configure secrets securely.
- Consider malware scanning for untrusted uploads.
- Use HTTPS and appropriate production server settings.

## 16. Learning Outcomes

By completing this project, you will learn:

- How to build a Flask web application.
- How file uploads work in Flask.
- How to create and use a Dockerfile.
- How to build Docker images and run containers.
- How to map container ports to host ports.
- How to inspect files inside containers.
- How to persist data using Docker volumes.

## 17. Conclusion

This project demonstrates how to develop a file upload application using Flask and package it into a Docker container. It provides practical experience with Python web development, Docker image creation, container execution, and persistent storage. The project can be extended with cloud deployment, automated testing, and CI/CD pipelines.
