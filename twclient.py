import sys, cat

# Main
if len(sys.argv) == 3:
    command = sys.argv[1]
    url = sys.argv[2]
    # switch for commands
    if command == "cat":
        cat.run(url)
    else:
        print "Invalid command"
else:
    print "Syntax: twclient.py <command> <url>"
