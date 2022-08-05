## Directories for landsat data may have extra characters on the end due to earlier failed downloads

import sys
import pathlib

def rename_dirs(in_dir:str)-> None:
    """Remove the trailing '(n)' suffix from directories within in_dir"""
    in_path = pathlib.Path(in_dir)

    for i, path in enumerate(in_path.iterdir()):

        new_name = str(path).split(' ')[0]
        path.rename(new_name)
    print(f"Renamed {i+1} directories in {in_dir}")


if __name__ == "__main__":

    in_dir = sys.argv[1]

    rename_dirs(in_dir)

    