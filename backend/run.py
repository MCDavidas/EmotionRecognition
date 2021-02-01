import argparse


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('module', choices=['server', 'client'],
                        help='runs a given module')

    return parser.parse_args()


def main():
    args = parse()
    if args.module == 'server':
        from app import server
        server.init_server()
    else:
        from app import client
        client.init_client()


if __name__ == '__main__':
    main()
