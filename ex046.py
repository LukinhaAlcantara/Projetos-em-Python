from time import sleep

for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('\033[2; 31mBOOOM\033[m')
