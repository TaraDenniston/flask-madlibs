from flask import Flask, request, render_template
import stories

app = Flask(__name__)

story_list = [
    stories.Story(
        ["adjective", "noun"],
        "Story 1: {adjective} {noun}"
    ),

    stories.Story(
        ["ing_verb", "plural_noun"],
        "Story 2: {ing_verb} {plural_noun}"
    ),

    stories.Story(
        ["verb", "direction"],
        "Story 3: {verb} {direction}"
    )
]


@app.route('/')
def select_story():
    return render_template('home.html')

@app.route('/story-form')
def story_form():
    story_num = int(request.args['story'])
    print(story_num)
    story = story_list[story_num - 1]
    print(story)
    return render_template('story_form.html', story=story, story_num=story_num)

@app.route('/story')
def display_story():
    story = story_list[int(request.args['story']) - 1]
    answers = dict(request.args)
    text_story = story.generate(answers)
    return render_template('story.html', story=text_story)



