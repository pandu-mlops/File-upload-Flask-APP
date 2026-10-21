# Assignment 1: Dockerizing a Flask Application with File Uploads

#### Task
Create a Flask application that allows users to upload files. The application should save the uploaded files to a directory within the Docker container. Dockerize the Flask application.

Tips: 
1. Create the Flask Application
2. Create a directory for your project and add the following files `app.py`, `requirements.txt`
`app.py`

```
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        message = request.form.get('message')
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

```
 `requirements.txt`

 ```
Flask==2.2.3
Werkzeug==2.2.3

 ```
3. Create a folder named `templates` in the same directory as `app.py`.
4. Inside the templates folder, create a file named `index.html`:
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Web App</title>
</head>
<body>
    <h1>Submit a Message</h1>
    <form method="POST">
        <label for="message">Message:</label>
        <input type="text" id="message" name="message" required>
        <button type="submit">Submit</button>
    </form>

    {% if message %}
        <h2>Submitted Message:</h2>
        <p>{{ message }}</p>
    {% endif %}
</body>
</html>

```
5. Create the Dockerfile:
In the same directory, create a Dockerfile:
```
# Use the official Python image from the Docker Hub

# Set the working directory in the container

# Copy the requirements file and install dependencies

# Copy the application code into the container

# Expose port 5000

# Command to run the Flask app

```
6. Build, Run and Push the Docker Image:











