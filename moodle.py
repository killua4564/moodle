import requests
from bs4 import BeautifulSoup

session = requests.session()

E = [
    'https://moodle.ntust.edu.tw/course/view.php?id=18786',
    'https://moodle.ntust.edu.tw/course/view.php?id=17582',
    'https://moodle.ntust.edu.tw/course/view.php?id=18023',
    'https://moodle.ntust.edu.tw/course/view.php?id=18030',
    'https://moodle.ntust.edu.tw/course/view.php?id=18032',
    'https://moodle.ntust.edu.tw/course/view.php?id=18033',
    'https://moodle.ntust.edu.tw/course/view.php?id=18433',
    'https://moodle.ntust.edu.tw/course/view.php?id=18594'
] # course link

def init():
    global session

    data = {
        'username': '<username>',
        'password': '<password>'
    }

    login_link = 'https://moodle.ntust.edu.tw/login/index.php'
    
    session.post(login_link, data=data)
    return session

if __name__ == '__main__':  
    init()
    for link in E:
        soup = BeautifulSoup(session.get(link).text, 'html5lib')
        print(soup.select('div.page-header-headings')[0].text)
        upcoming = soup.select('div.block_calendar_upcoming.block')[0].select('div.event')
        if len(upcoming):
            for i in upcoming:
                content = i.select('a')[0]
                print(content.text, content['href'])
        else: print('Nothing here')
