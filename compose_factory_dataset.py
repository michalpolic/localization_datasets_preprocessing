from os import listdir
from os.path import isfile, join
from shutil import copyfile
from pathlib import Path

in_train_dir = "/local/artwin/data/SiemensScans/generated_cutouts/train"
in_val_dir = "/local/artwin/data/SiemensScans/generated_cutouts/val"
out_dir = "/local/artwin/localization/Hierarchical-Localization/datasets/factory_from_scan"
out_train_dir = out_dir + "/db"
out_val_dir = out_dir + "/query"

Path(out_train_dir).mkdir(parents=True, exist_ok=True)
Path(out_val_dir).mkdir(parents=True, exist_ok=True)

# copy training images 
for f in listdir(in_train_dir):
    in_file_path = join(in_train_dir, f)
    if isfile(in_file_path) and in_file_path[-13:] == "reference.png":
        copyfile(in_file_path, join(out_train_dir, f))

# copy validation images 
for f in listdir(in_val_dir):
    in_file_path = join(in_val_dir, f)
    if isfile(in_file_path) and in_file_path[-13:] == "reference.png":
        copyfile(in_file_path, join(out_val_dir, f))

# create the calibration txt files 
# TODO: load json params -> save then into intrinsic file
intrinsic_file = open(out_dir + "/queries_with_intrinsics.txt", "w")
for img_file in listdir(in_val_dir):
    intrinsic_file.write(f"query/{img_file} SIMPLE_PINHOLE 1344 756 1163.938 672 378")
intrinsic_file.close()