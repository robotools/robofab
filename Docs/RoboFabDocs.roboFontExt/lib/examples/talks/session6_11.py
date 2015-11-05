# robothon06
# show OpenType naming records
# in the fontlab API

from robofab.world import CurrentFont

f = CurrentFont()
fn = f.naked()

for r in fn.fontnames:
    print r.nid, r.pid, r.eid, r.lid, r.name
