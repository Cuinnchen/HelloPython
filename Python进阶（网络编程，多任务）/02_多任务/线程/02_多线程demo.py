import threading
import  time


def saysorry():
    print("soy")
    time.sleep(1)


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=saysorry)
        t.start()