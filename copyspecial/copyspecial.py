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
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
  paths = []
  for p in os.listdir(dir):
    m = re.search(r"__\w+__", p)
    if m: paths.append( os.path.join( os.path.abspath(dir), p ) )
  return paths

def copy_to(paths, dir):
  if not os.path.exists(dir): os.makedirs(dir)
  for p in paths:
    shutil.copy(p, dir)

def zip_to(paths, zipPath):
  #command = ["zip", "/?"]
  command = ["zip", "-j", zipPath] + paths
  print( "Command to be done:", command)
  try:
    subprocess.check_call(command)
  except subprocess.CalledProcessError as e:
    sys.stderr.write( "returncode: " + str(e.returncode)
                     + "\noutput: " + str(e.output) )
    #sys.stderr.write("sadface")
    sys.exit(1)
  except:
    sys.stderr.write("No compatible exception found.")
    sys.exit(1)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print( "usage: [--todir dir][--tozip zipfile] dir [dir ...]" )
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
    print( "error: must specify one or more dirs" )
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  paths = []
  for dir in args:
    paths.extend( get_special_paths(dir) )
  print("Special files:")
  for p in paths:
    print(p)
  print()

  if todir:
    copy_to(paths, todir)

  if tozip:
    zip_to(paths, tozip)

  
if __name__ == "__main__":
  main()
