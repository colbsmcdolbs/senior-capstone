import os
from flask import Flask, request, jsonify
from pathlib import Path
from helpers.form_processor import validate_form
import pandas as pd
import joblib

## Defined here for global access, will be instantiated during startup
trained_model = None
model_columns = None

parent = Path(__file__).parent.absolute()
data_folder = f"{parent}/data"

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query_model():
    try:
        json_data = request.json
        validate_form(json_data)
        data_frame = pd.DataFrame(json_data)
        dummied_data = pd.get_dummies(data_frame)

        cleansed_query = dummied_data.reindex(columns=model_columns, fill_value=0)
        prediction = trained_model.predict(cleansed_query)

        return jsonify({'result': prediction})
    
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    trained_model = joblib.load(f"{data_folder}/model.pkl")
    model_columns = joblib.load(f"{data_folder}/model_columns.pkl")

    app.run(host='0.0.0.0', port=os.getenv('PORT'))
