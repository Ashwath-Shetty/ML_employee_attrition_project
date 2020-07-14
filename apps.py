import numpy as np
#from werkzeug.wrappers import Request, Response
from flask import Flask,jsonify,request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model1.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    a=[0]*14
    int_features = [int(x) for x in request.form.values()]
    
    #final_features1 = [np.array(int_features)]
    a[0:12]=int_features
    #a[0:12]=final_features1
    #c=final.reshape(-1,1)
    #a.reshape(
    if request.form.get("TRAVEL") == "2":
        a[12]=1;
        a[11]=0;
        a[13]=0
    elif request.form.get("TRAVEL") == "1":
        a[12]=0;
        a[11]=1;
        a[13]=0;
    else:
        a[12]=0;
        a[11]=0;
        a[13]=1
        
    
    final=[np.array(a)]    
    prediction = model.predict(final)
    #print(int_features)
    #if request.form.get("cars") == "1":
     #   score=1;
    #else:
     #   score=0;

    #output = round(prediction[0], 2)format(final_features1)

    return render_template('index.html', prediction_text='Employee attrition possibility will be {}'.format(prediction))


if __name__ == "__main__":
    app.run(debug=True)
