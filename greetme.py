import sys

if len(sys.argv)==2:
    print("Knock knock, {}".format(sys.argv[1]))
else:
    sys.stderr.write("Usage: {} <name>").__format__(sys.argv[0])