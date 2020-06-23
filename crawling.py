from urllib.request import urlopen
from bs4 import BeautifulSoup
import threading


class AsyncTask:
    def __init__(self):
        pass

    def taskA(self):
        html = urlopen("https://www.goarmy.mil.kr:447/gtboard/hbd/hbdlist.jsp?typeID=56&boardid=219")

        bsObject = BeautifulSoup(html, "html.parser")

        for link in bsObject.find_all('td'):
            if link.text.strip() == '400':
                print("new!!!!!!")

        threading.Timer(60, self.taskA).start()


def main():
    print('Started!!')
    a = AsyncTask()
    a.taskA()


if __name__ == '__main__':
    main()
