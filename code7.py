a="Thiruvananthapuram"
print(a)
print(a.find('v'))
print(len(a))
print(a.upper())
b=""" Trivandrum is popular for the Padmanabhaswamy Temple, backwaters, and beaches.
The capital of Kerala is no longer called Trivandrum. 
The name of this city has been changed to Thiruvananthapuram from the year 1991. The new name Thiruvananthapuram means the city of Lord Anantha, 
the chief deity at the popular Sri Padmanabhaswamy Temple."""
print(len(b))
print(b.count("Kerala",20,300))
c="      The name of this city has been changed to Thiruvananthapuram     "
print(c.split())
print(c.strip())
print(c.lstrip())
print(c.replace("Thiruvananthapuram","Kerala"))
print(c)
d="I love my country."
print(d[0])
print(d[-1])
print(d[0:5])
print(d[2:6])
print(d[0:len(c)-1])
print(d[::-1])
print(d[0:-1])
print(d[-8:])
print(d[-8:-1])
e="I love"
f="my country"
print('Hi!'+d+e)
print('Hi! %s %s' %(e,f))
print('Hi! %s %s' %(f,e))
print('Hi! {1}{0}'.format(e,f))
#list
print(e.split())
q=[10,"arya",.98,10]
print(q[1])
print(type(q))
print(q[0:2])
#string +string operation
states =['Tamilnadu','Banglore','Hydrabad','jammu']
print(states)
states.append('jamshedpur')
print(states)
states.insert(1,"jammu")
print(states)
states.remove('jammu')
print(states)
# a1=states.index("Banglore")
# print(a1)
# b1=states.count('jammu')
# print(b1)
