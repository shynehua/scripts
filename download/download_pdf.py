import re
import requests
import os, errno

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

        print (url)
        path = pathToSave + "/" + str(idx) + "_" + filename + "pdf"
        with open(path, 'wb') as f:
            f.write(response.content)
        idx += 1


def main():
    path = "downloaded"
    urlPrefix = "https://www.tutorialspoint.com/design_pattern/pdf/"
    fileList = get_links("source.txt", 16, 3)
    download(path, fileList, urlPrefix)

if __name__ == '__main__':
    main()


