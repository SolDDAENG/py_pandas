import requests
from bs4 import BeautifulSoup


class GoNaver():
    def sijak(self):
        url = "https://datalab.naver.com/keyword/realtimeList.naver?ahe=all"
        page = requests.get(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'})
        # 서비스에 접속할 수 없습니다. - 이렇게 못읽는 경우가 있다, 이렇땐 page에서 headers=~~ 붙여넣기
        soup = BeautifulSoup(page.text, 'lxml')
        # print(soup)
        title = soup.select('span.item_title')
        # print(title)
        print('네이버 실시간 검색어')
        count = 0
        for i in title:
            count += 1
            print(str(count) + "위 : " + i.string)


if __name__ == '__main__':
    GoNaver().sijak()
