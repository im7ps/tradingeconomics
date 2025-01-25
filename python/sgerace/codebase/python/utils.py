import os

def create_folder(folder_path:str):
	if not os.path.exists(folder_path):
		os.makedirs(folder_path)