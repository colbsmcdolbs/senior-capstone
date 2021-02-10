from helpers.fields import get_races, get_workclasses, get_educations, get_maritial_status, get_occupations, get_relationships, get_genders, get_native_countries

def validate_form(json_data):
    if not isinstance(json_data, list):
        raise Exception("Supplied JSON needs to be a list of one.")
    data = json_data[0]
    if data == None:
        raise Exception("Empty object found.")

    check_nulls(data)
    check_data_integrity(data)

"""
Checks the data for any unacceptable Data
"""
def check_data_integrity(data):
    if not isinstance(data['age'], int):
        raise Exception(f"Age not formatted as an integer")

    if data['age'] < 18 or data['age'] > 100:
        raise Exception(f"Age is too high or low...")

    if data['workclass'] not in get_workclasses():
        raise Exception(f"Invalid Workclass provided.")

    if data['education'] not in get_educations():
        raise Exception(f"Invalid Education provided.")

    if data['marital-status'] not in get_maritial_status():
        raise Exception(f"Invalid Marital-Status provided.")

    if data['occupation'] not in get_occupations():
        raise Exception(f"Invalid Occupation provided.")

    if data['relationship'] not in get_relationships():
        raise Exception(f"Invalid Relationship Status provided.")

    if data['race'] not in get_races():
        raise Exception(f"Invalid Race provided.")

    if data['gender'] not in get_genders():
        raise Exception(f"Invalid Gender provided.")

    if data['native-country'] not in get_native_countries():
        raise Exception(f"Invalid Native Country provided.")

    if not isinstance(data['hours-per-week'], int):
        raise Exception(f"Working hours per week is not formatted as an integer")

    if data['hours-per-week'] < 0 or data['age'] > 80:
        raise Exception(f"Working hours per week is too high or low...")

"""
Checks the data that we have received for null values
"""
def check_nulls(data):
    if data['age'] is None:
        raise Exception(f"Age is required.")
    
    if data['workclass'] is None:
        raise Exception(f"Workclass is required.")

    if data['education'] is None:
        raise Exception(f"Education is required.")

    if data['marital-status'] is None:
        raise Exception(f"Marital Status is required.")

    if data['occupation'] is None:
        raise Exception(f"Occupation is required.")

    if data['relationship'] is None:
        raise Exception(f"Relationship Status is required.")

    if data['race'] is None:
        raise Exception(f"Race is required.")

    if data['gender'] is None:
        raise Exception(f"Gender is required.")

    if data['hours-per-week'] is None:
        raise Exception(f"Working Hours per Week is required.")

    if data['native-country'] is None:
        raise Exception(f"Native Country is required.")
