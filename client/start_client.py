import argparse
import logging

from pi_client import Client
from acquisitor import Acquisitor


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip', dest='address', type=str, default='127.0.0.1', help='server ip address')
parser.add_argument('-p', '--port', dest='port', type=int, default=8000, help='target port')
parser.add_argument('-e', '--endpoint', dest='endpoint', type=str, default='/data', help='target endpoint')
parser.add_argument('-s', '--https', dest='https', action='store_true')
args = parser.parse_args()

protocol = 'https' if args.https else 'http'
url = protocol + '://' + args.address + ':' + str(args.port) + args.endpoint

client = None
acquisitor = None


def setup_logger():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting measurement app...")

def setup_client():
    global client
    logging.info("Setting up http client...")
    client = Client(url)
    logging.info("Http client started")

def setup_acquisitor():
    global acquisitor
    logging.info("Setting up data acquisitor")
    acquisitor = Acquisitor(client)
    logging.info("Acquisitor ready to collect data")

def setup():
    setup_logger()
    setup_client()
    setup_acquisitor()

def shutdown_acquisitor():
    global acquisitor
    logging.info("Shutting down data acquisitor")
    acquisitor.stop()

def shutdown_client():
    global client
    logging.info("Shutting down http client")
    client.shutdown()

def shutdown():
    logging.info("Stopping measurement app...")
    shutdown_acquisitor()
    shutdown_client()
    

if __name__ == "__main__":
    setup()
    try:
        acquisitor.run()
    except KeyboardInterrupt:
        pass
    shutdown()