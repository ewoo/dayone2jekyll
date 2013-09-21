import os
import re
from os.path import expanduser
from dateutil import parser

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
    self.__extract_title()
    self.__build_filename()

  def __parse_content(self):

    header_format = re.compile("^\t\w+:\t")

    for line in self.raw_content:
      match = header_format.search(line)
      if match:
        self.headers.append(line)
      else:
        # print "Adding content"
        self.content.append(line)

  def __reformat_headers(self):

    cleaned_headers = []
    date_header = re.compile(r"date:")

    for line in self.headers:
      line = line.replace("\t", " ")
      line = re.sub(r"^\s(\w+:)", lambda h: h.group(1).lower(), line)

      if date_header.search(line):
        self.create_date = parser.parse(line.replace("date:",""))
        line = "date: %s\n" % self.create_date.strftime("%Y-%m-%d %H:%M:%S")

      cleaned_headers.append(line)

    self.headers = cleaned_headers

  def __extract_title(self):
    
    lead_sentence = re.compile(r"^(\S.+?[.!?])(?=\s+|$)")
    
    for line in self.content:
      match = lead_sentence.search(line)
      if match:
        self.title = match.group(1)
        self.short_title = self.__smart_truncate(self.title)
        break

    title_header = "title: \"" + self.short_title + "\"\n"
    self.headers.insert(0, title_header)
    self.headers.insert(0, "layout: post\n")

  def __build_filename(self):

    esc_shortitle = self.__smart_truncate(self.short_title, 50, "")

    nonalpha = re.compile(r"(?:[^a-zA-Z0-9\- ]|(?<=['\"])s)")
    esc_shortitle = nonalpha.sub("", esc_shortitle)
    esc_shortitle = esc_shortitle.replace(" ", "-")
    self.file_name = self.create_date.strftime("%Y-%m-%d") + "-" + esc_shortitle + ".md"
    print self.file_name


  def __smart_truncate(self, content, length=100, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix

    # Massage headers. Remove beginning tabs and make lower case.
    #    for line in self.headers:

  def save(self, savepath):
    fullpath = os.path.join(savepath, self.file_name)
    fw = open(fullpath, "w")
    # Write headers in Front Matter format.
    fw.write("---\n")
    fw.writelines(self.headers)
    fw.write("---\n")
    # Wrtie blog post content.
    fw.writelines(self.content)
    fw.close()

  def print_headers(self):
    for line in self.headers:
      print line