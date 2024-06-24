import os

def main():
    for root, directories, files in os.walk("/tmp"):
        print(f"Root: {root}")
        print(f"Directories: {directories}")
        print(f"Files: {files}")

        for _file in files:
            abs_path = os.path.join(root,_file)
            print(abs_path)


if __name__ == '__main__':
    main()