import requests


def get_names_data(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print ('Returned status code: {}'.format(result.status_code))

if __name__ == '__main__':

    data = get_names_data ('http://api.data.mos.ru/v1/datasets/2009/rows?api_key=0f0726be1aaeaed6eb3a0c4872f222ea')
    for item in data:
        row = '<tr><th>%(Name)s</th><th>%(NumberOfPersons)s</th><th>%(Year)s</th><th>%(Month)s</th></tr>'
        row % item['Cells']
        print (item['Cells'])
        print ()
        print (row)
        input('aa')
