from django.http import HttpResponse

def test_html(request):
    html="hahah"
    return HttpResponse(html)