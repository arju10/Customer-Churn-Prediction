# from flask import Flask, request, jsonify
# import pickle
# import numpy as np

# # Initialize Flask app
# app = Flask(__name__)

# # Load the saved model
# with open('model.pkl', 'rb') as file:
#     model = pickle.load(file)

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get data from POST request
#         data = request.json
        
#         # Preprocess the data (assuming the features are sent in the same order as in the trained model)
#         # You might want to add data validation here
#         features = np.array([data['Age'], data['Gender'], data['Location'], data['Subscription_Length_Months'], data['Monthly_Bill'], data['Total_Usage_GB']])
        
#         # Perform prediction
#         prediction = model.predict(features.reshape(1, -1))
        
#         # Convert prediction to "Churn" or "Not Churn"
#         result = "Churn" if prediction[0] == 1 else "Not Churn"
        
#         return jsonify({"result": result})
        
#     except Exception as e:
#         return jsonify({"error": str(e)})


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form
        features = np.array([data['Age'], data['Gender'], data['Location'], data['Subscription_Length_Months'], data['Monthly_Bill'], data['Total_Usage_GB']])
        prediction = model.predict(features.reshape(1, -1))
        result = "Churn" if prediction[0] == 1 else "Customer is Not Churn"
        return render_template('index.html', result=result)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
