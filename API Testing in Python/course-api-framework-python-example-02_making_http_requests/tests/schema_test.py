
import requests
from json import loads

from config import BASE_URI

from assertpy.assertpy import assert_that, soft_assertions

from cerberus import Validator





schema = {
   "fname": {'type': 'string'},
   "lname": {'type': 'string'},
   "person_id": {'type': 'integer'},
   "timestamp": {'type': 'string'}
}




def test_read_one_operation_has_expected_schema():
   response = requests.get(f'{BASE_URI}/1')
   persons = loads(response.text)

   validator = Validator(schema, require_all=True)

   with soft_assertions():
       for person in persons:
           is_valid = validator.validate(person)
           assert_that(is_valid, description=validator.errors).is_true()