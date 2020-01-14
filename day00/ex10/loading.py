import sys
import time

def delete_last_line():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

def ft_progress(listy, secondes):
    eta = 20
    count = 0
    for elem in listy:
        current = (elem * 100) / max(listy)
        perc = int(current)
        yo = int(perc / 4)
        bar = "=" * yo + '>'
        seconds = time.ctime().split(' ')
        seconds = seconds[3].split(':')
        timer = int(seconds[1]) * 60 + int(seconds[2]) - secondes
        print("[ETA: %ds][" % eta, perc, "% ]", bar, elem + 1, "/", max(listy) + 1, '| elapsed time : %ds' % timer)
        time.sleep(0.001)
        if (elem == max(listy)):
            break
        delete_last_line()
        yield(elem)

def loading():
    start = time.ctime().split(' ')
    start = start[3].split(':')
    secondes = int(start[1]) * 60 + int(start[2])
    listy = range(3000)
    for elem in ft_progress(listy, secondes):
        time.sleep(0.001)

if __name__ == "__main__":
    loading()
   
