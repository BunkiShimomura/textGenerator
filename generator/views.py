from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import redirect, render

from .models import Query, SampleText, GeneratedText, PrepareChain, GenerateText

def home(request):
    template = loader.get_template('generator/home.html')
    context = {}
    return HttpResponse(template.render(context, request))

def search(request):
    return HttpResponse("キーワードを入力して，文章を生成する！をクリックしてください。")

def results(request):
    if request.method == 'GET':
        text = request.GET.get('your_name')
        chain = PrepareChain(text)
        triplet_freqs = chain.make_triplet_freqs()
        chain.save(triplet_freqs, True)

        numb_sentence = int(sentences) #文章の数

        generator = GenerateText()
        gen_txt = generator.generate()

        return gen_txt


    data = {
        'your_name': request.GET.get('your_name')
    }


    return render(request, 'generator/home.html', gen_txt)

    '''
    return HttpResponse("キーワードを入力して，文章を生成する！をクリックしてください。")

    template = loader.get_template('generator/result.html')
    context = {}
    return HttpResponse(template.render(context, request))
    '''
def export_txt(request):
    response = ""
