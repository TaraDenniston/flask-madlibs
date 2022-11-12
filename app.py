from flask import Flask, request, render_template
import stories

app = Flask(__name__)

@app.route('/home')
def story_form():
    story = stories.story
    return render_template('home.html', story=story)

@app.route('/story')
def display_story():
    answers = dict(request.args)
    text_story = stories.story.generate(answers)
    return render_template('story.html', story=text_story)



