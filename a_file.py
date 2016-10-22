print "This is a test to see if I can push a project to github"

f_in = open("input.txt", "r")

print "file open sucessful"

content = f_in.readlines()

print "file read sucessful"

print "Let's print some numbers!"

for number in content:
    print int(number)*3

print "Done printing numbers!"
