#
#  Copyright (c) 2015, Facebook, Inc.
#  All rights reserved.
#
#  This source code is licensed under the BSD-style license found in the
#  LICENSE file in the root directory of this source tree. An additional grant
#  of patent rights can be found in the PATENTS file in the same directory.
#
#  Author: Alexander M Rush <srush@seas.harvard.edu>
#          Sumit Chopra <spchopra@fb.com>
#          Jason Weston <jase@fb.com>

#/usr/bin/env python

import sys
import os
import re
import gzip
#@lint-avoid-python-3-compatibility-imports

# Make directory for output if it doesn't exist

base_filename = os.path.basename(sys.argv[1]) 
try:
    os.mkdir(sys.argv[2])
except OSError:
    pass

out = open(sys.argv[2] + os.sep + base_filename[:-len('.gz')] + '.txt', 'w', encoding='utf-8')

# Parse and print titles and articles
NONE, HEAD, NEXT, TEXT = 0, 1, 2, 3
MODE = NONE
title = ""
article = []

for l in gzip.open(sys.argv[1]):
    l = str(l, 'utf-8').strip()

    if MODE == TEXT and l == "</P>":
        articles = ' '.join(article)
        #title \t article
        out.write(title)
        out.write('\t')
        out.write(articles)
        out.write('\n')
        article = []
        MODE = NONE
        continue

    if MODE == HEAD:
        title = l
        MODE = NEXT
        continue

    if MODE == TEXT:
        article.append(l)
        continue

    if MODE == NONE and l == "<HEADLINE>":
        MODE = HEAD
        continue

    if MODE == NEXT and l == "<P>":
        MODE = TEXT
        continue


out.close()
