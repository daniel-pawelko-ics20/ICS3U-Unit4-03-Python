#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Dec 2021
# For Loops


def main():
    # main function for creating for loop program

    # asking for input
    num = input("Please enter a number: ")
    num = int(num)

    # process/output
    for i in range(num + 1):
        print(f"{i}² = {i*i}")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
