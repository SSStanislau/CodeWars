'''
You are given a link to a REST API: https://restcountries.eu/rest/v2/.
The API contains information about various countries in a json form, among others
what currency/currencies are used in a particular country. For example, in Zimbabwe (last number
on the list) there are as many as eight currencies in use. When you open the currencies rollout, there
are sections with particular currencies, each of them containing currency code, name and symbol.

Your task is to connect to the API and extract data about currencies and countries in a form of a dict.
To make it a bit more complicated, you are expected to return a dict whose keys are currency codes,
and values are lists of countries that use these currencies:

{'AED': ['United Arab Emirates'], 'AFN': ['Afghanistan'], 
'ALL': ['Albania'], ... 'CHF': ['Liechtenstein', 'Switzerland'], ... etc.}
There are valid currency codes more than three letters long, like JEP[G] or IMP[G].
Some currency codes, like Zimbabwe currency number 8, are empty. Do not include such entries
in your dict.
Have fun!
'''


import requests
import json
def countries_by_currency():
    response = requests.get('https://restcountries.eu/rest/v2/')
    content = json.loads(response.content)
    res = {}
    for i in content:
        for el in i['currencies']:
            if el['code'] in res:
                res[el['code']].append(i['name'])
            else:
                res[el['code']] = [i['name']]
    return res
