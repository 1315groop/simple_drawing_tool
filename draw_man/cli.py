import argparse
from drawman import Drawman


def create_parser():
    parser = argparse.ArgumentParser(description="simple draw tool")
    parser.add_argument(
        "--path",
        help="path to input and output file default current directory",
        default="input.txt output.txt",
        type=str,
    )
    args = parser.parse_args()
    if args.path:
        files = args.path.split()
        return files


def main():
    drw_man = Drawman()
    files = create_parser()
    inp = files[0]
    out = files[1]
    drw_man.draw(inp, out)

    # try:
    #    drw_man.draw(create_parser())
    # except Exception as error:
    #    print("ERROR: " + str(error))


main()
