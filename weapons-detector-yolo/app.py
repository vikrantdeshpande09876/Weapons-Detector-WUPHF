import http, json, os
from flask import Flask, render_template, request, make_response
from flask_assets import Bundle, Environment
from utils.detection import run_yolov5_detector, get_image_buffer
from utils.kafka_producer import Producer

app = Flask(__name__)
app.config.from_pyfile('config.py')






@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('Home.html', title='Home | Weapons Detector- WOOF!', header='Home | Weapons Detector- WOOF!')


@app.route('/detect-weapons', methods=['GET', 'POST'])
def predict():
    if request.method=='POST':
        if request.files.get('filename'):
            image = request.files['filename']
            image_filename = f'data/{image.filename}'
            image.save(image_filename)
            save_dir, predictions = run_yolov5_detector(source=image_filename, data='data/weapons-detection.yaml')
            os.remove(image_filename)
            image_buffer = get_image_buffer(f'{save_dir}/{image.filename}')

            
            producer = Producer(kafka_server=app.config.get('KAFKA_SERVER'))
            json_message = json.dumps({'header':'WEAPON DETECTED', 'label':predictions}).encode('utf-8')
            producer.send_alert_if_weapon(
                predictions=predictions,
                topic=app.config.get('RESPONSE_TOPIC'),
                message=json_message
                )
            
            response = make_response()
            response.headers.set('Content-Type', 'image/jpeg')
            response.headers.set('Content-Disposition', 'attachment', filename=f'{image.filename}')
            response.status_code = http.HTTPStatus.OK
            response.data = image_buffer
            return response
    return render_template('Home.html', title='Home | Weapons Detector- WOOF!', header='Home | Weapons Detector- WOOF!')


@app.route('/detect-weapons-webcam', methods=['GET', 'POST'])
def predict_webcam():
    if request.method=='POST':
        _ = run_yolov5_detector(source=0, data='data/weapons-detection.yaml')
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