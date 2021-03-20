import random
import time
import logging
import numpy as np


class Acquisitor:
    def __init__(self, client):
        self.client = client
        self.running = False

    def acquire_and_send(self):
        x = np.random.rand(1024)
        logging.info("Acquired data, sending...")
        self.client.send_ndarray(x)

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
