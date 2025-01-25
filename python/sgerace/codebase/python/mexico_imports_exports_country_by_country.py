from utils import create_folder

def country_imports_exports_country_by_country(data, imports, exports):
	create_folder("../../data/data_csv/imports")
	create_folder("../../data/data_csv/exports")

	countries = []
	for country in data["country2"]:
		if country not in countries:
			countries.append(country)

	for country in countries:
		data = imports[imports["country2"] == country]
		data.to_csv(f"../../data/data_csv/imports/{country}_imports.csv")


	for country in countries:
		data = exports[exports["country2"] == country]
		data.to_csv(f"../../data/data_csv/exports/{country}_exports.csv")
