# opening the file in read mode
file = open("modern-dark.user.css", "r")
replacement = ""
# using the for loop
for line in file:
    line = line.strip()
    changes = line.replace('Alpha(DEV BRANCH)', '')
    changes2 = line.replace('/dev/', '/main/')
    replacement = replacement + changes + '\n'
    replacement2 = replacement + changes2 + '\n'

file.close()
# opening the file in write mode
fout = open("modern-dark.user.css", "w")
fout.write(replacement)
fout.write(replacement2)
fout.close()