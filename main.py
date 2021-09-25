import logging
import os
import random
import signal
import sys
import threading
import time

running = True


logging.basicConfig(
    # set up logging configuration
    # formatting from
    # https://realpython.com/python-logging/#basic-configurations
    level="DEBUG",
    filename='greendays.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def receive_signal(sig_num, frame):
    """Handler for SIGTERM, SIGQUIT, and SIGINT"""
    global running
    logging.info("Stopped by " + signal.Signals(sig_num).name)
    running = False


def push_to_git():
    logging.info("Oh I better log something")
    git_add = "git add greendays.log"
    git_commit = "git commit -m 'i logged something'"
    git_push = "git push origin main"
    os.system(f'{git_add} && {git_commit} && {git_push}')


def main(*args):
    """pushes log messages to git repository"""
    # start up
    start_time = time.time()
    logging.info("Starting up")

    print(args)

    signal.signal(signal.SIGINT, receive_signal)
    signal.signal(signal.SIGTERM, receive_signal)
    signal.signal(signal.SIGQUIT, receive_signal)

    while running:
        logging.info("Begin long running program")
        time_increment = 20
        if "test" not in args[0]:
            time_increment = random.uniform(1, 12) * 3600
        print(time_increment)
        t = threading.Timer(time_increment, push_to_git)
        t.start()

    # end
    end_time = time.time()
    logging.info(f"Stopping. Time elapsed: {end_time - start_time} seconds")

if __name__ == "__main__":
    main(sys.argv[1:])
