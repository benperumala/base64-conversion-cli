import sys
import base64
import binascii


def usage():
    print("Usage: b64.py [encode|decode] [<string>]")
    sys.exit(1)


def encode(string):
    string = string.encode()
    payload = base64.b64encode(string)
    return payload.decode("utf-8")


def decode(string):
    try:
        string = string.encode()
        payload = base64.b64decode(string)
    except binascii.Error:
        print("'{}' is not a valid base64 string".format(string.decode("utf-8")))
        sys.exit(1)
    return payload.decode("utf-8")


def main():
    args = sys.argv
    if len(args) < 2:
        print("Error: Missing [<string>]")
    if len(args) < 3:
        usage()

    args[1] = args[1].lower()
    if args[1] == "encode":
        string = " ".join(args[2:])
        payload = encode(string)
    elif args[1] == "decode":
        string = " ".join(args[2:])
        payload = decode(string)
    else:
        usage()

    print(payload)


if __name__ == "__main__":
    main()
