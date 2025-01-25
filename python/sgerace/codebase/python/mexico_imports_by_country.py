import matplotlib.pyplot as plt
import os
import pandas as pd

def country_imports_png():
	os.makedirs("../../data/data_png", exist_ok=True)

	data = pd.read_csv("../../assets/csv/comrade_country.csv")

	data_imported = data[data['type'] == 'Import']

	current_country = None
	country_value = 0
	x = []
	y = []

	for _i, row in data_imported.iterrows():
		if current_country != row["country2"] and current_country != None:
			x.append(current_country)
			y.append(country_value)
			country_value = row["value"]
			current_country = row["country2"]
		else:
			country_value += row["value"]
			current_country = row["country2"]

	x.append(current_country)
	y.append(country_value)

	plt.figure(figsize=(20, 10))
	plt.bar(x, y)
	plt.xlabel('Country')
	plt.ylabel('Value of imports')
	plt.xticks(rotation=75)
	plt.tight_layout()
	plt.savefig('../../data/data_png/imports.png')
	plt.close()