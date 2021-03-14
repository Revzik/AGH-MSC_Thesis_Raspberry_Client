import requests
import logging

from concurrent.futures import ThreadPoolExecutor

class Client():
    def __init__(self, url):
        self.url = url
        self.executor = ThreadPoolExecutor(max_workers=10, thread_name_prefix='Client')

    def shutdown(self):
        self.executor.shutdown()

    def send_data(self, data):
        self.executor.submit(_send_data_async, self.url, data)


def _send_data_async(url, data):
    logging.info("Sending POST to %s..." % url)
    res = requests.post(url=url, data=data)
    logging.info("Response received, status %s" % res)
