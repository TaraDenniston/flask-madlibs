from flask import Flask, request, render_template
import stories

app = Flask(__name__)


story_list = [
    stories.Story(
        ["adjective1", "adjective2", "adjective3", "adverb", "body_part", \
        "condition", "ing_verb", "name1", "name2", "name3", "noun", \
        "past_tense_verb", "plural_noun", "relationship", "verb1", "verb2"],
        "Dear {name1},\n\nI am having a {adjective1} time at camp. "\
        "The counselor is {adjective2} and the food is {adjective3}. "\
        "I met {name2} and we became friends. Unfortunately, {name2} is "\
        "{condition} and I {past_tense_verb} my {body_part} so we "\
        "couldn't go {ing_verb} like everyone else. I need more "\
        "{plural_noun} and a {noun} sharpener, so please {adverb} "\
        "{verb1} when you {verb2} back.\n\nYour {relationship},\n{name3}"
    ),

    stories.Story(
        ["capitalized_adjective", "capitalized_sound", "illness", \
        "location", "name", "number", "plural_noun"],
        "Dear School Nurse:\n\n{name} will not be attending school "\
        "today. They have come down with a case of {illness} and have "\
        "horrible {plural_noun} and a fever of {number}. We have made "\
        "an appointment with Dr. {capitalized_sound}, who studied for "\
        "many years in {location}. He will send you all the information "\
        "you need.\n\nSincerely,\nMrs. {capitalized_adjective}"
    ),

    stories.Story(
        ["adjective", "adverb", "animals", "body_part", "emotion_noun", \
        "illness", "item", "liquid", "noun", "number", "occupation", \
        "plural_noun", "verb1", "verb2"],
        "In order to wash your face {adverb}, you must first wet your "\
        "{item} in warm {liquid}. Then, {verb1} it across your face "\
        "{number} times. This will wash off any remaining {plural_noun}."\
        " When you are done you should {verb2} the {item} in {adjective}"\
        " water to clean it. You should also wipe your face with a "\
        "{noun} to keep it smooth and shiny. This will also keep away "\
        "{animals}. Don't worry, it is normal to experience {emotion_noun} "\
        "the first time you try this. Consult your {occupation} if you "\
        "break out in {illness}. This works well on your {body_part} too!"
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



