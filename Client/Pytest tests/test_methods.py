import requests
import pytest
import random
from random import randint
import string

def random_json():
	letters = string.ascii_lowercase
	random_string = ''.join(random.choice(letters) for i in range(randint(1,30)))

	json = {"title": random_string,	"details": random_string, \
			"value": random_string, "number": randint(0, 1000), \
			"plane_id": randint(0, 4)}
	return json


def test_get_all_messages_status_code_equals_200():
	response = requests.get("http://127.0.0.1:8000/api/messages/")
	assert response.status_code == 200


def test_one_message_status_code_equals_200():
	message_id = randint(0, 1000000)
	response = requests.get("http://127.0.0.1:8000/api/messages/" + \
		str(message_id))
	assert response.status_code == 200


def test_change_values_status_code_equals_200_or_404():
	message_id = randint(0, 1000000)
	response = requests.put("http://127.0.0.1:8000/api/messages/" + \
		str(message_id), data=random_json())

	assert response.status_code in [200, 404]


def test_post_message_status_code_equals_200():
	response = requests.post("http://127.0.0.1:8000/api/messages/", \
														data=random_json())
	assert response.status_code == 200


def test_delete_message_status_code_equals_200():
	message_id = randint(0, 1000000)
	response = requests.get("http://127.0.0.1:8000/api/messages/" + \
		str(message_id))
	assert response.status_code in [200, 404]
