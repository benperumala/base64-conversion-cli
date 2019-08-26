import sys
import base64
import binascii
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--verbose', '-v', action='count')

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-e', '--encode', nargs='+', help='Convert a string to base64')
group.add_argument('-d', '--decode', help='Decode a base64 string to UTF-8')


def encode(string):
    string = string.encode()
    payload = base64.b64encode(string)
    return payload.decode("utf-8")


def decode(string):
    string = string.encode()
    try:
        payload = base64.b64decode(string)
    except binascii.Error:
        print("'{}' is not a base64 string".format(string.decode("utf-8")))
        sys.exit(1)
    return payload.decode("utf-8")


def main(args):
    if args.verbose:
        print("Namespace: {}".format(args))

    if args.encode:
        string = " ".join(args.encode)
        payload = encode(string)
    elif args.decode:
        string = " ".join(args.decode)
        payload = decode(string)

    print(payload)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
