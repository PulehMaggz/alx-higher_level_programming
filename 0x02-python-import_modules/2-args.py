#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]  # Get arguments excluding the script name
    argc = len(argv)

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
        print(f"1: {argv[0]}")
    else:
        print(f"{argc} arguments:")
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")
