from flask import Flask, request, render_template
import stories

app = Flask(__name__)

@app.route('/home')
def story_form():
    return render_template('home.html')

@app.route('/story')
def display_story():
    return render_template('story.html')


