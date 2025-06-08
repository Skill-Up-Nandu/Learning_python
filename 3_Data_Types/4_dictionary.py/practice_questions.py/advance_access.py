# Given a dictionary of country codes, write a function to find the country name for a given code.

country_code = {
    'india' : 'in', 'london' : 'lon', 'singapore' : 'sig', 'america' : 'usa'
    }

def get_country(country):
    code = country_code.get(country)
    if code:
        print(f"{code} : {country}")
    else:
        print(f"{country} not found")

get_country('singapore')
get_country('pakistan')