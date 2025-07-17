from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'app/static/uploads/'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'jpg', 'jpeg', 'png'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['description']
        hashtags = request.form['hashtags']
        category = request.form['category']
        video = request.files['video']
        thumbnail = request.files['thumbnail']

        if video and allowed_file(video.filename):
            video_name = secure_filename(video.filename)
            video.save(os.path.join(app.config['UPLOAD_FOLDER'], video_name))

        if thumbnail and allowed_file(thumbnail.filename):
            thumb_name = secure_filename(thumbnail.filename)
            thumbnail.save(os.path.join(app.config['UPLOAD_FOLDER'], thumb_name))

        # Save data (title, desc, etc.) in DB (coming soon)
        return f"✅ Uploaded '{title}' successfully!"

    return render_template("upload.html")
