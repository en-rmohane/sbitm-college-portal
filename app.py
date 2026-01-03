from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/departments')
def departments():
    return render_template('departments.html')

@app.route('/facilities')
def facilities():
    return render_template('facilities.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/academics')
def academics():
    return render_template('academics.html')

@app.route('/faculty')
def faculty():
    return render_template('faculty.html')

@app.route('/placement')
def placement():
    return render_template('placement.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/admission')
def admission():
    return render_template('admission.html')

if __name__ == '__main__':
    app.run(debug=True)
