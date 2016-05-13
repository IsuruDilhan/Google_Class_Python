#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import zipfile

"""Copy Special exercise
"""

def copy_to(source, target):
    if not os.path.isdir(target):
        os.makedirs(target)
    paths = special_paths(source)
    for p in paths:
        shutil.copy(p, target + '/' + p)

def zip_to(source, target):
    copy_to(source,target)
    zipf = zipfile.ZipFile('copyspecial.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir(target, zipf)
    #shutil.rmtree(target)
    zipf.close()
    # cmd='py'
    # (status, output) = commands.getstatusoutput(cmd)
    # if status:
    #     sys.stderr.write(output)
    #     sys.exit(1)

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

def special_paths(dir):
  results = []
  filenames = os.listdir(dir)
  for filename in filenames:
    if re.match(r'.+\_\_\w+\_\_.+', filename):
      results.append(filename)
  return  results

def print_results(results):
    for result in results:
        print(os.path.abspath(result))

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  if todir:
    copy_to(args[0],todir)
  elif tozip:
    zip_to(args[0],tozip)
  print_results(special_paths(args[0]))

if __name__ == "__main__":
  main()
