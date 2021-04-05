import requests
import ast
from random import randint
from timer_wrapper import timer

class Client:

	def __init__(self):

		self.url = 'http://127.0.0.1:8000/api/messages/'
		self.response = requests.get(self.url)
		self.dict = ast.literal_eval(self.response.text)
		self.status_code = self.response.status_code


	# GET methods
	@timer
	def get_all_messages(self):
		'''return all messages each on a new line
		   return call status'''

		if len(self.dict) == 0:
			print('There are no messages!')
		
		for i in range(len(self.dict)):
			print(self.dict[i])


		if self.status_code == 200:
			print(f'\n{self.status_code} GET method called successfully!')
		elif self.status_code == 404:
			print('Url not found!')


	@timer
	def get_one_message(self, message_id):
		'''return specific message with index
		   return call status'''

		counter = 0
		for i in self.dict:
			if i['id'] == message_id:
				print(i)
			else:
				counter += 1

			if counter == len(self.dict):
				print('Message_id not found!')


		if self.status_code == 200:
			print(f'\n{self.status_code} GET method called successfully!')
		elif self.status_code == 404:
			print('Url not found!')
 		

	# PUT method
	@timer
	def change_values(self, message_id, json):
		'''change values of message
		   return call status'''
		
		self.url = 'http://127.0.0.1:8000/api/messages/' + str(message_id)
		
		payload = json

		r = requests.put(self.url, data=payload)

		if r.status_code == 200:
			print(f'Message {message_id} has been changed!')
		elif r.status_code == 404:
			print(f'Message_id {message_id} not found!')


	# POST method
	@timer
	def post_message(self, json):
		'''create message
		   return call status
		   {message: str, detials: str,	plane: str, value: str,	number: int}'''

		self.url = 'http://127.0.0.1:8000/api/messages/'

		payload = json

		r = requests.post(self.url, data=payload)

		if r.status_code == 200:
			message_title = json['title']
			print(f'Message {message_title} has been created!')
		else:
			print(f'Incorrect/missing value or incorrect format!')


	# DELETE method
	@timer
	def delete_message(self, message_id):
		'''delete message
		   return call status'''

		self.url = 'http://127.0.0.1:8000/api/messages/' + str(message_id)
		
		
		self.requests = requests.delete(self.url)

		if self.requests.status_code == 200:
			print(f'Message {message_id} getted!')
			print(f'Message_id {message_id} deleted!')
		elif self.requests.status_code == 404:
			print(f'Message_id {message_id} not found!')



<<<<<<< HEAD
=======

>>>>>>> c10969d85939bcec499abe608befe6cf7c154b9b
# for i in range(100):
# 	Client().post_message({"title": f"Message {i}",
# 							   "details": "det 20",
# 							   "value": "value 20",
# 							   "number": i + 1000,
# 							   "plane_id": randint(1, 4)})

<<<<<<< HEAD
# for i in range(930, 1010):
=======

# for i in range(250, 500):
>>>>>>> c10969d85939bcec499abe608befe6cf7c154b9b
# 	Client().delete_message(i)

# Client().change_values(455, {"title": "Message Edited"})

# Client().get_one_message(344)
# Client().get_all_messages()