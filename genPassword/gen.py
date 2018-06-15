#!/usr/bin//env python3
import os
import string
import random


def test(message):
    userInput = input(message)
    return userInput


def main():
    length = test("How long of a password do you want? \n")
    print(length)


if __name__ == "__main__":
    main()
