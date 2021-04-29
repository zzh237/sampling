from flask import Flask, render_template,send_from_directory
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
PEOPLE_FOLDER = os.path.join(APP_ROOT, 'static')

def run_app()->Flask:
    app = Flask(__name__)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


    app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

    @app.route('/')
    @app.route('/index')
    def show_index():
        # full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'IMG_1222.jpg')
        # if os.path.isfile(full_filename) == False:
        #     raise FileNotFoundError('image not found')
        # render_template("index.html", image_image = full_filename)
        return render_template("index.html")

    @app.route('/')
    @app.route('/index/<filename>')
    def send_image(filename):
        return send_from_directory("static",filename) 
    return app 

if __name__ == "__main__":
    run_app().run(host='0.0.0.1',port=5000, debug=False)