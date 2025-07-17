from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        category = request.form['category']
        hashtags = request.form['hashtags']
        
        video = request.files['video']
        thumbnail = request.files['thumbnail']

        video_path = os.path.join(UPLOAD_FOLDER, video.filename)
        thumbnail_path = os.path.join(UPLOAD_FOLDER, thumbnail.filename)

        video.save(video_path)
        thumbnail.save(thumbnail_path)

        return render_template('success.html',
                               title=title,
                               description=description,
                               video_url='/' + video_path,
                               thumbnail_url='/' + thumbnail_path)

    return render_template('upload.html')
