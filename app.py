from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import csv
import os

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    # prediction = 0
    # if request.method == 'POST':
    #     model = pickle.load(open('model_house_price.sav','rb'))
    #     bed = request.form.get('bedrooms')
    #     bath = request.form.get('bathrooms')
    #     sqft = request.form.get('sqft')


        # params = {'bedrooms':[bed], 'bathrooms':[bath], 'sqft_living': [sqft]}
        # print(params)

        # if bed == '' or bath == '' or sqft == '' or int(sqft) < 50:
        #     prediction = 0
        # else:
        #     prediction = int(model.predict(pd.DataFrame(params)))

        # print(prediction)


    # return render_template('index.html', prediction=prediction)
    return render_template('index.html')


@app.route('/data', methods=['GET','POST'])
def data():
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("==============================")
    print("==============================")
    print("==============================")
    print("==============================")
    print("Files in %r: %s" % (cwd, files))
    print("==============================")
    print("==============================")
    print("==============================")
    print("==============================")
    print("==============================")

    if request.method == 'POST':
        f = request.form['csvfile']
        data = []
        with open(f) as file:
            csvfile = csv.reader(file)
            for row in csvfile:
                data.append(row)
        return render_template('data.html', data=data)




if __name__ == '__main__':
    app.run(debug=True)