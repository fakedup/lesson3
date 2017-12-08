from flask import Flask, abort, request
from req import get_weather
from names import get_names_data

from news_list import all_news

city_id = 524901
weather_apikey = '03e701b8d073c289b7940e664344d261'
mosdata_apikey = '0f0726be1aaeaed6eb3a0c4872f222ea'

app = Flask(__name__)

@app.route('/')
def index():
    url = 'http://api.openweathermap.org/data/2.5/weather?id=%s&appid=%s&units=metric' % (city_id, weather_apikey)
    weather = get_weather (url)
    result = '<p>Temperature: %s </p>' % weather['main']['temp']
    result += '<p>City: %s</p>' % weather['name']
    return result

@app.route('/hi')
def index_hi():
    return ('Hi, world!')

@app.route('/news/<int:news_id>')
def news_by_id(news_id):
    news_to_show = [news for news in all_news if news['id'] == news_id]
    if len(news_to_show) == 1:
        result = '<h1>%(title)s</h1><p><i>%(date)s</i></p><p>%(text)s</p>'
        result = result % news_to_show[0]
        return result
    else:
        abort(404)

@app.route('/news')
def all_the_news():
    limit = request.args.get('limit', 'all')
    color = request.args.get('color', 'black')
    return '<h1 style="color:%s">News: <small>%s</small></h1>' % (color, limit)

@app.route('/names')
def show_names():
    try:
        year = int(request.args.get('year'))
    except ValueError:
        year = 'all'
    names_data = get_names_data('http://api.data.mos.ru/v1/datasets/2009/rows?api_key='+mosdata_apikey)
    result = '<table><tr><th>Имя</th><th>Количество человек</th><th>Год</th><th>Месяц</th></tr>'
    for item in names_data:
        if item['Cells']['Year'] == year or year == 'all':
            result += '<tr><th>%(Name)s</th><th>%(NumberOfPersons)s</th><th>%(Year)s</th><th>%(Month)s</th></tr>'
            result = result % item['Cells']
    result += '</table>'
    return result



if __name__ == '__main__':
    app.run()