#!/usr/bin/env python3
import os
import platform
import time


def base():
    system = platform.system()

    if system == "Darwin":
        home = "~"

        def systemwhat():
            print("Your system is macOS")

        def clearscr():
            os.system("clear")

        def listfiles():
            os.system("ls")

        def changedir(name):
            os.chdir(name)

        def printwd():
            os.system("pwd")

    elif system == "Windows":
        home = "%homepath%"

        def systemwhat():
            print("Your system is Windows")

        def clearscr():
            os.system("cls")

        def listfiles():
            os.system("dir")

        def changedir(name):
            os.chdir(name)

        def printwd():
            os.system("cd")

    elif system == "Linux":
        home = "/home/"

        def systemwhat():
            print("Your system is Linux")

        def clearscr():
            os.system("clear")

        def listfiles():
            os.system("ls")

        def printwd():
            os.system("pwd")

        def changedir(name):
            os.chdir(name)

    else:
        print("Your system is not detected. Exiting")
        exit()

    return home, systemwhat, clearscr, listfiles, changedir, printwd


def prompt():
    home, systemwhat, clearscr, listfiles, changedir, printwd = base()
    clearscr()
    print("Welcome to PyPrompt 1.0")
    print("")
    first_time = True

    while True:
        print("")
        if first_time:
            print("How do you want to get started?")
        else:
            print("")
            print("How do you want to continue?")

        print("")
        print("")
        print("(1) What is my system?")
        print("(2) What is my current directory?")
        print("(3) What files are in my current directory")
        print("(4) I want to change my directory")
        print("(5) I want to leave")

        answer = input("Enter your choice:")

        if answer == "1":
            clearscr()
            systemwhat()
        elif answer == "2":
            clearscr()
            printwd()
        elif answer == "3":
            clearscr()
            listfiles()
        elif answer == "4":
            clearscr()
            print("What directory to change to?")
            print("(1) Root of the file system")
            print("(2) Home directory")
            print("(3) Another directory")
            answer2 = input("Enter your choice:")
            if answer2 == "1":
                name = "/"
                changedir(name)
            elif answer2 == "2":
                name = home
                changedir(name)
            elif answer2 == "3":
                name = input("Where do you want to go?")
                changedir(name)
            else:
                print("Remaining in the same directory")
            clearscr()
            print("You are currently in:")
            printwd()
        elif answer == "5":
            clearscr()
            print("")
            print("Leaving now. Have a good day!")
            time.sleep(2)
            clearscr()
            exit()
        else:
            print("Please enter a valid option.")

        first_time = False


prompt()
