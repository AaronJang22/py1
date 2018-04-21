import bs4 as bs
from urllib import request

def bugs_rank():
    sauce = request.urlopen("https://music.bugs.co.kr/chart/track/day/total?chartdate=20180420")
    '''ssoup = bs.BeautifulSoup(sauce, "lxml")

    rank = 0

    zipped = zip(soup.find_all(name="p", arttrs={"class":"title"}),
                 soup.find_all(name="p", arttrs={"class":"artist"}))

    for t, a in zipped:
        rank += 1
        print("top" + str(rank))
        print("song : " + t.find('a').text)
        print("artist : " + a.find('a').text)
'''
bugs_rank()
        
        

