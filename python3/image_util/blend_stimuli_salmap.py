import os, argparse, glob
from PIL import Image, ImageOps

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-p", "--pattern", metavar="PATTERN", required=True, help="specify the files pattern")
parser.add_argument("-m", "--map-folder", metavar="MAP_FOLDER", required=True, help="specify path to map folder")
parser.add_argument("-o", "--output-folder", metavar="OUTPUT_FOLDER", help="specify path to map folder")
args = parser.parse_args()

output_folder = (os.path.dirname(os.path.realpath(__file__)) + "/output/") if args.output_folder is None else args.output_folder

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in glob.iglob(args.pattern):
    print(filename)
    
    output_filename = filename.replace('\\', '/').split('/')[-1]
    map_filename = args.map_folder + output_filename

    with Image.open(filename).convert("RGB") as stimuli, Image.open(map_filename) as sal_map:
        masked_map = ImageOps.colorize(sal_map, "black", "red", "yellow")
        output = Image.blend(stimuli, masked_map, alpha=0.6)
        output.save(output_folder + output_filename)