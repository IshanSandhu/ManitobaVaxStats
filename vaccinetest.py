from bs4 import BeautifulSoup
import urllib.request

sample_dict = {'January 3': '3,432', 'January 2': '3,432', 'December 31': '3,400', 'December 30': '2,900',
               'December 29': '2,477', 'December 28': 'of', 'December 27': '2,177', 'December 24': '2,177',
               'December 23': '10,000', 'December 15': 'flu', 'December 14': 'of', 'December 13': 'COVID-19',
               'December 12': 'COVID-19'}
for k, v in sample_dict.copy().items():
    if not v.replace(',', '').isdigit() or v == '10,000':
        del sample_dict[k]

print(sample_dict) #
