#!/usr/bin/python3
import sys
import os

def progress(blockNum, blockSize, totalSize):
    read = blockNum * blockSize
    if totalSize > 0:
        percent = read * 100 / totalSize
        s = "\r%5.0f%% " % (percent)
        sys.stderr.write(s)
        if read >= totalSize:
            sys.stderr.write("\n")
    else:
        sys.stderr.write("read %d\n" % (read,))

urls = ['https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names',
        'https://pjreddie.com/media/files/yolov3.weights']

for url in urls:
    filename = url[url.rfind("/") + 1: ]
    print ('Downloading ' + filename)
    if sys.version_info.major > 2:
        import urllib.request
        urllib.request.urlretrieve(url, os.path.join("../tensorflow-yolo-v3", filename), progress)
    else:
        import urllib
        urllib.urlretrieve(url, os.path.join("../tensorflow-yolo-v3", filename), progress)
