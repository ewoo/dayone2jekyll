#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
from os.path import expanduser

def main():
  home = expanduser("~")

  fo = open(os.path.join(home, "Dropbox/dayone-to-jekyll/entries.md"), "r")

  new_entry_marker = re.compile("^\tDate:")
  count = 0
  entry = []

  for line in fo:

    match = new_entry_marker.search(line)
    if match:
      count = count + 1
      if count > 1:
          # dump entry
          print count
          process_entry(entry)
          # new entry init.
          entry = []

    entry.append(line)
  
  fo.close()


#  print lastline

def process_entry(entry):
  print entry[0]
  savefile(entry)

def build_filename_from_entry(entry):
  # Format: 2013-09-13-first-sentence-or-heading.md
  pass

def savefile(filename, content):
  pass

if __name__ == "__main__":
    main()