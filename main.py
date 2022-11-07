import os

print('Inter folder path: ', end='')
folder = f'{input()}\\'
count = 1
for file_name in os.listdir(folder):
    source = folder + file_name
    destination = f'{folder}{str(count)}.bmp'
    print('Source:', source)
    print('Destination', destination)
    os.rename(source, destination)
    count += 1
print('All Files Renamed')

