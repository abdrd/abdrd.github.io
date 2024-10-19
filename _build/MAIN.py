import POST, INDEX, sys

def main():
    if len(sys.argv) == 2:
        POST.mdtohtml(md_path=sys.argv[1])
    elif len(sys.argv) > 2:
        sys.exit("usage: mdc optional[<markdown_file>]")
    INDEX.make_index()

if __name__ == "__main__":
    main()