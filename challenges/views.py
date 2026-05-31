from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

monthly_challenges: dict[int, str] = {
    1: "Read Quran every day in January!",
    2: "Walk for at least 5km every day in February!",
    3: "Read Hadees every day in March!",
    4: "No social media in April!",
    5: "Cook a new recipe every week in May!",
    6: "30 minutes of exercise every day in June!",
    7: "Read one book in July!",
    8: "Wake up at 5am every day in August!",
    9: "Learn a new skill in September!",
    10: "Drink 2 litres of water daily in October!",
    11: "Journal every night in November!",
    12: "Practice gratitude every day in December!",
}

_month_name_to_number: dict[str, int] = {
    "january": 1,  "jan": 1,
    "february": 2, "feb": 2,
    "march": 3,    "mar": 3,
    "april": 4,    "apr": 4,
    "may": 5,
    "june": 6,     "jun": 6,
    "july": 7,     "jul": 7,
    "august": 8,   "aug": 8,
    "september": 9, "sep": 9,
    "october": 10, "oct": 10,
    "november": 11, "nov": 11,
    "december": 12, "dec": 12,
}


def index(request: HttpRequest) -> HttpResponse:
    try:
        return render(request, "challenges/index.html", {"challenges": monthly_challenges})
    except Exception:
        raise Http404("Something went wrong loading the challenges index.")


def monthly_challenge_by_number(request: HttpRequest, month: int) -> HttpResponse:
    try:
        challenge = monthly_challenges.get(month)
        if challenge is None:
            raise Http404(
                f"Month {month!r} is invalid. Enter a number between 1 and 12.")
        return HttpResponse(f"<h1>{challenge}</h1>")
    except Http404:
        raise
    except Exception:
        raise Http404("Something went wrong loading the challenge.")


def monthly_challenge(request: HttpRequest, month: str) -> HttpResponse:
    try:
        month_number = _month_name_to_number.get(month.lower())
        if month_number is None:
            raise Http404(f"{month!r} is not a valid month name.")
        return HttpResponseRedirect(reverse("challenges:month-by-number", args=[month_number]))
    except Http404:
        raise
    except Exception:
        raise Http404("Something went wrong resolving the month.")
