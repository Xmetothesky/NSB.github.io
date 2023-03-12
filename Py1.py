from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-image', methods=['POST'])
def submit_image():
    file = request.files['myFile']
    scale = request.form['scale']
    # Do something with the file and scale values
    return 'Image received'

if __name__ == '__main__':
    app.run(debug=True)
