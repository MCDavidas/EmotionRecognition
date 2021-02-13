import argparse
import logging
import yaml


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

        try:
            with open("./config.yaml", "r") as config_file:
                configuration = yaml.load(config_file, Loader=yaml.FullLoader)
        except FileNotFoundError:
            logging.error("Config not found")
            return

        try:
            if 'logging' in configuration:

                if 'level' in configuration['logging']:
                    if configuration['logging']['level'] == 'DEBUG':
                        logging_level = logging.DEBUG
                    elif configuration['logging']['level'] == 'INFO':
                        logging_level = logging.INFO
                    elif configuration['logging']['level'] == 'WARNING':
                        logging_level = logging.WARNING
                    elif configuration['logging']['level'] == 'ERROR':
                        logging_level = logging.ERROR
                    elif configuration['logging']['level'] == 'CRITICAL':
                        logging_level = logging.CRITICAL
                    else:
                        raise Exception

                logging.getLogger().setLevel(logging_level)

            host = configuration['server']['host']
            port = configuration['server']['port']

        except Exception:
            logging.error("Incorrect config file")
            return

        server.init_server(host=host, port=port)

    elif args.module == 'client':
        from app import client
        client.init_client()


if __name__ == '__main__':
    main()
