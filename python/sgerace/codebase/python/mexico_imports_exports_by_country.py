import pandas as pd
from utils import create_folder
from mexico_imports_exports_country_by_country import country_imports_exports_country_by_country

def csv_creation():
	data = pd.read_csv("../../assets/csv/comrade_country.csv")
	data = data[["country2", "value", "type"]]

	imports = data[data["type"] == "Import"]
	exports = data[data["type"] == "Export"]

	create_folder("../../data/data_csv")
	country_imports_exports_by_country(data, imports, exports)
	country_imports_exports_country_by_country(data, imports, exports)
    

def country_imports_exports_by_country(data, imports, exports):
	country_values_imports = []

	current_country = ""
	country_value = 0

	for _i, row in imports.iterrows():
		if current_country != row["country2"]:
			current_country = row["country2"]
			country_values_imports.append(country_value)
			country_value = row["value"]
		else:
			country_value += row["value"]

	country_values_imports = pd.DataFrame(country_values_imports)
	country_values_imports.to_csv("../../data/data_csv/country_total_imports.csv")

	country_values_exports = []

	current_country = ""
	country_value = 0

	for _i, row in exports.iterrows():
		if current_country != row["country2"]:
			current_country = row["country2"]
			country_values_exports.append(country_value)
			country_value = row["value"]
		else:
			country_value += row["value"]

	country_values_exports = pd.DataFrame(country_values_exports)
	country_values_exports.to_csv("../../data/data_csv/country_total_exports.csv")

