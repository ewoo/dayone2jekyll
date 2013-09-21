#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys
from os.path import expanduser
from entry import Entry

def run():
  home = expanduser("~")

  fo = open(os.path.join(home, "Dropbox/dayone2jekyll/samples/entries.md"), "r")

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

if __name__ == "__main__":
    sys.exit(run())