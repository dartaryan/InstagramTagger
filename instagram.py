import pyautogui
import time
import random
import datetime


def min2sec_delay(time_min):
    return time.sleep(time_min * 60)
points=list(pyautogui.position())
time.sleep(4)
print(points)
pyautogui.moveTo(points[0],points[1],duration=2)
names = ["@gavrieldouk","@vered_vd","@alonrapo","@asifpz","@elirantyu","@talyber","@salman.kher", "@galelbaz_", "@barbenzion", "@ladymey", "@tripicsee", "@shaharbitton31","@nir_volo"]
#
hours = 8
min_counter = 0
names_hours = []
count_names = []
for name in names:
    count_names.append([name, 0])
while min_counter < (hours * 60):
    currentDT = datetime.datetime.now()
    pyautogui.moveTo(points[0],points[1],duration=2)
    pyautogui.click(points[0],points[1])
    time.sleep(1)
    account = random.choice(names)
    count_names[names.index(account)][1] += 1
    pyautogui.typewrite(account)
    print(currentDT.strftime("%H:%M:%S"))
    print("user: ", account)
    print("--------")
    print("--------")
    pyautogui.typewrite(['enter'])
    waiting_time = random.randrange(1, 2, 1)     # real one
    # waiting_time = random.randrange(1, 3, 1)       # checking
    print("wait: ", waiting_time)
    min_counter += waiting_time
    print("counter: ", min_counter)
    stamp = str(currentDT.strftime("%H:%M:%S")) + " ► " + account
    names_hours.append(stamp)
    min2sec_delay(waiting_time)     # real one
    #time.sleep(waiting_time)      # checking

print("---------")
print("Finished commenting at ", currentDT.strftime("%H:%M:%S"))
print("---------")
for count in count_names:
    print(count[0], " : ", count[1])

print("--------------")
sums=0
for sum_counts in count_names:
    sums= sums + sum_counts[1]

print("Total counts : ", sums)

print("--------------")
for count in names_hours:
    print(count)
