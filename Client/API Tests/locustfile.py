from locust import HttpUser, task, between
import time
import string
import random
from random import randint


def random_json():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(randint(1,30)))

    json = {"title": random_string, "details": random_string, \
            "value": random_string, "number": randint(0, 1000), \
            "plane_id": randint(1, 4)}
    return json


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def get_all_messages(self):
        self.client.get('http://127.0.0.1:8000/api/messages/')
        time.sleep(1)

    @task
    def get_one_message(self):
        message_id = randint(0, 1000)

        with self.client.get('http://127.0.0.1:8000/api/messages/' \
            + str(message_id), catch_response=True) as response:
            if response.status_code == 404:
                response.success()

        time.sleep(1)

    @task
    def put_message(self):
        message_id = randint(0, 1000)
        # self.client.put('http://127.0.0.1:8000/api/messages/' + \
        #                      str(message_id), json=random_json())
        with self.client.put('http://127.0.0.1:8000/api/messages/' \
            + str(message_id), json=random_json(), catch_response=True) as response:
            if response.status_code == 404:
                response.success()
        time.sleep(1)

    @task
    def post_message(self):
        self.client.post('http://127.0.0.1:8000/api/messages/', \
                                                        data=random_json())
        time.sleep(1)

    @task
    def delete_message(self):
        message_id = randint(0, 1000)
        # self.client.delete('http://127.0.0.1:8000/api/messages/' \
        #                                             + str(message_id))

        with self.client.delete('http://127.0.0.1:8000/api/messages/' \
            + str(message_id), catch_response=True) as response:
            if response.status_code == 404:
                response.success()
        time.sleep(1)
