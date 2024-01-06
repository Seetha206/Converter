from flask import Flask, render_template
from Src.controller.conversion_controller import ConversionController
from Src.util.logger import custom_logger

app = Flask(__name__)
app.config.from_object('Src.constants.constants')
app.logger=custom_logger
conversion_controller = ConversionController(app)

@app.route('/')
def index():
    converted_file=True
    return render_template('conversion.html',converted_file=converted_file)

@app.route('/upload', methods=['POST'])
def upload():
    return conversion_controller.upload()

@app.route('/download/<filename>')
def download(filename):
    return conversion_controller.download(filename)

if __name__ == '__main__':
    app.run(debug=True)
