from flask import Flask, render_template, request, redirect
import requests
#import redis
app = Flask(__name__)
#cache = redis.Redis(host='redis', port=6379)
API_GATEWAY_URL = "https://8bvo32h992.execute-api.us-east-1.amazonaws.com/dev/submit"

@app.route('/')
def index():
    return render_template('form.html')
@app.route('/submit', methods=['POST'])
def submit():
    data = {
        "nume": request.form['nume'],
        "intrebari": {
            "How many years of experience do you have with AWS ?": request.form['q1'],
            "How many years of experience do you have with Python frameworks(ex:Django) ?": request.form['q2'],
            "How many years of experience do you have with Docker, Kubernetes ?": request.form['q3'],
            "How many years of experience do you have with Linux distributions ?": request.form['q4']
            }
        }
    if not data.get("nume").isalnum():
        return "Invalid input", 400
    for i in data.get("intrebari"):
        if not data.get("intrebari")[i].isdigit():
            return "Invalid input", 400

    response=requests.post(API_GATEWAY_URL,json=data)
    if response.status_code == 200:
        print("SENT!")
        return render_template('success.html')
    else:
        return f"Eroare la trimitere: {response.text}", 500

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8000)
