import os, argparse, glob
from shutil import copyfile, move

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-p", "--pattern", metavar="PATTERN", required=True, help="specify the files pattern")
parser.add_argument("-s", "--separator", metavar="SEPARATOR", required=True, help="specify the files pattern")
parser.add_argument("-dc", "--default-category", metavar="DEFAULT", default="default", help="specify default category")
parser.add_argument("-d", "--depth", metavar="DEPTH", default=1, help="specify category depth")
parser.add_argument("-c", "--copy", action="store_true", help="specify whether keep old ones or not")
args = parser.parse_args()

if not (args.copy):
    if input("Are you sure you want to delete the old images after converting?(y/n)").lower() != "y" :
        exit()

_separator = args.separator
_depth = args.depth
_dc = args.default_category.split(_separator)
_dc.extend([_dc[-1]] * (_depth - len(_dc)))
dir_sep = "\\"
for filename in glob.iglob(args.pattern):
    d, f = filename.split(dir_sep, 1)
    subs = f.split(dir_sep)
    f = subs[-1]
    n, ex = os.path.splitext(f)
    p = n.split(_separator, _depth)
    s = len(p)

    if s <= _depth:
        for i in range(s-1,_depth):
            p.append(_dc[i])

    lego = [d]
    if len(subs) > 1:
        lego.extend(subs[:-1])
    lego.extend(p[1:])
    d = dir_sep.join(lego)
    if not os.path.exists(d):
        os.makedirs(d)
    new_filename = d + dir_sep + p[0] + ex
    print(filename)
    if args.copy:
        copyfile(filename, new_filename)
    else:
        move(filename, new_filename)