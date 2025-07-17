from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/free-videos')
def free_videos():
    return render_template('free_videos.html')

@app.route('/premium-videos')
def premium_videos():
    return render_template('premium_videos.html')

@app.route('/photos')
def photos():
    return render_template('photos.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')
