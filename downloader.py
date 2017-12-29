import os
import threading
import requests
from queue import Queue


class Downloader(threading.Thread):
    """Потоковый загрузчик файлов"""

    def __init__(self, queue):
        """Инициализация потока"""
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        """Запуск потока"""
        while self.queue:
            # Получаем url из очереди
            url = self.queue.get()

            count_of_tries = 0
            status = False
            while(not status or count_of_tries > 2):
                status = self.download_file(url)
                count_of_tries+=1
            # Отправляем сигнал о том, что задача завершена
            self.queue.task_done()

    def download_file(self, url):
        """Скачиваем файл"""
        response = requests.get(url, stream=True)
        fname = os.path.basename(url)
        if not fname:
            url = url.rstrip('/')
            fname += '.html'
            fname = url + fname
        if response.status_code != 200:
            return False

        with open(fname, "wb") as out_file:
            while True:
                chunk = response.raw.read(1024)
                if not chunk:
                    break
                out_file.write(chunk)
        return True



def main(urls):
    queue = Queue()

    for url in urls:
        queue.put(url)

    for i in range(5):
        t = Downloader(queue)
        t.setDaemon(True)
        t.start()

    # Ждем завершения работы очереди
    queue.join()


if __name__ == "__main__":
    urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040a.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
            "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]

    main(urls)
