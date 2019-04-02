import os, sys
import cat, download, upload

# Main
if len(sys.argv) == 3:
    command = sys.argv[1]
    url = sys.argv[2]
    # switch for commands
    if command == "cat":
        cat.run(url)
    elif command == "download":
        download.run(url)
    elif command == "upload":
        upload.run(url)
    else:
        print "Invalid command"
else:
    print "Syntax: %s <command> <url>" % sys.argv[0]
