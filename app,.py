from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/videos'
app.config['THUMB_FOLDER'] = 'static/thumbnails'

# Create folders if they don't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['THUMB_FOLDER'], exist_ok=True)

# In-memory video database
videos_db = []

@app.route("/")
def home():
    return render_template("home.html", videos=videos_db)

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["description"]
        hashtags = request.form["hashtags"]
        category = request.form["category"]
        video = request.files["video"]
        thumbnail = request.files["thumbnail"]

        video_name = secure_filename(video.filename)
        thumb_name = secure_filename(thumbnail.filename)

        video.save(os.path.join(app.config['UPLOAD_FOLDER'], video_name))
        thumbnail.save(os.path.join(app.config['THUMB_FOLDER'], thumb_name))

        videos_db.append({
            "title": title,
            "description": desc,
            "hashtags": hashtags,
            "category": category,
            "video": video_name,
            "thumbnail": thumb_name
        })

        return "Video uploaded successfully!"

    return render_template("upload.html")
