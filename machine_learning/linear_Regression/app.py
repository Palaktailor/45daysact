
# used for web frame work
from flask import Flask, render_template, request, url_for
import joblib, pickle
import pandas as pd
import sqlite3 


#load the model
model = pickle.load(open("model.pkl","rb"))# load the prre trained model


app = Flask(__name__)         # Creates a Flask app named app.

# database connection

def get_db_connection():
    try:
        conn = sqlite3.connect("bike_db.db")          # Connects to the SQLite database file named bike_db.db
        # to get the data into dict like formate
        conn.row_factory = sqlite3.Row               # row_factory makes rows behave like dictionaries (e.g., row['brand_name']).
        return conn

    except sqlite3.Error as e:
        print(e)
        return None

# create a table if not exist
def create_table():
    conn = get_db_connection()
    if conn:
        # cursor ---> to fetch and send data, and to run any query in database
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS bike_prediction(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand_name TEXT NOT NULL,
        owner INTEGER NOT NULL, 
        kms_driven INTEGER NOT NULL, 
        age INTEGER NOT NULL, 
        power INTEGER NOT NULL, 
        predicted_price INTEGER NOT NULL)""")

        conn.commit()
        cursor.close()
        conn.close()

# initialize the database
create_table()

# route history page
@app.route('/history', methods=["GET", "POST"])
def history():
    brand_name_filter = request.form.get("brand_name_filter", None)
    conn = get_db_connection()
    historical_data = []
    if conn:
        cursor = conn.cursor()
        try:
            if brand_name_filter:
                query = """SELECT * FROM bike_prediction WHERE brand_name = ?"""
                cursor.execute(query, (brand_name_filter,))
            else:
                query = """SELECT * FROM bike_prediction"""
                cursor.execute(query)
            historical_data = [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    return render_template('history.html', historical_data=historical_data)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/data_science')
def data_science():
    return render_template('data_science.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/predict', methods = ["POST"])
def predict():
    if request.method == "POST":
        try:
            brand_name = request.form['brand_name']
            owner_name = int(request.form['owner'])
            age_bike = int(request.form['age'])
            power_bike = int(request.form['power'])
            kms_driven_bike = int(request.form['kms_driven'])

            bike_numbers = {'TVS': 0,
            'Royal Enfield': 1,
            'Triumph': 2,
            'Yamaha': 3,
            'Honda': 4,
            'Hero': 5,
            'Bajaj': 6,
            'Suzuki': 7,
            'Benelli': 8,
            'KTM': 9,
            'Mahindra': 10,
            'Kawasaki': 11,
            'Ducati': 12,
            'Hyosung': 13,
            'Harley-Davidson': 14,
            'Jawa': 15,
            'BMW': 16,
            'Indian': 17,
            'Rajdoot': 18,
            'LML': 19,
            'Yezdi': 20,
            'MV': 21,
            'Ideal': 22}

            brand_name_encoded = bike_numbers.get(brand_name)
            input_data = [[owner_name,
            brand_name_encoded,
            kms_driven_bike,
            age_bike, power_bike]]

            prediction = model.predict(input_data)
            prediction = round(prediction[0], 2)

            conn = get_db_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO bike_prediction (brand_name, owner, kms_driven, age, power, predicted_price)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (brand_name, owner_name, kms_driven_bike, age_bike, power_bike, prediction))
                conn.commit()
                cursor.close()
                conn.close()

            return render_template('project.html',prediction = prediction)

        except:
            return "something is wrong"



if __name__ == '__main__':
    app.run(debug = True)