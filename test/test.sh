#!/bin/bash

rm 1.mp3 2.mp3
$(dirname "$0")/../clitts.py 1.txt 1.mp3
$(dirname "$0")/../clitts.py --ssml 2.txt 2.mp3
