import xml.etree.ElementTree as ET

'''
    Function that reads a XML file, finds an specific element in the XML tree and 
    returns the CDATA contained in the "tail" of the element 
'''
def get_xml_CDATA_from_element_tail(xml_file_directory: str, element_name: str):
    tree = ET.parse(xml_file_directory)
    element_tail = tree.find(element_name).tail
    return element_tail

