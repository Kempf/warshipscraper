## Dependencies
matplotlib, pandas, ???

## Usage
+ Set up your Reddit API in __auth.py__ 
+ __scrape.py__ (set __num__ to how many submissions to download) to generate __data.csv__ file
+ __titlegen.py__ (this used to do some NLP but now it just removes resolutions) to generate __titles.csv__
+ __country.py__ to categorize titles (see __titles_unsorted.csv__ for stuff it missed)
+ __view_stats.py__ outputs fancy plots