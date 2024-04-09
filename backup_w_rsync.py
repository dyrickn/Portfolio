#!/usr/bin/env python
import subprocess
from multiprocessing import Pool
import os

src = "~/source"
dest = "~/destination"

def run(dir):
  #Remote Sync
  subprocess.call(["rsync", "-arq", dir, dest])
  print("Handling Folder: {}".format(dir))

if __name__ == "__main__":
  filelist = [os.path.join(src, file) for file in os.listdir(src)]
  p = Pool(len(filelist))
  p.map(run, filelist)