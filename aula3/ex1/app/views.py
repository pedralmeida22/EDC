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
        'cursos': info,
        'frase': "Cursos da Universidade de Aveiro"
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


def by_grau(request):
    grau = request.GET.get("grau")
    cursos = xml.xpath("//curso[grau = '{}']".format(grau))

    info = dict()

    for c in cursos:
        info[c.find('guid').text] = c.find('nome').text

    tparams = {
        'cursos': info,
        'frase': 'Cursos do grau ' + grau + ':'
    }

    return render(request, 'cursos.html', tparams)


def by_depart(request):
    depart = request.GET.get("depart")
    info = dict()
    cursos = xml.xpath("//curso[departamentos//departamento = '{}']".format(depart))

    for c in cursos:
        info[c.find('guid').text] = c.find('nome').text

    tparams = {
        'cursos': info,
        'frase': 'Cursos do ' + depart + ':'
    }

    return render(request, 'cursos.html', tparams)


def by_area(request):
    area = request.GET.get("area")
    info = dict()
    cursos = xml.xpath("//curso[areascientificas//areacientifica = '{}']".format(area))

    for c in cursos:
        info[c.find('guid').text] = c.find('nome').text

    tparams = {
        'cursos': info,
        'frase': 'Cursos da área ' + area + ':'
    }

    return render(request, 'cursos.html', tparams)


def by_local(request):
    local = request.GET.get("local")
    cursos = xml.xpath("//curso[local = '{}']".format(local))

    info = dict()

    for c in cursos:
        info[c.find('guid').text] = c.find('nome').text

    print("cursos", cursos)

    tparams = {
        'cursos': info,
        'frase': 'Cursos de ' + local + ':'
    }

    return render(request, 'cursos.html', tparams)


def departamentos(request):
    departamentos = xml.xpath("//cursos//departamentos//departamento")

    info = [d.text for d in departamentos]

    tparams = {
        'departs': info
    }
    return render(request, 'departamentos.html', tparams)


def areas(request):
    return HttpResponse("areas")


def locais(request):
    return HttpResponse("locais")
