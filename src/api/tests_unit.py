import unittest

from helpers.form_processor import check_nulls, check_data_integrity, validate_form

good_data = {
        'age': 25,
        'workclass': 'Private',
        'education': 'Doctorate',
        'marital-status': 'Married-civ-spouse',
        'occupation': 'Sales',
        'relationship': 'Husband',
        'race': 'White',
        'gender': 'Male',
        'native-country': 'United-States',
        'hours-per-week': 40 }

class FormProcessorCheckNullsTests(unittest.TestCase):

    def test_happy_path(self):
        check_nulls(good_data)
        self.assertTrue(True)

    def test_one_value_null(self):
        one_null = good_data.copy()
        one_null['age'] = None
        with self.assertRaises(Exception):
            check_nulls(one_null)

    def test_all_values_at_none(self):
        data = good_data.copy()
        for key in data:
            data[key] = None
        with self.assertRaises(Exception):
            check_nulls(data)

    def test_with_empty_object(self):
        empty_obj = {}
        with self.assertRaises(Exception):
            check_nulls(empty_obj)

class FormProcessorCheckDataIntegrityTests(unittest.TestCase):

    def test_happy_path(self):
        check_data_integrity(good_data)
        self.assertTrue(True)

    def test_age_as_not_int(self):
        age_not_int = { 'age': 'test' }
        with self.assertRaises(Exception):
            check_data_integrity(age_not_int)

    def test_work_hours_as_not_int(self):
        age_not_int = { 'hours-per-week': 'test' }
        with self.assertRaises(Exception):
            check_data_integrity(age_not_int)

    def test_occupation_not_in_enum(self):
        data = good_data.copy()
        data['occupation'] = 'NOT_GOING_TO_WORK'
        with self.assertRaises(Exception):
            check_data_integrity(data)

    def test_empty_object(self):
        empty_obj = {}
        with self.assertRaises(Exception):
            check_data_integrity(empty_obj)

class FormProcessorValidateFormTests(unittest.TestCase):

    def test_happy_path(self):
        validate_form([good_data])
        self.assertTrue(True)

    def test_json_is_not_list(self):
        with self.assertRaises(Exception):
            validate_form(good_data)

    def test_list_containing_empty_object_will_fail(self):
        with self.assertRaises(Exception):
            validate_form([{}])

if __name__ == '__main__':
    unittest.main()
