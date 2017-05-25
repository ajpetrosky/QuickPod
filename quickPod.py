# A quick way to install pods in a new or existing Xcode project
# Author: ajpetrosky

import os

print('Run this program in the Xcode project folder to create and install the pods.')

podfile = open('Podfile', 'w+')
while true:
    setGlobalPlatform = input('Do you want to set a global platform, i.e. \"ios, \'9.0\'\", \"ios, \'10\'\", etc.? (y/n) ')
    if setGlobalPlatform == 'y':
        podfile.write('# Project global platform')
        globalPlatform = input('Specify platform: ')
        podfile.write('platform :' + globalPlatform + '\n')
        break
    elif setGlobalPlatform == 'n':
        break

projectName = os.getcwd().split('/')[-1]
podfile.write('target ' + projectName + ' do')
podfile.write('  use_frameworks!')
podfile.write('\n  # Pods for ' + projectName)

while true:
    pod = input('Pod name to include in project (type \'x\' if no more pods to add): ')
    if pod == 'x':
        podfile.write('end')
        break
    else:
        podfile.write('  ' + pod)


podfile.close()
