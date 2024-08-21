from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


def analyze(request):
    # get the text
    subtext = request.POST.get("text", "default")
    # make these functions off by default
    removepunc = request.POST.get("removepunc", "off")
    capitalized = request.POST.get("capitalized", "off")
    newlineremove = request.POST.get("newlineremove", "off")
    extraspaceremover = request.POST.get("extraspaceremover", "off")
    countcharacter = request.POST.get("countcharacter", "off")
    # make a condition if the functions is on
    # removing punctuation from the text
    if removepunc == "on":
        punctuations = """.  ,  ;  :  ?  !  -  --  (  )  [  ]  {  }  '  "  /  \  |  @  #  $  %  ^  &  *  _  +  =  <  >  ~  `"""
        analyze = ""
        for char in subtext:
            if char not in punctuations:
                analyze = analyze + char

        var1 = {"purpose": "Remove Punctuations", "analyzed_text": analyze}

        subtext = analyze
    # capitalized text
    if capitalized == "on":
        analyze = ""
        for char in subtext:
            analyze = analyze + char.upper()
        var1 = {"purpose": "Capitalized String", "analyzed_text": analyze}

        subtext = analyze
    # removing new line from the text
    if newlineremove == "on":
        analyze = ""
        for char in subtext:
            if char != "\n" and char != "\r":
                analyze = analyze + char
        var1 = {"purpose": "Remove New Line", "analyzed_text": analyze}

        subtext = analyze
    # extra space removes
    if extraspaceremover == "on":
        analyze = ""
        previous_char_was_space = False

        for index, char in enumerate(subtext):
            if subtext[index] == " " and subtext[index + 1] == " ":
                pass
            else:
                analyze = analyze + char

        var1 = {"purpose": "Remove extra spaces", "analyzed_text": analyze}

        subtext = analyze

    if countcharacter == "on":
        # it will tell total length of the string

        analyze = len(subtext)
        var1 = {
            "purpose": "Character Count",
            "analyzed_text": f"{subtext} Total count = {analyze}",
        }

        subtext = analyze

    if (
        countcharacter != "on"
        and extraspaceremover != "on"
        and newlineremove != "on"
        and removepunc != "on"
        and capitalized != "on"
    ):
        return HttpResponse("Error")

    return render(request, "analyze.html", var1)
