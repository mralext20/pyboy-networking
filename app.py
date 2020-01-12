from io import BytesIO

from flask import Flask, send_file
from pyboy import PyBoy, windowevent

app = Flask(__name__)

import threading


pyboy = PyBoy('pkmnred.gb')
pyboy.set_emulation_speed(1)

@app.before_first_request
def runningjob():
    def run_job():
        while True:
            pyboy.tick()

    thread = threading.Thread(target=run_job)
    thread.start()


def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'jpeg', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

@app.route('/up')
def up_key():
    pyboy.send_input(windowevent.PRESS_ARROW_UP)
    pyboy.tick()
    pyboy.send_input(windowevent.RELEASE_ARROW_UP)
    return "OK"


@app.route('/down')
def down_key():
    pyboy.send_input(windowevent.PRESS_ARROW_DOWN)
    pyboy.tick()
    pyboy.send_input(windowevent.RELEASE_ARROW_DOWN)
    return "OK"


@app.route('/left')
def left_key():
    pyboy.send_input(windowevent.PRESS_ARROW_LEFT)
    pyboy.tick()
    pyboy.send_input(windowevent.RELEASE_ARROW_LEFT)
    return "OK"


@app.route('/right')
def right_key():
    pyboy.send_input(windowevent.PRESS_ARROW_RIGHT)
    pyboy.tick()
    pyboy.send_input(windowevent.RELEASE_ARROW_RIGHT)
    return "OK"


@app.route('/start')
def start_key():
    pyboy.send_input(windowevent.PRESS_BUTTON_START)
    pyboy.tick()
    pyboy.send_input(windowevent.RELEASE_BUTTON_START)
    return "OK"


@app.route('/select')
def select_key():
    pyboy.send_input(windowevent.PRESS_BUTTON_SELECT)
    pyboy.tick()
    pyboy.send_input(windowevent.RELEASE_BUTTON_SELECT)
    return "OK"


@app.route('/a')
def a_key():
    pyboy.send_input(windowevent.PRESS_BUTTON_A)
    pyboy.tick()
    pyboy.send_input(windowevent.RELEASE_BUTTON_A)
    return "OK"


@app.route('/b')
def b_key():
    pyboy.send_input(windowevent.PRESS_BUTTON_B)
    pyboy.tick()
    pyboy.send_input(windowevent.RELEASE_BUTTON_B)
    return "OK"

@app.route('/speed/<int:x>')
def set_speed(x):
    pyboy.set_emulation_speed(x)
    return f"set speed to {x}"

@app.route('/frame')
def get_frame():
    frame = pyboy.get_screen_image()
    frame = frame.convert('RGB')
    return serve_pil_image(frame)



if __name__ == "__main__":
    app.run()
