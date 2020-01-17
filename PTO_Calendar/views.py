from django import template
from django.shortcuts import render, redirect, get_object_or_404
from . import utils

def index(request):
    cal = utils.Calendar(None)
    made_calendar = cal.make_calendar(2020, 1)
    calHTML = "<div class=\"row\"><div class=\"col-1 border text-center bg-secondary text-light\">Sun</div><div class=\"col-2 border text-center\">Mon</div><div class=\"col-2 border text-center\">Tue</div><div class=\"col-2 border text-center\">Wed</div><div class=\"col-2 border text-center\">Thu</div><div class=\"col-2 border text-center\">Fri</div><div class=\"col-1 border text-center bg-secondary text-light\">Sat</div></div>"

    for week in made_calendar:
        calHTML += "<div class=\"row\">"
        counter = 0
        for day in week:
            prnt_day = ""
            if day == 0:
                prnt_day = ""
            else:
                prnt_day = str(day)
            if counter == 0 or counter == 6:
                calHTML += "<div class=\"col-1 border text-left bg-secondary text-light py-4\">" + prnt_day + "</div>"
            else:
                calHTML += "<div class=\"col-2 border text-left py-4\">" + prnt_day + "</div>"
            counter += 1

        calHTML += "</div>"

    params = {
        "calendar": calHTML,
    }

    return render(request, 'pages/index.html', params)