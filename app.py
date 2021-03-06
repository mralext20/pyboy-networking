import threading
from io import BytesIO

from flask import Flask, send_file, render_template
from pyboy import PyBoy, windowevent, window
from io import BytesIO
from os import environ

app = Flask(__name__, template_folder='template')


ROM_NAME = 'rom/' + environ['ROM_NAME']


pb = PyBoy(ROM_NAME, window_type=None)
pb.set_emulation_speed(1)
pb.tick()

save = BytesIO()
save.seek(0)
pb.save_state(save)
save.seek(0)


@app.before_first_request
def runningjob():
    def run_job():
        while True:
            pb.tick()

    thread = threading.Thread(target=run_job)
    thread.start()


def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'jpeg', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


@app.route('/up')
def up_key():
    pb.send_input(windowevent.PRESS_ARROW_UP)
    pb.tick()
    pb.send_input(windowevent.RELEASE_ARROW_UP)
    return "OK"


@app.route('/down')
def down_key():
    pb.send_input(windowevent.PRESS_ARROW_DOWN)
    pb.tick()
    pb.send_input(windowevent.RELEASE_ARROW_DOWN)
    return "OK"


@app.route('/left')
def left_key():
    pb.send_input(windowevent.PRESS_ARROW_LEFT)
    pb.tick()
    pb.send_input(windowevent.RELEASE_ARROW_LEFT)
    return "OK"


@app.route('/right')
def right_key():
    pb.send_input(windowevent.PRESS_ARROW_RIGHT)
    pb.tick()
    pb.send_input(windowevent.RELEASE_ARROW_RIGHT)
    return "OK"


@app.route('/start')
def start_key():
    pb.send_input(windowevent.PRESS_BUTTON_START)
    pb.tick()
    pb.send_input(windowevent.RELEASE_BUTTON_START)
    return "OK"


@app.route('/select')
def select_key():
    pb.send_input(windowevent.PRESS_BUTTON_SELECT)
    pb.tick()
    pb.send_input(windowevent.RELEASE_BUTTON_SELECT)
    return "OK"


@app.route('/a')
def a_key():
    pb.send_input(windowevent.PRESS_BUTTON_A)
    pb.tick()
    pb.send_input(windowevent.RELEASE_BUTTON_A)
    return "OK"


@app.route('/b')
def b_key():
    pb.send_input(windowevent.PRESS_BUTTON_B)
    pb.tick()
    pb.send_input(windowevent.RELEASE_BUTTON_B)
    return "OK"


@app.route('/speed/<int:x>')
def set_speed(x):
    pb.set_emulation_speed(x)
    return f"set speed to {x}"


@app.route('/frame')
def get_frame():
    frame = pb.get_screen_image()
    frame = frame.convert('RGB')
    return serve_pil_image(frame)


@app.route('/save')
def save_state():
    with open(f'{ROM_NAME}.sav', 'wb') as fp:
        pb.save_state(fp)
        return 'saved'


@app.route('/load')
def load_state():
    with open(f'{ROM_NAME}.sav', 'rb') as fp:
        pb.load_state(fp)
        return 'loaded'


@app.route('/reset')
def reset_state():
    pb.load_state(save)
    return 'loaded'


@app.route('/')
def index():
    gametitle = pb.get_cartridge_title()
    return render_template('index.html', gametitle=gametitle)


if __name__ == "__main__":
    app.run()
