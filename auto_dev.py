# opening the file in read mode
file = open("modern-dark.user.css", "r")
replacement = ""
# using the for loop
for line in file:
    line = line.strip()
    changes = line.replace('YouTube - Modern Dark', 'YouTube - Modern Dark Alpha(DEV BRANCH)')
    replacement = replacement + changes + '\n'


file.close()
# opening the file in write mode
fout = open("modern-dark.user.css", "w")
fout.write(replacement)
fout.close()

# opening the file in read mode
file = open("modern-dark.user.css", "r")
branch = ""


for line in file:
    line = line.strip()
    change_branch = line.replace(
        'main', 'dev')
    branch = branch + change_branch + '\n'


file.close()
# opening the file in write mode
fout = open("modern-dark.user.css", "w")
fout.write(branch)
fout.close()
