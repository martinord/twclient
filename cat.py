from twisted.web import client
from twisted.internet import reactor

# Event handler
def printPage(data):
    print data
    reactor.stop()

# Event handler
def printError(failure):
    print >> sys.stderr, "Error: " + failure.getErrorMessage()
    reactor.stop()

def run(url):
    # Get
    client.getPage(url).addCallback(printPage).addErrback(printError)
    reactor.run()

# Main
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        url = sys.argv[1]
        run(url)
    else:
        print "Syntax: %s <url>" % sys.argv[0]
