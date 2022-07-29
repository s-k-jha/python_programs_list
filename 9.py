# Remove empty tuples from a list

def Remove(tuples):
    tuples = [t for t in tuples if t]
    return tuples

tuples = [(), ('shivam','20','2001'), (), ('kumar', 'jha'),
          ('rohan', 'shiv', '12'), ('',''),(),()]
print(Remove(tuples))