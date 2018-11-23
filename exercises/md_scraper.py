## syntax: python3 md_scraper.py
## This will scrape links from each md or json file it finds in
## all subdirectories and test them via the Requests package.

import dogUtil
from pathlib import Path

pathlist = Path('.').glob('**/*.md')
for path in pathlist:
    pathStrings = str(path)
    dogUtil.md_scraper(pathStrings)

pathlist = Path('.').glob('**/*.json')
for path in pathlist:
    pathStrings = str(path)
    dogUtil.md_scraper(pathStrings)
