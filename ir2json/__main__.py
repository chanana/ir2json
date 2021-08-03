"""Convert a UV File to JSON.

Takes a Bruker OPUS dotZero (*.0) file and converts it into a JSON file containing the x (cm^-1) and y (transmittance)
"""

from argparse import ArgumentParser
from ir2json import convert_to_json_ir


def main():
    parser = ArgumentParser(description="Convert Bruker OPUS to JSON file")
    parser.add_argument(
        "filenames",
        help="convert given filename(s) to json",
        nargs="+",
    )

    args = parser.parse_args()
    convert_to_json_ir.convert(args.filenames)


if __name__ == "__main__":
    main()
