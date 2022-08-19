from bs4 import BeautifulSoup

from src import init_db, Tag, db_session, Data, DataTag

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

for i in range(25000):
    filename = path + '~so_' + str(i+1) + '.html'
    data = loadData(filename)
    bs = BeautifulSoup(data, 'html.parser')
    list = bs.findAll('div', {'class':'s-post-summary'})

    for item in list:
        try:
            title = item.find('h3').text.strip()
            uri = item.find('h3').find('a', href=True)['href']
            user_uri = item.find('div', {'class':'s-user-card--link'}).find('a', href=True)['href']

            stats = item.find_all('div', {'class':'s-post-summary--stats-item'})

            vote = 0
            answer = 0
            view = 0
            for count in stats:
                if 'Score of' in count['title']:
                    vote = int(count['title'].replace('Score of ', ''))
                if 'answers' in count['title']:
                    answer = int(count.find('span', {'class':'s-post-summary--stats-item-number'}).text.strip())
                if 'views' in count['title']:
                    view = int(count['title'].replace(' views', ''))

            datetime = item.find('time', {'class':'s-user-card--time'}).find('span')['title']
            date = datetime.split(' ')[0]

            data = Data(title=title, uri=uri, user_uri=user_uri, view=view, answer=answer, vote=vote, date=date)

            db_session.add(data)
            db_session.commit()

            tags = item.find('div', {'class':'s-post-summary--meta-tags'}).text.split(' ')
            for tagNew in tags:
                tag = Tag.query.filter_by(name=tagNew.strip()).first()
                if tag is None:
                    tag = Tag(name=tagNew.strip())
                    db_session.add(tag)
                    db_session.commit()

                data_tag = DataTag(tag_id=tag.id, data_id=data.id)
                db_session.add(data_tag)
                db_session.commit()
        except:
            pass

    print (filename)
