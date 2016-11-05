import timeDuration

def getTotalEventSpan(eventName):
    file = open("Events.txt","r")
    newTS= timeDuration.TimeSpan(0,0,0)
    all_lines=file.readlines()[2:]
    for line in all_lines:
        l=line.split()
        print(l)
        if l[0] == eventName:
            if l[1][-1] == 'h':
                newTS += (timeDuration.TimeSpan(0,0,int(l[1][:-1])*(int(l[2]))))
            elif l[1][-1] == 'd':
                newTS += (timeDuration.TimeSpan(0,int(l[1][:-1])*(int(l[2])),0))
            else:
                newTS += (timeDuration.TimeSpan(int(l[1][:-1])*(int(l[2])),0,0))
    return newTS
