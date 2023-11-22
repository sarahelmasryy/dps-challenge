import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
from joblib import dump, load


app = Flask(__name__)
# model = pickle.load(open('randomForestRegressor.pkl','rb'))

model = load('RandomForest.h5') 


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods = ['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    return render_template('home.html', prediction_text="Predicted Accidents {}".format(int(prediction[0])))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    year = data['year']
    month = data['month']
    prediction = model.predict(([[year,month]]))

    output = int(prediction[0])
    response = {"prediction": output}
    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True)