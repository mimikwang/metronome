import argparse
import time

from .speaker import Speaker


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--bpm", type=int, help="Beats per minute (defaults to 120)", default=120
    )
    args = parser.parse_args()

    try:
        with Speaker(bpm=args.bpm):
            while True:
                time.sleep(10)
    except KeyboardInterrupt:
        pass
