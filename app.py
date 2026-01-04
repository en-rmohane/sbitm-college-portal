import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'supersecretkey' # Needed for flash messages
app.config['UPLOAD_FOLDER'] = 'static/images/faculty'

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

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

@app.route('/upload_faculty', methods=['GET', 'POST'])
def upload_faculty():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)
        file = request.files['file']
        custom_name = request.form.get('filename')
        
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
            
        if file:
            # Use custom name if provided, else original filename
            if custom_name:
                filename = secure_filename(custom_name)
            else:
                filename = secure_filename(file.filename)
                
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash(f'Image uploaded successfully as {filename}!', 'success')
            return redirect(url_for('upload_faculty'))
            
    return render_template('upload_faculty.html')

if __name__ == '__main__':
    app.run(debug=True)

