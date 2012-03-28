import sys
from urllib.request import urlopen
from urllib.error import URLError

try:
    urlopen(sys.argv[1])
    print("The URL is valid")
except ValueError:
    print("URL is not a string, it must be a string")
except IndexError:
    print("Argument is missing")
except URLError:
    print("Impossible to load URL")
except:
    print("This error has occured", sys.exc_info()[0])
