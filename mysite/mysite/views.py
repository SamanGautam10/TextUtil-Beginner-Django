# Created by Author

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    print(djtext)

    # Check which checkbox is on
    removepunc = request.POST.get('removepunc', 'off')
    fullcap = request.POST.get('fullcap', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    if removepunc == 'on':
        analyzed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Analyze Texts', 'analyzed_text': analyzed}
        djtext = analyzed

        # analyze the text
        # return render(request, 'analyze.html', params)

    # change the text to capital letter
    if (fullcap == 'on'):
        analyzed = ""

        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Change to Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed

        # analyze the text
        # return render(request, 'analyze.html', params)

    if (newlineremover == 'on'):
        analyzed = ""

        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'New line remover', 'analyzed_text': analyzed}
        djtext = analyzed

        # analyze the text
        # return render(request, 'analyze.html', params)

    if(extraspaceremover== 'on'):
        analyzed = ""

        for char in djtext:
            analyzed = analyzed + char.replace("  ", " ")

        params = {'purpose': 'Space remover', 'analyzed_text': analyzed}
        djtext = analyzed

        # analyze the text
        # return render(request, 'analyze.html', params)

    # Character counter
    elif(charcounter == 'on'):
        analyzed = 0

        for char in djtext:
            if char != ' ':
                analyzed = analyzed + 1

        params = {'purpose': 'Count Character', 'analyzed_text': analyzed}

    if (removepunc != 'on' and fullcap != 'on' and newlineremover != 'on' and extraspaceremover != 'on'
            and charcounter != 'on'):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)

print("Saman")