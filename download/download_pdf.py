import re
import requests
import os, errno
import time

def get_links(filename, prefixLen, afterLen):
    pathList = []
    with open(filename) as f:
        for line in f:
            link = re.search("\"(.*)\"", line)
            if(link != None):
                name = link[0][prefixLen + 1:-1 - afterLen]
                pathList.append(name)
    return pathList

def download(pathToSave, fileList, urlPrefix):
    try:
        os.makedirs(pathToSave)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    idx = 1
    for filename in fileList:
        url = urlPrefix + filename + "pdf"
        response = requests.get(url)
        time.sleep(5)
        print (response.status_code)
        if(response.status_code == 403):
            print (response.text)
        print (url)
        path = pathToSave + "/" + str(idx) + "_" + filename + "pdf"
        with open(path, 'wb') as f:
            print (f.write(response.content))
        idx += 1


def main():
    path = "downloaded"
    urlPrefix = "https://www.tutorialspoint.com/design_pattern/pdf/"
    fileList = get_links("source.txt", 16, 3)
    download(path, fileList, urlPrefix)

if __name__ == '__main__':
    main()


