import pandas as pd
from bs4 import BeautifulSoup


def parse_table(table):
    res = pd.DataFrame()

    id_question = 0
    link_question = ''
    date_question = ''
    question = ''
    who_asked = ''
    who_asked_id = ''
    who_asked_link = ''
    who_asked_city = ''
    answer = ''

    question_tr = table.find('tr', {'class': 'question'})
    question = question_tr.find_all('td')[1].find(
        'div').text.replace('<br />', '\n').strip()

    Widget_info = question_tr.find_all('td', {'class': 'widget_info'})
    link_question = 'https://www.banki.ru' + \ 
        Widget_info[0].find('a').get('href').strip()
    id_question = link_question.split('=')[1]

    who_asked = widget_info[1].find('a').text.strip()
    who_asked_link = 'https://www.banki.ru' + \
         Widget_info[1].find('a').get('href').strip()
    who_asked_id = widget_info[1].find('a').get('href').strip().split('=')[1]

    who_asked_city = widget_info[1].text.split('(')[1].split(')')[0].strip()

    date_question = widget_info[1].text.split('(')[1].split(')')[1].strip()
    answer_tr = table.find('tr', {'class': 'answer'})
    if answer_tr:
        answer = answer_tr.find_all('td')[1].find(
            'div').text.replace('<br />', '\n').strip

    res = res.append(pd.DataFrame([id_question,
                                   link_question, question, date_question,
                                   who_asked_city, who_asked_id, who_asked_city, answer]))

return res


