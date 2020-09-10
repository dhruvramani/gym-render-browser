import cv2
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, request, render_template, Response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def frame_gen(env_func, *args, **kwargs):
    get_frame = env_func(*args, **kwargs)
    while True:
        frame = next(get_frame, None)
        if frame is None:
            break
        _, frame = cv2.imencode('.png', frame)
        frame = frame.tobytes()
        yield (b'--frame\r\n' + b'Content-Type: image/png\r\n\r\n' + frame + b'\r\n')

def render_browser(env_func):
    def wrapper(*args, **kwargs):
        @app.route('/render_feed')
        def render_feed():
            return Response(frame_gen(env_func=env_func, *args, **kwargs), mimetype='multipart/x-mixed-replace; boundary=frame')

        print("Starting rendering, check `server_ip:5000`.")
        app.run(host='0.0.0.0', port='5000', debug=False)

    return wrapper

if __name__ == '__main__':
    print("Testing Gym Browser Render")
    import gym

    @render_browser
    def random_policy():
        env = gym.make('Breakout-v0')
        env.reset()

        for _ in range(100):
            yield env.render(mode='rgb_array')
            action = env.action_space.sample()
            env.step(action)

    random_policy()