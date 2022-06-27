from bs4 import BeautifulSoup
import urllib.request
import matplotlib.pyplot as plt


def get_vaccine_num(bulletin_url):
    r = urllib.request.urlopen(bulletin_url).read()
    soup = BeautifulSoup(r, 'lxml')

    text_list = soup.get_text().split()
    vacc_num = []

    for i, word in enumerate(text_list):
        if word == 'January' or word == 'December':
            vacc_num.append(text_list[i] + ' ' + text_list[i + 1][:-1])
            break
    for i, word in enumerate(text_list):
        if word == 'immunizations':
            vacc_num.append(text_list[i - 1])
            break
    return vacc_num


def get_current_dict():
    r = urllib.request.urlopen('https://www.gov.mb.ca/covid19/vaccine/media.html').read()
    soup = BeautifulSoup(r, 'lxml')

    vacc_updates = []

    for link in soup.find_all('a'):
        if 'https' in str(link.get('href')):
            vacc_updates.append(link.get('href'))

    vacc_nums_list = {}

    for link in vacc_updates:
        if len(get_vaccine_num(link)) == 2:
            vacc_nums_list[get_vaccine_num(link)[0]] = get_vaccine_num(link)[1]

    return vacc_nums_list


def get_bar_graph(dict):
    x_value = []
    y_value = []
    for k, v in dict.copy().items():
        if not v.replace(',', '').isdigit() or v == '10,000':
            del dict[k]
    for k, v in dict.items():
        x_value.append(k)
        y_value.append(int(v.replace(',', '')))

    x_value.reverse()
    y_value.reverse()

    plt.plot(x_value, y_value, "o--b")

    plt.title("Manitoba Administered Covid Vaccines")
    plt.xlabel("Date")
    plt.ylabel("Number of Immunizations")
    plt.xticks(rotation=75)

    ax = plt.gca()
    ax.set_ylim([0, 5000])

    plt.show()


sample_dict = {'January 3': '3,432', 'January 2': '3,432', 'December 31': '3,400', 'December 30': '2,900',
               'December 29': '2,477', 'December 28': 'of', 'December 27': '2,177', 'December 24': '2,177',
               'December 23': '10,000', 'December 15': 'flu', 'December 14': 'of', 'December 13': 'COVID-19',
               'December 12': 'COVID-19'}

#get_bar_graph(sample_dict)

get_bar_graph(get_current_dict())