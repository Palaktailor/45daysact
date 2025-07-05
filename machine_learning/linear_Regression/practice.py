from flask import Flask , render_template ,request,url_for  
import numpy as np
import joblib , pickle
import pandas as pd

#load the model 
model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
##
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/project")
def project():
    return render_template('project.html')

if __name__ == '__main__':
    app.run(debug=True)