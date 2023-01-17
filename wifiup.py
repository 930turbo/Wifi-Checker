import psutil
import time
# import os
# import subprocess
import logging
import socket
from datetime import datetime

logging.basicConfig(filename='network_stats.log', level=logging.DEBUG)

def check_wifi():
    try:
        hostname = "www.google.com"
        socket.create_connection((hostname, 80), timeout=2)
        return True
    except (socket.error, socket.timeout):
        return False
    except Exception as e:
        logging.debug(str(datetime.now()) + ' Error: ' + str(e))
        return False

def get_network_stats():
    try:
        net_io_counters = psutil.net_io_counters()
        return net_io_counters
    except Exception as e:
        logging.debug(str(datetime.now()) + ' Error: ' + str(e))

def main():
    while True:
        wifi = check_wifi()
        if wifi:
            print("WiFi is working.")
            net_io_counters = get_network_stats()
            print("Bytes sent: ", net_io_counters.bytes_sent)
            print("Bytes received: ", net_io_counters.bytes_recv)
            logging.debug(str(datetime.now()) + ' WiFi is working. Bytes sent: ' + str(net_io_counters.bytes_sent) + ' Bytes received: ' + str(net_io_counters.bytes_recv))
        else:
            print("WiFi is not working.")
            logging.debug(str(datetime.now()) + ' WiFi is not working.')
        time.sleep(5)

if __name__ == '__main__':
    main()
