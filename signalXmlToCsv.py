import csv
from lxml import etree
import sys
import csv

reload(sys)
sys.setdefaultencoding('utf-8')

# use recover=True to ignore errors in the XML
# examples of errors in XML:
#   missing "<" in opening tag:
#   fax></fax>
# missing "</" in closing tag:
#   <uid>1429860810uid>
#
# also ignore blank text

parser = etree.XMLParser(recover=True, remove_blank_text=True)

# xml on disk...could also pass etree.parse a URL
file_name = "SignalPlaintextBackup.xml"

# use lxml to read and parse xml
root = etree.parse(file_name, parser)

# element names with data to keep
attrb_list = ["address", "date", "body", "type"]
with open('signalMessages.csv', 'wb') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # add field names by copying tag_list
    # csv_writer.writerow(attrb_list[:])
    header =["number", "date", "text", "type", "chars"]
    csv_writer.writerow(header)

    # pull info out of each poi node
    def get_sms_attrb(sms):
        global attrb_list
        sms_data = []
        for attrb in attrb_list:
            # if tag == "name":
            # print "%s" % p.find(tag).text
            data = sms.attrib[attrb]
            print data
            if data is not None:
                sms_data.append(data)
                # info.append(node.text.encode("ascii", "ignore"))
        # add character count for text (message body)
        sms_data.append(len(sms.attrib["body"]))

        return sms_data

    # get all <sms> elements
    messages = root.findall("sms")
    for sms in messages:
        # print sms.attrib
        sms_data = get_sms_attrb(sms)
        # print sms_data
        if sms_data:
            csv_writer.writerow(sms_data)
