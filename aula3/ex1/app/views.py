from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from lxml import etree


# Create your views here.
def cursos(request):
    tree = etree.parse("app/xml_files/cursos.xml")
    info = dict()
    cursos = tree.xpath('//curso')
    for c in cursos:
        info[c.find('guid').text] = c.find('nome').text

    tparams = {
        'cursos': info
    }

    return render(request, 'cursos.html', tparams)


def curso_details(request, curso_name):
    tree = etree.parse("app/xml_files/cursos.xml")
    info = dict()
    cursos = tree.xpath('//curso/[@guid=curso_name]')
    for c in cursos:
        info[c.find('guid').text] = c.find('nome').text

    tparams = {
        'cursos': info
    }
    return render(request, 'detalhes.html', tparams)
