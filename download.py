from twisted.web import client
from twisted.internet import reactor
import os, tempfile

# Handler that returns the same value given as input
def returnThis(_, arg):
    return arg

def downloadToTempFile(url):
    # Given an URL, returns a Deferred object that will be called back
    # with the name of a temporary file containing the downloaded file

    tmpfd, tempfilename = tempfile.mkstemp()    # Create a tmp file
    os.close(tmpfd)

    return client.downloadPage(url, tempfilename).addCallback(returnThis, tempfilename)

def showFileName(fileName):
    print "Web page downloaded to: " + fileName
    reactor.stop()

def run(url):
    def printError(failure):
        print >> sys.stderr, "Error:", failure.getErrorMessage()

    downloadToTempFile(url).addCallback(showFileName).addErrback(printError)
    reactor.run()

# Main
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        url = sys.argv[1]
        run(url)
    else:
        print "Syntax: %s <url>" % sys.argv[0]
