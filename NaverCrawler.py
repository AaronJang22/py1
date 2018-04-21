from bs4 import BeautifulSoup
import urllib.request

FILE = 'naver_news.txt'

URL = "http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=215&aid=0000622323"
def get_text(URL):
    source = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source, 'lxml', from_encoding='utf-8')
    text = ''
    for item in soup.find_all('div', id='articleBodyContents'):
        text += str(item.find_all(text=True))

    return text

def main():
    open_output_file = open(FILE, 'w+')
    result_text = get_text(URL)
    open_output_file.write(result_text)
    open_output_file.close()

main()


    
