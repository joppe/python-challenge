import urllib

handle = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php')
contents = handle.read()

print contents