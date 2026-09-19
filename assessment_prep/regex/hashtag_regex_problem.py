import re
from typing import List

from collections import Counter

tweets = ["Loving the #sunshine today", "Rainy days need #coffee and #sunshine too"]

all_hashtags = []
for tweet in tweets:
    #re.findall() -> returns a list of hashtags, so we use .extend()
    # it merges that list's items into all_hashtages one by one. 
    # if you used .append() instead, you'd end up with a list-inside-a-list
    all_hashtags.extend(re.findall(r"#\w+", tweet))
    
counts = Counter(all_hashtags)


print(counts.most_common(1))






    

