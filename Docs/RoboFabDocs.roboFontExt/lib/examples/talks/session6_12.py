# robothon06
# show encoding 

from robofab.world import CurrentFont

f = CurrentFont()
fn = f.naked()

# object containing encoding records.
# you can iterate through it by using an index.
print fn.encoding

for i in range(len(fn.encoding)):
    er = fn.encoding[i]
    print er, er.name, er.unicode
