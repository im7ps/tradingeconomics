from data_creation_router import data_creation
from save_data_to_json import save_data_router
from mexico_imports_by_category import country_imports_by_category

def main():
    data_creation()
    # save_data_router('.png')
    # save_data_router('.csv')

    # country_imports_by_category()

if __name__ == '__main__':
    main()