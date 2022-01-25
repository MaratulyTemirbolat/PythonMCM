l = [1,2,3,4,4,5,5,6,1]
set([x for x in l if l.count(x) > 1])
set([1, 4, 5])