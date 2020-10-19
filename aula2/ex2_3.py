import pyinputplus as pyip
from lxml import etree
import urllib.request


def menu():
    return pyip.inputMenu(["Leitura Doc XML", "Validar Doc XML", "Mostrar Info Curso", "Sair"],
                          "Selecione uma opção:\n", numbered=True)


def print_tree(root, t=""):
    if root.attrib != "":
        info = str(root.attrib)
    else:
        info = t + str(root.tag) + " -> " + str(root.text) + "\n"

    info = info.replace("{}", "").replace("\n", "")
    print(info)
    if len(root.getchildren()):
        for child in root:
            print_tree(child, t + "\t")


def main():
    url = "http://acesso.ua.pt/xml/curso.v5.asp?i=23"
    document = urllib.request.urlopen(url).read()
    tree = etree.fromstring(document)

    while True:
        response = menu()

        if response == "Leitura Doc XML":
            print("Source: ", url)
            print("Ler: " + tree.find("nome").text)

        elif response == "Validar Doc XML":
            schema_root = etree.parse('xml_files/curso.xsd')
            schema = etree.XMLSchema(schema_root)

            print("Validação: " + str(schema.validate(tree)))

        elif response == "Mostrar Info Curso":
            print_tree(tree)

        elif response == "Sair":
            break

    print("program ended")


if __name__ == '__main__':
    main()
