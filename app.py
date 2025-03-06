import random
import string
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# Dictionary to store shortened URLs
url_database = {}

# Function to generate a short URL key
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_code = generate_short_code()
        url_database[short_code] = long_url
        return render_template('short_url.html', short_url=request.host_url + short_code)
    return render_template('index.html')

@app.route('/<short_code>')
def redirect_to_long_url(short_code):
    long_url = url_database.get(short_code)
    if long_url:
        return redirect(long_url)
    return "Short URL not found!", 404

if __name__ == '__main__':
    app.run(debug=True)
