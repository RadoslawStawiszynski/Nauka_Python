from time import gmtime, strftime, struct_time, strptime
print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))

print(strptime("30 Nov 00", "%d %b %y"))
# time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0,
#                   tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1))

