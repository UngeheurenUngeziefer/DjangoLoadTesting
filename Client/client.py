import requests
import ast


class Client:

	def __init__(self):

		self.url = 'http://127.0.0.1:8000/api/messages/'
		self.response = requests.get(self.url)
		self.dict = ast.literal_eval(self.response.text)
		self.status_code = self.response.status_code

	# GET methods
	def get_all_messages(self):
		'''return all messages each on a new line
		   return call status'''

		for i in range(len(self.dict)):
			print(self.dict[i])

		if self.status_code == 200:
			print(f'\n{self.status_code} GET method called successfully!')
		elif self.status_code == 404:
			print('Url not found!')


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
	def post_message(self, json):
		'''create message
		   return call status'''

		self.url = 'http://127.0.0.1:8000/api/messages/'

		payload = json

		r = requests.post(self.url, data=payload)

		if r.status_code == 200:
			message_title = json['title']
			print(f'Message {message_title} has been created!')
		else:
			print(f'Incorrect or missing value!')


	# DELETE method
	def delete_message(self, message_id):
		'''delete message
		   return call status'''

		self.url = 'http://127.0.0.1:8000/api/messages/' + str(message_id)
		
		r = requests.delete(self.url)

		if r.status_code == 204:
			print(f'Message {message_id} has been deleted!')
		elif r.status_code == 404:
			print(f'Message_id {message_id} not found!')


Client().delete_message(23)
Client().get_all_messages()
