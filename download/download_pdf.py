import re
import os, errno
import urllib.request

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
        print (url)
        # add user agent to http header, to avoid 403 forbidden error
        send_headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0)',
        }
        req = urllib.request.Request(url,headers=send_headers)
        pdfFile = urllib.request.urlopen(req)


        path = pathToSave + "/" + str(idx) + "_" + filename + "pdf"
        with open(path, 'wb') as f:
            #print (f.write(response.content))
            f.write(pdfFile.read())
        idx += 1


def main():
    path = "downloaded"
    urlPrefix = "https://www.tutorialspoint.com/design_pattern/pdf/"
    fileList = get_links("source.txt", 16, 3)
    download(path, fileList, urlPrefix)

if __name__ == '__main__':
    main()


