import urllib


def read_text():
    quotes = open("resources/quotes.txt")
    content = quotes.read()
    # print(content)
    quotes.close()
    return content


def check_profanity(to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + to_check)
    output = connection.read()
    if "true" in output:
        print "Bish! There's bad words in here"
    elif "false" in output:
        print "No bad words ya bish"
    else:
        print "Your file sucks"
    connection.close()


check_profanity(read_text())
