#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
from os.path import expanduser
from dateutil import parser

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
        #process_entry(entry)
        e = Entry(entry)
        #e.print_headers()

        # Init entry
        entry = []
      entry.append(line)
  fo.close()


#  print lastline
class Entry:
  def __init__(self, raw_content):
    self.raw_content = raw_content
    self.headers = []
    self.create_date = False
    self.title = ""
    self.short_title = ""
    self.file_name = ""
    self.content = ""
    self.image = ""
    self.__parse_content()

  def __parse_content(self):
    firstline = self.raw_content[0]
    self.create_date = parser.parse(firstline.replace("Date:", ""))

    header_format = re.compile("^\t\w+:\t")
    for line in self.raw_content:
      print line
      match = header_format.search(line)
      if match:
        self.headers.append(line)
      else:
        self.content.append(line)

    # Massage headers. Remove beginning tabs and make lower case.
    #    for line in self.headers:

  def print_headers(self):
    for line in self.headers:
      print line



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
    main()