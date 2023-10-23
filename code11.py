#Dictonary
a={100:'moolya',2:'moolyaed'}
print(a[100])
print(a)
b={'moolya':100,'moolyaed':2}
print(b['moolya'])
print(b)
c={'a':'arya','b':'harya'}
print(c['a'])

#method in dictonary
a[3]='moon'
print(a)
b['s']='hello'
print(b)
#get
print(a.get(3))
print(a.pop(100))
a.update({3:'sun'})
print(a)
print(a.popitem())
print(a)