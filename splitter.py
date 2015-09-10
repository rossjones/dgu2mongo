import json

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


count = 0
print "Loading ...."
blob = json.load(open('data.gov.uk-ckan-meta-data-2015-09-09.json'))
print "Splitting ...."
for part in chunks(blob, 1000):
    count += 1
    print "Writing out chunk ", count
    fname = 'pkgs/{count}.json'.format(count=count)
    with open(fname, 'wb') as f:
        f.write(json.dumps(part))
