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
        # Flush.
        e = Entry(entry)
        e.print_headers()

        # Reset.
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
    self.content = []
    self.image = ""

    self.__parse_content()
    self.__reformat_headers()


  def __parse_content(self):

    header_format = re.compile("^\t\w+:\t")

    for line in self.raw_content:
      match = header_format.search(line)
      if match:
        self.headers.append(line)
      else:
        self.content.append(line)

  def __reformat_headers(self):

    cleaned_headers = []
    date_header = re.compile(r"date:")


    for line in self.headers:
      line = line.replace("\t", " ")
      line = re.sub(r"^\s(\w+:)", lambda h: h.group(1).lower(), line)

      if date_header.search(line):
        self.create_date = parser.parse(line.replace("date:",""))
        line = "date: %s" % self.create_date.strftime("%Y-%m-%d %H:%M:%S")

      cleaned_headers.append(line)

    self.headers = cleaned_headers

    # Massage headers. Remove beginning tabs and make lower case.
    #    for line in self.headers:

  def save(self, path):
    fw = open(os.path.join(path, self.file_name), "w")
    # Write headers in Front Matter format.
    fw.writeline("---")
    fw.writelines(self.headers)
    fw.writeline("---")
    # Wrtie blog post content.
    fw.writelines(self.content)
    fw.close()

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