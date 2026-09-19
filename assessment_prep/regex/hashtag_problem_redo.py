from collections import Counter
import re

" Find the most hastagged word"

tweets = ["Loving the #sunshine today", "Rainy days need #coffee and #sunshine too"]

hashtags = []

for tweet in tweets:
    x = re.findall(r"#\w+", tweet)
    hashtags.extend(x)

counts = Counter(hashtags)


print(counts.most_common(1))



print("".join(["a", "b", "c"]))