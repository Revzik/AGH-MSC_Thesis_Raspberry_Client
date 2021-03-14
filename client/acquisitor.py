import random
import time
import logging


class Acquisitor:
    def __init__(self, client):
        self.client = client
        self.running = False

    def acquire_and_send(self):
        x = random.randint(0, 100)
        logging.info("Acquired data %d, sending..." % x)
        self.client.send_data(x)

    def run(self):
        logging.info("Starting data acquisition...")
        self.running = True

        while self.running:
            start_time = time.time_ns()

            self.acquire_and_send()

            end_time = time.time_ns()
            time.sleep((1e9 + start_time - end_time) % 1e9 / 1e9)

        logging.info("Stopped data acquisition")

    def stop(self):
        self.running = False
