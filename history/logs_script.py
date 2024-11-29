def inputlog(*args):
    from datetime import datetime
    log = open('history/logs.txt', 'a')
    timestring = '\n' + 'Дата: ' + str(datetime.now()) + '\n'
    log.write(timestring)
    for arg in args:
        log.write('Ввод:  ' + str(arg) + '\n')
    log.close()

def outputlog(*args):
    from datetime import datetime
    log = open('history/logs.txt', 'a')
    timestring = '\n' + 'Дата: ' + str(datetime.now()) + '\n'
    log.write(timestring)
    for arg in args:
        log.write('Вывод:  ' + str(arg) + '\n')
    log.close()
