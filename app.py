from flask import Flask, render_template, request
import pickle
import numpy as np
from io import BytesIO
from keras.models import load_model



#model = pickle.load(open('file.pkl','rb'))
#model = load_model('calories.h5')
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')


@app.route('/predict', methods=['POST'])
def result():
    gender = request.form.get('gender')
    if(gender=='Male'):
        gender=0
    else:
        gender=1
    age = int(request.form.get('age'))
    height = float(request.form.get('height'))
    weight = float(request.form.get('weight'))
    duration = float(request.form.get('duration'))
    heart = float(request.form.get('heart'))
    bodytemp = float(request.form.get('bodytemp'))
    print(gender)
    input_data = np.array([[gender, age, height, weight, duration, heart, bodytemp]])

    pred = model.predict(input_data)
    print('prediction', pred)
    return render_template('result.html', data=pred)
