time = input('your time > ')
# getting the time in this formm xx:xx:xx

hours = ''
minutes = ''
seconds = ''
total_seconds = ''
# making variables which we will use in future

if time[-2] == ':':
    # trying to find the ':'
    # assuming that seconds are not 2 digit number by finding the ':'
    seconds = int(time[-1])
    if time[-4] == ':':
        # assuming that minutes are not 2 digit number by finding the ':'
        minutes = int(time[-1])
        hours = int(time[:-4:])
    elif time[-5] == ':':
        minutes = int(time[-4] + time[-3])
        hours = int(time[:-5:])

    # end if


elif time[-3] == ':':
    # assuming that seconds are 2 digit number by finding the ':'
    seconds = int(time[-2] + time[-1])
    if time[-5] == ':':
        # assuming that minutes are not 2 digit number by finding the ':'
        minutes = int(time[-4])
        hours = int(time[:-5:])
    elif time[-6] == ':':
        minutes = int(time[-5] + time[-4])
        hours = int(time[:-6:])
    
    # end if

# end if

# calculating total seconds and printing it
total_seconds = hours * 3600 + minutes * 60 + seconds
print(total_seconds)





    




    