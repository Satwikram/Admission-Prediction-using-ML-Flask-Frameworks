from flask import Flask, render_template, request, jsonify
from flask_cors import CORS,cross_origin
import pickle



app = Flask(__name__) #Initilizing the Flask App


@app.route('/', methods = ['GET']) #Route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict', methods = ['GET', 'POST']) #Route to show the predictions in the web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:

            #Reading the input from the user
            gre_score = float(request.form['gre_score'])
            toefl_score = float(request.form['toefl_score'])
            university_rating = float(request.form['university_rating'])
            sop = float(request.form['sop'])
            lor = float(request.form['lor'])
            cgpa = float(request.form['cgpa'])
            is_research = request.form['research']

            if is_research == 'yes':
                research = 1
            else:
                research = 0

            filename =  'finalized_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) #Loading the file from the storage
            #Predictions using loaded_model
            prediction = loaded_model.predict([[gre_score, toefel_score, university_rating, sop, lor, cgpa, is_research]])
            print("Prediction is:", prediction)

            #Showing Prediction in UI
            return render_template('result.html', prediction = round(100 * prediction[0]))

        except Exception as e:
            print("Error is:", e)
            return "Something Went Wrong!, Please Contact Administration."

        else:
            return_template('index.html')



if __name__ == '__main__':
    app.run(debug = True)
