from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

monthly_challenges = {
    "january": "Eat no meat for the entire month.",
    "february": "Walk for atleast 20 minutes every day.",
    "march": "Learn Django for at least 20 minutes every day.",
    "april": "Practice the piano for 30 minutes every day.",
    "may": "Make a new friend.",
    "june": "Learn a new sport.",
    "july": "Make an origami bird.",
    "august": "Visit a national park in state.",
    "september": "Visit a national park out of state.",
    "october": "Watch a musical.",
    "november": "Watch Harry Potter movies 1 through 4 every weekend.",
    "december": "Watch Harry Potter movies 5 through 8 every weekend.",
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month - 1]

    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        return HttpResponse(monthly_challenges[month])
    except:
        return HttpResponseNotFound("This month is not supported!")
