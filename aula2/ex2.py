import pyinputplus as pyip
from lxml import etree


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
    while True:
        response = menu()

        if response == "Leitura Doc XML":
            tree = etree.parse('xml_files/miect.xml')
            root = tree.getroot()
            print_tree(root)

        elif response == "Validar Doc XML":
            # validate_file('xml_files/miect.xml')
            schema_root = etree.parse('xml_files/curso.xsd')
            schema = etree.XMLSchema(schema_root)

            print(schema.validate(tree))

        elif response == "Mostrar Info Curso":
            print('show')

        elif response == "Sair":
            break

    print("program ended")


if __name__ == '__main__':
    main()
