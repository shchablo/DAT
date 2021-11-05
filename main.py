import sys
sys.path.append("units")
sys.path.append("config")
from dumper import dump
from analyzer import freqСloud

def hydrogen():

    # Use Hydrogen to run this shitte code.
    print("DAT / Deep Anal of Tweets")

    path2data = "./csv/data.csv"; path2save = "./tests/"

    # Run If you want to get fresh tweets
    dump(path2data, 35, 1)

    # Next, add your units for analysis of text data and success with it,
    # or get an anal feeling with your results and do not cry!

    # Let's do simple worldcloud
    freqСloud(path2data, path2save)

def main():
    print("I'm empty")

if __name__ == "__main__":
    main()
