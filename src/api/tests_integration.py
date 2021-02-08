import unittest
import pandas as pd
import joblib
from pathlib import Path
from helpers.form_processor import validate_form

should_pass = [{
    'age': 67,
    'workclass': 'Private',
    'education': 'Doctorate',
    'marital-status': 'Divorced',
    'occupation': 'Exec-managerial',
    'relationship': 'Not-in-family',
    'race': 'White',
    'gender': 'Male',
    'native-country': 'United-States',
    'hours-per-week': 60
}]

should_fail = [{
    'age': 25,
    'workclass': 'State-gov',
    'education': 'Some-college',
    'marital-status': 'Never-married',
    'occupation': 'Other-service',
    'relationship': 'Not-in-family',
    'race': 'Black',
    'gender': 'Male',
    'native-country': 'United-States',
    'hours-per-week': 40
}]

parent = Path(__file__).parent.absolute()
data_folder = f"{parent}/data"
trained_model = joblib.load(f"{data_folder}/model.pkl")
model_columns  = joblib.load(f"{data_folder}/model_columns.pkl")

def RunModel(json):
    validate_form(json)
    data_frame = pd.DataFrame(json)
    dummied_data = pd.get_dummies(data_frame)

    cleansed_query = dummied_data.reindex(columns=model_columns, fill_value=0)
    prediction = trained_model.predict(cleansed_query)
    return prediction

class VerifyModelWorkingTests(unittest.TestCase):

    def test_good_data_should_succeed(self):
        result = RunModel(should_pass)
        self.assertEqual(result, 1)

    def test_bad_data_should_fail(self):
        result = RunModel(should_fail)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
