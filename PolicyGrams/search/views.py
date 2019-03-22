from django.shortcuts import render
import re
from .models import Issue, actor, result

# Create your views here.

force_list = [
"Single Payer Healthcare:Barack Obama",
"Universal Basic Income:Barack Obama",
"Single Payer Healthcare:Donald Trump",
"Universal Basic Income:Alexandria Ocasio-Cortez",
"Free College:Barack Obama",
"Free College:Donald Trump",
]


class results():
    def __init__(self, text):
        self.issue, self.actor = text.split(':')

    def __str__(self):
        return self.actor + " on " + self.issue

def index(request):
    print(force_list)

    # lines = result.objects.order_by()
    # print(issue_list)
    issue_list = []
    search_term = "college"

    r_search = r"" + search_term

    for i in range(0, len(force_list)):
        if re.search(r_search, force_list[i].lower()):
            issue_list.append(results(force_list[i]))

    context = {
        'issue_list':issue_list
    }
    return render(request, 'search/index.html', context)
