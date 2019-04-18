from django.shortcuts import render
import re
from .models import Issue, actor, result
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.

force_list = [
"Single Payer Healthcare:Barack Obama",
"Universal Basic Income:Barack Obama",
"Single Payer Healthcare:Donald Trump",
"Universal Basic Income:Alexandria Ocasio-Cortez",
"Free College:Barack Obama",
"Free College:Donald Trump",
"Single Payer Healthcare:Alexandria Ocasio-Cortez",
"Single Payer Healthcare:Bernie Sanders"
]


class results():
    def __init__(self, text):
        self.issue, self.actor = text.split(':')
        self.headshot = "Headshot_"+self.actor+".svg"

    def __str__(self):
        return self.actor + " on " + self.issue

class policygram():
    def __init__(self, name, issue):
        self.name = name
        self.issue = issue



def index(request):

    search_term = ""
    issue_list = []

    # TODO Replace '+' with ' '

    if request.method == "POST":
        full_str = request.body.decode("utf-8")
        print(request.body.decode("utf-8"))
        query = full_str.split("newquery=", 1)[1]
        search_term = query
    else:
        print("NO POST")


    r_search = r"" + search_term

    if r_search != "":
        for i in range(0, len(force_list)):
            if re.search(r_search, force_list[i].lower()):
                issue_list.append(results(force_list[i]))

    context = {
        'issue_list':issue_list,
        'search_term':search_term
    }

    return render(request, 'search/index.html', context)

def issue(request):

    if request.method == "POST":
        full_str = request.body.decode("utf-8")
        full_query = full_str.split("name=", 1)[1]
        name = full_query.split("%2C")[0]
        issue = full_query.split("%2C")[1]
        name = name.replace('+', ' ', 10)
        issue = issue.replace('+', ' ', 10)

    else:
        print("NO POST")
        name = "Barack Obama"
        issue = "Single Payer Healthcare"


    p = policygram(name, issue)

    context = {
        'policygram' : p
    }

    return render(request, 'search/issue_final.html', context)


def home(request):


    context = {

    }

    return render(request, 'search/home.html', context)
