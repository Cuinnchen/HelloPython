import urllib.request
import gevent
from gevent import monkey


monkey.patch_all()

def download(img_name,url):
    req = urllib.request.urlopen(url)
    img = req.read()
    with open(img_name,'wb') as f:
        f.write(img)


def main():
    gevent.joinall([
        gevent.spawn(download,'1.jpg', 'https://rpic.douyucdn.cn/live-cover/appCovers/2020/06/21/5695362_20200621173529_small.jpg/webpdy1'),
        gevent.spawn(download,'2.jpg', 'https://rpic.douyucdn.cn/live-cover/roomCover/2020/08/10/451cf5ed55b6064c85ad75224c6d3fcc_big.png/webpdy1'),
    ])


if __name__ == '__main__':
    main()
