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

"""
Pull out elements of the title-article file.
"""
import sys
import os
#@lint-avoid-python-3-compatibility-imports


article_out = open(sys.argv[1] + '.article', 'w', encoding='utf-8')
title_out = open(sys.argv[1] + '.title', 'w', encoding='utf-8')

for l in open(sys.argv[1], encoding='utf-8'):
	sp = l.strip().split('\t')
	if len(sp) != 2:
		continue
	title_out.write(sp[0] + '\n')
	article_out.write(sp[1] + '\n')

title_out.close()
article_out.close()
