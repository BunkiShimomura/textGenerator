from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('generator/home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def search(request):
    return HttpResponse("キーワードを入力して，文章を生成する！をクリックしてください。")

def results(request):
    response = "生成されたテキストです。"
    return HttpResponse(response)
