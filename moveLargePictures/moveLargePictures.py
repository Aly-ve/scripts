#!/usr/bin/python3

import shutil
import sys
import os
import time
from pathlib import Path
from PIL import Image

def create_folder(dest):
  if not os.path.exists(dest):
    os.makedirs(dest)

def get_pictures_more_than(files, min_width, min_height):
  pictures = []

  for f in files:
    try:
      im = Image.open(f)
      width, height = im.size
      if width > min_width and height > min_height:
        pictures.append(f)
    except:
      pass

  return pictures

def copy_files(pictures, dest):
  for picture in pictures:
    p = str(picture).split('/')[-1]
    shutil.copyfile(picture, os.path.join(dest, p))

if __name__ == '__main__':
  start = time.time()

  *head, path, width, height, dest = sys.argv
  width, height = int(width), int(height)

  files = [f for f in Path(path).glob('**/*.*')]
  pictures = get_pictures_more_than(files, width, height)

  create_folder(dest)
  copy_files(pictures, dest)

  end = time.time()
  diff = end - start

  print('{} files copied in {} second(s)'.format(len(pictures), diff,))
