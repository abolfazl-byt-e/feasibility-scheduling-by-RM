import math
tasks = []

### get tasks

print("enter number of the tasks : ")
n = int(input())
for i in range(1, n+1):
    print("enter task", i)
    t_string = input()
    g = t_string.split(" ")
    tasks.append(g)
# print(tasks)

def utilization_of_cpu():
    u_cpu = 0
    for i in tasks:
        u = float(i[2]) / float(i[1])
        u_cpu += u
    return u_cpu

def comparison_D_and_P():
    state = 0
    for task in tasks:
        if task[3] > task[1]:
            state = 1        
    return state

def utilization_of_RM(n, delta):
    delta = delta
    n = n

    if delta >= 0 and delta <= 0.5:
        return delta

    elif delta >= 0.5 and delta <= 1:
        result =  n * (((2*delta)**(1/n))-1) + 1 - delta    
        return result

    else:
        result = (delta * (n-1)) * (((delta + 1)/(delta))**((1)/(n-1)) - 1)
        return result


def TDA(task):
    # t = t + (math.ceil(t/p) * e)
    print("check", task )
    t0 = 0
    for e in range(tasks.index(task)):
        # print("the e of task", e+1, tasks[e][2])
        t0 += float(tasks[e][2])
    # print("t0 = ", t0)
    t = t0
    e_my = float(task[2])
    # counter = 0
    while(True):
        # counter +=1
        t_old = t
        g = 0
        for j in range(tasks.index(task)):
            e = float(tasks[j][2])
            p = float(tasks[j][1])
            # print("the p of task", i+1, tasks[j][1])
            g += ((math.ceil(t/p)) * e)
        t = g + e_my
        # print("t = ", t)
        # print("t_old = ", t_old)
        if t == t_old:
            if t <= float(task[3]):
                print("max respose time of task", tasks.index(task) + 1," = ", t)
                break
            else:
                return 0


def busy_interval(task):
    print("check", task )
    t0 = 0
    for e in range((tasks.index(task))+1):
        # print("the e of task", e+1, tasks[e][2])
        t0 += float(tasks[e][2])
    # print("t0 = ", t0)
    t = t0
    while(True):
        # counter +=1
        t_old = t
        g = 0
        for j in range((tasks.index(task))+1):
            e = float(tasks[j][2])
            p = float(tasks[j][1])
            # print("the p of task", i+1, tasks[j][1])
            g += ((math.ceil(t/p)) * e)
        t = g
        # print("t = ", t)
        # print("t_old = ", t_old)
        if t == t_old:
            jobs = math.ceil(t/float(task[1]))
            # print("number of jobs :", jobs)
            break

    for job in range(1, jobs+1):
        #TODO find the best t0
        t0 = 0
        e_my = float(task[2])
        t = 0
        # counter = 0
        while(True):
            # counter +=1
            t_old = t
            g = 0
            for j in range(tasks.index(task)):
                e = float(tasks[j][2])
                p = float(tasks[j][1])
                # print("the p of task", i+1, tasks[j][1])
                g += ((math.ceil(t/p)) * e)
            t = g + ((job) * (e_my))
            # print("t = ", t)
            # print("t_old = ", t_old)
            if t == t_old:
                response_time = t - ((job-1)*(float(task[1])))
                if response_time <= float(task[3]):
                    if job == jobs:
                        print("max respose time of task", tasks.index(task) + 1, "=", t)
                    break
                else:
                    return 0



def feasibility():
    state = comparison_D_and_P()
    u_cpu = utilization_of_cpu()
    u_rm = utilization_of_RM(n, 1)
    if state == 0:
        if u_cpu <= u_rm:
            return 1
        if u_cpu > u_rm:
            # print("Lets check...")
            for task in tasks:
                s = TDA(task)
                if s == 0:
                    return s
    elif state == 1:
        for task in tasks:
            if task[3] > task[1]:
                s = busy_interval(task)
                if s == 0:
                    return 0
            else:
                s = TDA(task)
                if s == 0:
                    return 0

print("------------------------")
print("utilization of cpu = " , utilization_of_cpu())
print("utilization of rm with " , n, "tasks = " , utilization_of_RM(n, 1))


s = feasibility()
if s == 0:
    print("NOT feasible")
else:
    print("feasible")