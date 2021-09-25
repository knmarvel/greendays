import sys
import time

def main(*args):
    start_time = time.time()
    print(f"Starting up...{time.ctime(start_time)}")
    print(f"Running")
    end_time = time.time()
    print(f"Stopping...{time.ctime(end_time)}\nTime elapsed: {end_time - start_time} seconds")


if __name__ == "__main__":
    main(sys.argv[1:])