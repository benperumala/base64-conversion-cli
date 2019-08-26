# Base64 Lightweight Conversion CLI

A lightweight program that aids in the encoding and decoding of Base64 strings.

## Argparse Version

This version uses Python's `argparse` library

### Usage:

```
b64-argparse.py [-h] [--verbose] (-e ENCODE [ENCODE ...] | -d DECODE)
optional arguments:
  -h, --help            show this help message and exit
  --verbose, -v
  -e ENCODE [ENCODE ...], --encode ENCODE [ENCODE ...]
                        Convert a string to base64
  -d DECODE, --decode DECODE
                        Decode a base64 string to UTF-8
```

## Simplified Version

A version which does the same thing but specifies decode/encode without `-` in front (since it's not really an optional argument)

### Usage:

```
b64-simplified.py [encode|decode] [<string>]
```
