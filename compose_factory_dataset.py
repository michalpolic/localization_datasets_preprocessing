from os import listdir
from os.path import isfile, join

in_train_dir = "/local/artwin/data/SiemensScans/generated_cutouts/train"
in_val_dir = "/local/artwin/data/SiemensScans/generated_cutouts/val"
out_train_dir = "/local/artwin/localization/Hierarchical-Localization/datasets/factory_from_scan/db"
out_val_dir = "/local/artwin/localization/Hierarchical-Localization/datasets/factory_from_scan/query"

# copy training images 
for f in listdir(in_train_dir):
    file_path = join(in_train_dir, f)
    if isfile(file_path) and "reference.png":
        pass
