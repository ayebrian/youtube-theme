# opening the file in read mode
file = open("modern-dark.user.css", "r")
replacement = ""
# using the for loop
for line in file:
    line = line.strip()
    changes = line.replace('Alpha(DEV BRANCH)', '')
    replacement = replacement + changes + '\n'

file.close()
# opening the file in write mode
fout = open("modern-dark.user.css", "w")
fout.write(replacement)
fout.close()