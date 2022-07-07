from time import strftime, get_clock_info, monotonic, time, gmtime


print(time())
print(get_clock_info('monotonic'))
print("1")
print(monotonic())
print("2")
print(strftime("%a, %d %b %Y %H:%M:%S"))
print("3")
print(gmtime())
print("4")
secs = 40000
obj = gmtime(secs)
print("time.struct_time object for seconds =", secs)
print(obj)
print('5')
print('time.gmtime() : %s' % gmtime())

