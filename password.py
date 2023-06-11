from flask import Flask, render_template, request
import string
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        length = int(request.form['length'])
        character_set = request.form.getlist('character_set')
        password = generate_password(length, character_set)
        return render_template('result.html', password=password)
    return render_template('index.html')

def generate_password(length, character_set):
    characters = ''
    if 'digits' in character_set:
        characters += string.digits
    if 'letters' in character_set:
        characters += string.ascii_letters
    if 'special_characters' in character_set:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == '__main__':
    app.run(debug=True)
