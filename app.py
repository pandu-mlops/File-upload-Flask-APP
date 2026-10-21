
from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "/app/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB limit

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file selected", 400

    file = request.files["file"]

    if file.filename == "":
        return "Please select a file", 400

    filename = secure_filename(file.filename)

    if not filename:
        return "Invalid filename", 400

    file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    return f"File '{filename}' uploaded successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
