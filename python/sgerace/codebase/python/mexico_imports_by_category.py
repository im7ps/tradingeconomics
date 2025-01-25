import pandas as pd
from sentence_transformers import SentenceTransformer

def country_imports_by_category():
	# Carica i dati
	data = pd.read_csv("./csv/comrade_country.csv", quotechar='"')

	# Filtro i dati per ottenere solo quelli con 'Import' e 'category' non vuota
	data = data[(data['type'] == 'Import') & (~pd.isna(data['category']))]

	# Funzione per rimuovere le virgolette (sia singole che doppie) e gestire gli spazi
	def normalize_category(category):
		if isinstance(category, str):
			# Rimuove virgolette doppie e singole all'inizio e alla fine della stringa
			category = category.strip().strip('"').strip("'")
		return category

	# Applica la normalizzazione a tutte le categorie
	data['category'] = data['category'].apply(normalize_category)

	# Filtra le righe con categorie non vuote
	categories = data['category'][data['category'] != '']

	data.reset_index(drop=True, inplace=True)
	categories.reset_index(drop=True, inplace=True)

	# Carica il modello
	model = SentenceTransformer('all-MiniLM-L6-v2')

	# Crea gli embedding
	embeddings = model.encode(categories)

	# Verifica la forma degli embedding
	print(embeddings.shape)