
import xml.etree.ElementTree as ET

'''
    Convert xml to dictionary
'''
def xml_to_dict(uploaded_file):
    tree = ET.parse(uploaded_file)
    root = tree.getroot()
    if not len(root):
        return {root.tag: ""}

    elem_arr = []
    for elem in root:
        sub_elem_arr = []

        if len(elem):
            for subelem in elem:
                sub_elem_dict = {subelem.tag: subelem.text}
                sub_elem_arr.append(sub_elem_dict)

        elem_dict = {elem.tag: sub_elem_arr}
        elem_arr.append(elem_dict)

    return {root.tag: elem_arr}
