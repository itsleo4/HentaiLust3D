from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

videos_db = []  # Temporary in-memory video database

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
        thumb = request.files["thumbnail"]

        video_name = secure_filename(video.filename)
        thumb_name = secure_filename(thumb.filename)

        video_path = os.path.join(app.config['UPLOAD_FOLDER'], video_name)
        thumb_path = os.path.join(app.config['UPLOAD_FOLDER'], thumb_name)

        video.save(video_path)
        thumb.save(thumb_path)

        videos_db.append({
            "title": title,
            "description": desc,
            "hashtags": hashtags,
            "category": category,
            "video": video_name,
            "thumbnail": thumb_name
        })

        return redirect(url_for("home"))

    return render_template("upload.html")
