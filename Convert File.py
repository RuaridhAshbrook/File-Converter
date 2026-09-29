import os


def GetFiles():
    # gets the filepath from the user
    filePath = input("What is the filepath?\n")
    targetExtension = input("What extension to you want to target?\n")
    newExtension = input("What is the new extension\n")
    # loops through all the files in the directory
    for file in os.listdir(filePath):
        if file.endswith(targetExtension):
            pre, ext = os.path.splitext(file)
            os.rename(filePath + "/" + file, pre + newExtension)

def main():
    GetFiles()

main()