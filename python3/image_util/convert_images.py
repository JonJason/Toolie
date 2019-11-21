import os, argparse, glob
from PIL import Image

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-f", "--format", metavar="FORMAT", required=True, help="specify the target format")
parser.add_argument("-p", "--pattern", metavar="PATTERN", required=True, help="specify the files pattern")
parser.add_argument("-c", "--copy", action="store_true", help="specify whether keep old ones or not")
args = parser.parse_args()

if not (args.copy):
    if input("Are you sure you want to delete the old images after converting?(y/n)").lower() != "y" :
        exit()
_format = args.format
for filename in glob.iglob(args.pattern):
    print(filename)
    img = Image.open(filename)
    img.save(os.path.splitext(filename)[0]+'.%s'%_format.lower(), _format)
    img.close()
    if not (args.copy):
        os.remove(filename)