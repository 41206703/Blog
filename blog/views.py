from django.http import HttpResponse

def page_2003_view(request):
    html="hahah"
    return HttpResponse(html)