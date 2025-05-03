from flask import Flask, render_template_string

app = Flask(__name__)

def read_html(file_name):
    with open(f'templates/{file_name}', 'r', encoding='utf-8') as f:
        return f.read()

@app.route('/')
def home():
    return render_template_string(read_html('index.html'))

@app.route('/catalog')
def catalog():
    return render_template_string(read_html('catalog.html'))

@app.route('/category')
def category():
    return render_template_string(read_html('category.html'))

@app.route('/contacts')
def contacts():
    return render_template_string(read_html('contacts.html'))

@app.route('/<path:unknown_path>')
def fallback(unknown_path):
    return render_template_string(read_html('contacts.html'))

if __name__ == '__main__':
    app.run(debug=True)
