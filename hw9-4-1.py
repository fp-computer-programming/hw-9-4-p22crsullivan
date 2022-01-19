# Author: CRS 01/18/22
words = ["dog", "cat", "fish"]
def split(lst):
    var = ""
    for word in lst:
        if word != lst[len(lst) - 1]:
            var += word + " "
        else:
            var += word + " "
        print(var)
split(words)