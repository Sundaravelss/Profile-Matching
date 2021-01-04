'''import hmni
matcher=hmni.Matcher(model='latin')

def fuzzy_name_matching(uname1,uname2):
    #get 2 user profile names and 
    #return 1 if the names match or 0
    match=matcher.similarity(uname1,uname2,surname_first=True,threshold=0.9,prob=True)
    return match

print(fuzzy_name_matching('sundara Vel','sundara v'))'''


from fuzzywuzzy import fuzz 

name1='Albert Thomp'
name2='Albert Thompson'

print(fuzz.ratio(name1,name2))
print(fuzz.partial_ratio(name1,name2))
print(fuzz.token_sort_ratio(name1,name2))
print(fuzz.WRatio(name1,name2))