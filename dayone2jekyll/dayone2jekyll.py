#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys
from os.path import expanduser
from dateutil import parser
from . import entry
import entry

def run():
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
        # Flush.
        e = Entry(entry)
        e.save(home)
        #e.print_headers()

        # Reset.
        entry = []
    entry.append(line)

  fo.close()


def process_entry(entry):
  firstline = entry[0].replace("Date:", "")
  print firstline
  ds = parser.parse(firstline)

  print entry[0]
  print ds.strftime("%Y-%m-%d") # %H:%M:%S
  savefile("", "content")


def build_filename_from_entry(entry):
  # Format: 2013-09-13-first-sentence-or-heading.md
  pass


def savefile(filename, content):
  pass


if __name__ == "__main__":
    sys.exit(run())