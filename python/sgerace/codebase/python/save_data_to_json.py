import os
import json

def save_data_router(extension):
	base_path = os.path.join('assets', 'data')
	for folder in os.listdir(base_path):
		folder_path = os.path.join(base_path, folder)
		if os.path.isdir(folder_path):
			save_data_to_json(folder_path, extension)


def save_data_to_json(folder_path:str, extension:str):
	if not folder_path:
		raise FileNotFoundError(f"The directory {folder_path} does not exist")

	try:
		plots = []
		for file in os.listdir(folder_path):
			if file.endswith(extension):
				file_path = os.folder_path.join(folder_path, file)
				if os.folder_path.isfile(file_path) and os.access(file_path, os.R_OK):
					plots.append({"title": os.folder_path.splitext(file)[0], "src": file_path})
				else:
					print(f"The file {file_path} is not readable or is corrupted.")
		
		if not plots:
			raise ValueError("No valid files found in the directory")
		
		# Salva i dati in un file JSON
		with open("plot_data.json", "w") as json_file:
			json.dump(plots, json_file)

	except ValueError as e:
		print(f"Error saving the files, value error: {e}")
	except Exception as e:
		print(f"Error saving the files: {e}")

