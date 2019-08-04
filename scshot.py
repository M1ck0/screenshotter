#!/usr/bin/env python

'''
Takes screeshots of screen every X seconds, stores them in folder in the active directory.
It makes folders in the active directory and gives them a name of the current date. It puts images for that date in the folder and gives them a name
of current time.

It is small and it was fun to make. Hope some of you can use it :)

MIT License

Copyright (c) [2019] [M1ck0]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
import mss
import os
from datetime import datetime
from time import sleep
import shutil

__author__ 		= " M1ck0 "
__copyright__ 	= " *** "
__credits__ 	= [ "M1ck0" ]
__license__ 	= " MIT License "
__version__ 	= " 1.0.0 "
__maintainer__ 	= " M1ck0 "
__email__ 		= " dulovicmileta1@gmail.com "
__status__ 		= " Production" 


dir_name = 'Day: ' + str(datetime.now().date())

interval = int(input('Choose interval for taking screenshots (in seconds) | eg - 60: '))

def fcount(path):

		num_of_dirs = []
		count1 = 0

		for root, dirs, files in os.walk(path):
			dirname = os.listdir(path)

		for d in dirname:
			if 'Day' in d:
				num_of_dirs.append(d)
		
		# If there are more than seven directories in the folder it removes first one
		if len(num_of_dirs) > 7:
			shutil.rmtree(num_of_dirs[0])

def on_exists(fname):

	now = datetime.now().date()

	path = "/home/m1ck0/Desktop/"

	# If directory for that date exists do not make new one, just add image to already made one
	if os.path.isdir(dir_name):
		return True
	else:
		os.mkdir('Day: ' + str(now))


while True:
	with mss.mss() as sct:
		filename = sct.shot(output = dir_name + "/%s.png" % format(datetime.now().time())[0:8], callback = on_exists)
		sleep(interval)



