import tag_crawler

keywords = ['permission', 'access', 'privilege']

tstats = tag_crawler.aggrTagStats()
for t in tstats:
  for kw in keywords:
    if kw in t:
      print t, tstats[t]