import argparse
import logging


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('module', choices=['server', 'client'],
                        help='runs a given module')

    return parser.parse_args()


def main():
    args = parse()

    logging_format = '%(asctime)s %(levelname)s: %(message)s'
    logging_level = logging.WARNING
    logging_filename = 'server.log'
    logging.basicConfig(level=logging_level, format=logging_format)

    if args.module == 'server':
        from app import server
        server.init_server()
    else:
        from app import client
        client.init_client()


if __name__ == '__main__':
    main()
