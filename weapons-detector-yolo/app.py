import http, io
from flask import Flask, render_template, request, make_response
from flask_assets import Bundle, Environment
from my_detection import run as run_yolov5_detector
from PIL import Image

app = Flask(__name__)
app.config.from_pyfile('config.py')




def get_image_buffer(abs_path):
    image = Image.open(abs_path)
    buffer = io.BytesIO()
    image.save(buffer, format='jpeg')
    return buffer.getvalue()




@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('Home.html', title='Home | Weapons Detector- WOOF!', header='Home | Weapons Detector- WOOF!')


@app.route('/detect-weapons', methods=['GET', 'POST'])
def predict():
    if request.method=='POST':
        if request.files.get('filename'):
            image = request.files['filename']
            image.save(f'data/{image.filename}')
            save_dir = run_yolov5_detector(source=f'data/{image.filename}')
            response = make_response()
            response.headers.set('Content-Type', 'image/jpeg')
            response.headers.set('Content-Disposition', 'attachment', filename=f'{image.filename}')
            response.status_code = http.HTTPStatus.OK
            response.data = get_image_buffer(f'{save_dir}/{image.filename}')
            return response
    return render_template('Home.html', title='Home | Weapons Detector- WOOF!', header='Home | Weapons Detector- WOOF!')


@app.route('/detect-weapons-webcam', methods=['GET', 'POST'])
def predict_webcam():
    if request.method=='POST':
        _ = run_yolov5_detector(source=0)
    return render_template('Result.html', title='Home | Weapons Detector- WOOF!', header='Home | Weapons Detector- WOOF!')




if __name__ == "__main__":
    bundles = {
        'javascript_source' : Bundle('js/base.js', output='gen/base.js'),
        'javascript_result' : Bundle('js/Result_XML_Checkboxes.js', output='gen/Result_XML_Checkboxes.js'),
        'css_source' : Bundle('css/base.css', output='gen/base.css')
    }

    assets = Environment(app)
    assets.register(bundles)

    app.run(
        host=app.config.get('FLASK_HOST'),
        port=app.config.get('FLASK_PORT'),
        use_reloader=app.config.get('DEBUG')
        )