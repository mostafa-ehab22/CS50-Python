import sys
import csv
from bs4 import BeautifulSoup

def main():
    link, folder = get_info()




def get_info():
    default_path = r"D:\Programming\Python\CS50P csv-files"
    link = input("Input item link: ")
    save_folder = input("Saving folder path")
    
    if link == "":
        sys.exit("No link provided. Exiting...")

    if save_folder == "":
        save_folder = default_path
    
    return (link, save_folder)


if __name__ == "__main__":
    main()