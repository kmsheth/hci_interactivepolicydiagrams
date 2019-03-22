import re

class results():

    def __init__(self, text):

        self.issue, self.actor = text.split(':')

        print("ACTOR: ", self.actor, " ", self.issue)

        # self.actor = actor
        # self.issue = issue


    def get_info(self):

        source_file = open("Sources.txt", "r")
        lines = source_file.read().split("\n")

        return lines


search_term = "oba"

source_file = open("Sources.txt", "r")
lines = source_file.read().split("\n")

print (lines)

r_search = r""+search_term

print(r_search)

for i in range(0, len(lines)):
    if re.search(r_search, lines[i].lower()):
        r = results(lines[i])
        #print("FOUND: ", lines[i])