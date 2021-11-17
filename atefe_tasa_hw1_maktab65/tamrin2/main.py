def houres_sumation(time1,time2):
    time1_list=time1.split(':')
    time2_list=time2.split(':')
    dic1={}
    dic2={}
    sum={}
    sum_minutes=0
    sum_houres=0
    for i in range(0,len(time1_list)):
        if i==0:
            dic1['houre(s)']=time1_list[i]
        elif i==1:
            dic1['minute(s)']=time1_list[i]
        elif i==2:
            dic1['second(s)']=time1_list[i]
    for i in range(0,len(time2_list)):
        if i==0:
            dic2['houre(s)']=time2_list[i]
        elif i==1:
            dic2['minute(s)']=time2_list[i]
        elif i==2:
            dic2['second(s)']=time2_list[i]

    sum_seconds=int(dic1['second(s)'])+int(dic2['second(s)'])
    if sum_seconds>=60:
        sum_seconds=sum_seconds-60
        sum_minutes+=1
    sum['second(s)']=sum_seconds
    sum_minutes+=int(dic1['minute(s)']) +int(dic2['minute(s)'])
    if sum_minutes>=60:
        sum_minutes=sum_minutes-60
        sum_houres+=1
    sum['minute(s)']=sum_minutes
    sum_houres+=int(dic1['houre(s)'])+int(dic2['houre(s)'])
    sum['houre(s)']=sum_houres
    return sum

time1=input("please enter the first time:")
time2=input("please enter the second time:")
time=houres_sumation(time1,time2)
if time['houre(s)']==0 and time['minute(s)']!=0 and time['second(s)']!=0:
    print(f"time is{time['minute(s)']}minute(s) and {time['second(s)']} second(s)")
elif time['minute(s)']==0 and time['houre(s)']!=0 and time['second(s)']!=0:
    print(f"time is{time['houre(s)']}houre(s) and {time['second(s)']} second(s)")
elif time['second(s)']==0 and time['houre(s)']!=0 and time['minute(s)']!=0:
    print(f"time is{time['houre(s)']}houre(s) and {time['minute(s)']} minute(s)")
elif time['second(s)']==0 and time['minute(s)']==0 :
    print(f"time is{time['houre(s)']}houre(s)")
elif time['houre(s)'] == 0 and time['second(s)'] == 0:
    print(f"time is{time['minute(s)']} minute(s)")
else:
    print(f"time is {time['houre(s)']} houre(s) and {time['minute(s)']} minute(s) and {time['second(s)']} second(s)")








