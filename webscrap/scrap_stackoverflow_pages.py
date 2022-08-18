from bs4 import BeautifulSoup

from src import init_db, Tag, db_session, engine, Model

path = '../data/'
init_db()

def loadData(fileName):
    with open(fileName, 'r', encoding="utf-8") as f:
        contents = f.readlines()
    f.close()

    data = ''
    for line in contents:
        data = data + line

    return data

for i in range(1):
    filename = path + '~so_' + str(i+1) + '.html'
    data = loadData(filename)
    bs = BeautifulSoup(data, 'html.parser')
    list = bs.findAll('div', {'class':'s-post-summary'})

    for item in list:
        # print(item.find('h3').text.strip())
        # print(item.find('h3').find('a', href=True)['href'])
        # print(item.find_all('div', {'class':'s-post-summary--stats-item'})[0]['title'])
        # print(item.find_all('div', {'class':'s-post-summary--stats-item'})[1]['title'])
        # print(item.find_all('div', {'class':'s-post-summary--stats-item'})[2]['title'])
        tags = item.find('div', {'class':'s-post-summary--meta-tags'}).text.split(' ')
        for tagNew in tags:
            tag = Tag.query.filter_by(name=tagNew.strip()).first()
            if tag is None:
                tag = Tag(name=tagNew.strip())
                db_session.add(tag)
                db_session.commit()
        # print(item.find('div', {'class':'s-user-card--link'}).find('a', href=True)['href'])
        # print(item.find('time', {'class':'s-user-card--time'}).find('span')['title'])
