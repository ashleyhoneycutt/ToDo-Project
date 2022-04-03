# CommandLine Todo application
# =============================

############### Print usage
commandLine = """
Command line arguments:
    -l   Lists all the tasks
    -a   Adds a new task
    -r   Removes an task
    -c   Completes an task
"""
print(commandLine)

############### List tasks
# todo -l

# 1 - Walk the dog
# 2 - Buy milk
# 3 - Do homework

list_of_tasks = []


def init():
    fileGet = open('tasks.txt', 'r')
    tasks = fileGet.readlines()
    for i in tasks:
        list_of_tasks.append(i)

def save():
    fileGet = open('tasks.txt', 'w')
    for i in list_of_tasks:
        fileGet.write(i)
    fileGet.close()


def list_task():
    if len(list_of_tasks) == 0:
        print("No Tasks for today")
    else:
        print(list_of_tasks)


def add_task():
    wl = input('Please choose a to do task: ')
    if wl == "":
        print("Unable to add: no task provided")
    else:

        lenArr = len(list_of_tasks) + 1
        file = open('tasks.txt', 'w')
        list_of_tasks.append(f'{lenArr} - {wl} []')


def remove_task():
    for u in list_of_tasks:
        print(u)
    w = input('Please choose a task to remove: ')
    w = int(w) - 1
    list_of_tasks.pop(w)
    print(list_of_tasks)


# for w in list_of_tasks:
#      file.write(w)
# file.close()
# print(list_of_tasks)


while True:
    init()
    w = input('Please choose a command: ')

    # def complete_task():
    #     w = int(input('Enter the number of the completed task: '))
    #     if w == "":
    #         print("Unable to complete task")
    #     for i in list_of_tasks:
    #         if w == list_of_tasks[i]:
    #             print(f'{i+1} - {w} [X]')
    #         else:
    #             print('Task not recognized')

    if w == '-l':
        list_task()
    if w == '-a':
        add_task()
    if w == '-r':
        remove_task()
    # if w == '-c':
    # complete_task()
