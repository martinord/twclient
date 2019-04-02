from  twisted.web import client
from twisted.internet import reactor
import os, tempfile, webbrowser, random

def encodeMultipartForm(inputs):
    #
    # As input gets a dictionary of inputs and returns a string encoded as
    # a multipart/form-data
    #
    # First it is generated a random "boundary" of 20 chars
    getRandomChar = lambda: chr(random.choice(range(97, 123)))
    randomChars = [getRandomChar() for x in range(20)]
    boundary = "---%s---" % randomChars
    lines = [boundary] # the boundary is included as the first parameter

    # Process each input
    for key, val in inputs.items():
        header = 'Content-Disposition: form-data; name="%s"' % key
        # if the input has a name it is included
        if hasattr(val, 'name'):
            header += '; filename="%s"' % val.name # get only the name and not the complete path

        lines.append(header)

        if hasattr(val, 'read'):
            openedfile = file(val)
            lines.append(openedfile.read()) # if val is a file-like object
        else:
            lines.append(val.encode('utf-8')) # if val is a string

        lines.append('')
        lines.append(boundary) # end of each input

    return "\r\n".join(lines)  # return the encoded string


def showPage(pageData):
    tmpfd, tmp = tempfile.mkstemp('.html')
    os.close(tmpfd)
    file(tmp, 'w+b').write(pageData)
    webbrowser.open('file://' + tmp)
    reactor.stop()


def run(url):
    def handleError(failure):
        print "Error:" , failure.getErrorMessage()
        reactor.stop()

    # Just get one input in this case
    filename = raw_input("File name to upload: ")
    myinput = raw_input("Input ID in the form: ")

    form = encodeMultipartForm({myinput : filename})
    postRequest  = client.getPage(
        url,
        method='POST',
        headers={
                'Content-Type' : 'multipart/form-data; charset=utf-8',
                'Content-Length' : str(len(form))
                },
        postdata=form
    )
    postRequest.addCallback(showPage).addErrback(handleError)
    reactor.run()

# Main
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 2:
        url = sys.argv[1]
        run(url)
    else:
        print "Syntax: %s <url>" % sys.argv[0]
