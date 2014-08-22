
import os, sys



def readQuestion(question): #returns question in latexform according to example in tex folder.
    stream = open(question, "r" , encoding="utf-8")
    lines = stream.readlines()
    string = "\\textbf{\question " + lines[0] + "}\n"
    for line in lines[1:]:
        if line[0] == "#":
            string = string + "\correctchoice " + line[1:] + "\\\\\n"
        else:
            string = string + "\choice " + line + "\\\\\n"
    stream.close()
    return string

def sprgGenerator(liste):
    for name in liste:
        if name[-5:] == ".sprg": yield name

def writeTex(name):

    f = open(name, "w" , encoding="utf-8")

    header = open("./tex/header.tex" , "r" , encoding="utf-8")
    for line in header.readlines():
        f.write(line)
    header.close()

    f.write("\\begin{document}\n \\begin{questions}\n")
    questions = sprgGenerator(os.listdir("./sporgsmaal/"))

    for question in questions:
        q = readQuestion("./sporgsmaal/" + question)
        f.write(q + "\n\n")


    f.write("\end{questions}\n \end{document}")
    f.close()


if __name__ == "__main__":
    writeTex(sys.argv[1])
