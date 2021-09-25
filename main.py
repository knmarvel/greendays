import logging
import sys
import time

# set up logging configuration
# from https://realpython.com/python-logging/#basic-configurations
logging.basicConfig(
    level="DEBUG",
    filename='greendays.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def main(*args):
    # start up
    start_time = time.time()
    logging.info("Starting up")
    print(f"Starting up...{time.ctime(start_time)}")

    print(f"Running")

    # end
    end_time = time.time()
    logging.info(f"Stopping. Time elapsed: {end_time - start_time} seconds")
    print(f"Stopping...{time.ctime(end_time)}\nTime elapsed: {end_time - start_time} seconds")


if __name__ == "__main__":
    main(sys.argv[1:])