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

import sys
#@lint-avoid-python-3-compatibility-imports

article_out = open(sys.argv[1] + '.filter', 'w', encoding='utf-8')
title_out = open(sys.argv[2] + '.filter', 'w', encoding='utf-8')

dedup = set()

with open(sys.argv[1], encoding='utf-8') as article_in, open(sys.argv[2], encoding='utf-8') as title_in:
    for article, title in zip(article_in, title_in):
        article = article.strip()
        title = title.strip()
        title_words = title.split()
        article_words = article.split()
    
        # No blanks.
        if any((word == "" for word in title_words)):
            continue
    
        if any((word == "" for word in article_words)):
            continue
    
        if not any((word == "." for word in article_words)):
            continue
    
        # Spurious words to blacklist.
        # First set is words that never appear in input and output
        # Second set is punctuation and non-title words.
        bad_words = ['update#', 'update', 'recasts', 'undated', 'grafs', 'corrects',
                     'retransmitting', 'updates', 'dateline', 'writethru',
                     'recaps', 'inserts', 'incorporates', 'adv##',
                     'ld-writethru', 'djlfx', 'edits', 'byline',
                     'repetition', 'background', 'thruout', 'quotes',
                     'attention', 'ny###', 'overline', 'embargoed', 'ap', 'gmt',
                     'adds', 'embargo',
                     'urgent', '?', ' i ', ' : ', ' - ', ' by ', '-lrb-', '-rrb-']
        if any((bad in title.lower()
                for bad in bad_words)):
            continue
    
        # Reasonable lengths
        if not (10 < len(article_words) < 100 and
                3 < len(title_words) < 50):
            continue
    
        # Some word match.
        matches = len(set([w.lower() for w in title_words if len(w) > 3]) &
                      set([w.lower() for w in article_words if len(w) > 3]))
        if matches < 1:
            continue
        k = article + ' ' + title
        if k in dedup:
            continue
        # Okay, save it.
        dedup.add(k)
        article_out.write(article + '\n')
        title_out.write(title + '\n')

print(str(len(dedup)) + ' duplicates')
article_out.close()
title_out.close()

