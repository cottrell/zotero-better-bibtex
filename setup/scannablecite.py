#!/usr/bin/env python3

from mako.template import Template

with open('zotero-odf-scan-plugin/resource/translators/Scannable Cite.js') as f:
  src = ''.join([line for line in f.readlines() if line.strip() != 'let key;'])

with open('gen/ScannableCite.ts', 'w') as f:
  f.write(Template(filename='setup/templates/Scannable Cite.mako').render(src=src))