from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from lxml import etree

# Create your views here.
xml = etree.parse("app/xml_files/cursos.xml")


def cursos(request):
    info = dict()
    cursos = xml.xpath('//curso')
    for c in cursos:
        info[c.find('guid').text] = c.find('nome').text

    tparams = {
        'cursos': info
    }

    return render(request, 'cursos.html', tparams)


def curso_details(request, guid):
    info = dict()

    curso = xml.find("//curso[guid = '{}']".format(guid))

    info['nome'] = curso.find('nome').text
    info['codigo'] = curso.find('codigo').text
    info['grau'] = curso.find('grau').text

    info['departamentos'] = []
    for depart in curso.xpath(".//departamentos/departamento"):
        info['departamentos'].append(depart.text)

    info['areas'] = []
    for a in curso.xpath(".//areascientificas/areacientifica"):
        info['areas'].append(a.text)

    info['local'] = curso.find('local').text

    tparams = {
        'curso': info
    }
    return render(request, 'detalhes.html', tparams)
