# Python Program to handle missing keys in Python dictionaries
country_code = {'India' : '0091',
                'Pakistan' : '0025',
                'Australia' : '00977'}
print(country_code.get('India', 'Not Found'))
 
print(country_code.get('russia', 'Not Found'))