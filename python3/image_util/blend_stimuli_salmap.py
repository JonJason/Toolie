import os, argparse, glob
from PIL import Image, ImageOps
from pathlib import Path

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-p", "--pattern", metavar="PATTERN", required=True, help="specify the files pattern")
parser.add_argument("-m", "--map-folder", metavar="MAP_FOLDER", required=True, help="specify path to map folder")
parser.add_argument("-o", "--output-folder", metavar="OUTPUT_FOLDER", help="specify path to map folder")
parser.add_argument("-d", "--depth", metavar="DEPTH", type=int, default=0, help="specify category depth")
args = parser.parse_args()

output_folder = (os.path.dirname(os.path.realpath(__file__)) + "/output/") if args.output_folder is None else args.output_folder

for filename in glob.iglob(args.pattern):
    print(filename)
    
    output_filename = "/".join(filename.replace('\\', '/').split('/')[-(args.depth + 1):])
    map_filename = args.map_folder + output_filename

    with Image.open(filename).convert("RGB") as stimuli, Image.open(map_filename) as sal_map:
        masked_map = ImageOps.colorize(sal_map, "black", "red", "yellow")
        output = Image.blend(stimuli, masked_map, alpha=0.6)
        path = Path(output_folder + output_filename)
        
        if not os.path.exists(path.parent):
            os.makedirs(path.parent)
        output.save(output_folder + output_filename)