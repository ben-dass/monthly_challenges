from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
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
    "december": None,
    # "december": "Watch Harry Potter movies 5 through 8 every weekend.",
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(
        request,
        "challenges/index.html",
        {
            "months": months,
        },
    )


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month!</h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {
                "month_name": month,
                "text": challenge_text,
            },
        )
    except:
        raise Http404()
