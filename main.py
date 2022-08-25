from crypt import methods
from distutils.log import debug
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
regressor = pickle.load(open('regressor.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('templates\index.html')


@app.route('/predict', methods=('GET', 'POST'))
def predict():
    try:
        prediction = regressor.predict([[request.form.get('area', 'bedrooms', 'bathrooms', 'stories',
                                                          'mainroad', 'guestroom', 'basement',	'hotwaterheating', 'airconditioning',
                                                          'parking', 'prefarea', 'furnishingstatus')]])
        output = round(prediction[0], 2)
        return render_template('templates\index.html', prediction_text=f'Total price of the property is {output}/-')
    except:
        return render_template('templates\index.html', prediction_text='Invalid Input!')


if __name__ == '__main__':
    app.run(debug=True)
