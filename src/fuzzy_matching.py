from fuzzywuzzy import process


def match_city(city, reg_city_db):
    match = process.extractOne(city, reg_city_db['city'], score_cutoff=70)
    return reg_city_db.loc[reg_city_db['city'] == match[0], 'region_code'].values[0] if match else 99


def match_city_code(city, reg_city_db):
    match = process.extractOne(city, reg_city_db['city'], score_cutoff=70)
    return reg_city_db.loc[reg_city_db['city'] == match[0], 'city_code'].values[0] if match else 0
