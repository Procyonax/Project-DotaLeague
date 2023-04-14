from flask import Flask, render_template

from controllers.matches_controller import matches_blueprint

app = Flask(__name__)

app.register_blueprint(matches_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
