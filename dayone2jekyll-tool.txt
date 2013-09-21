Algorithm for processing DayOne markdown export:

- open file
- readlines until next "Date" entry
- transform meta lines into front matter
- grab content
- extract post title from content (first sentence)
- if photo exists, create first line on content as photo
- save file into destination

Algorithm for converting meta lines into frontmatter

- remove preceding spaces
- make lower case of property name
- convert dates into frontmatter date format
- convert tags into categories
- add hashmarks to tags