import sys
import re
from pprint import pprint

sample = { 'awesome-cancer-variant-databases':
            { 'Cancer':
                {
                    'Clinically-focused':
                    [{'CanDL': 'https://candl.osu.edu' }],
                    'Catalogs':
                    [{ 'COSMIC':
                    'http://cancer.sanger.ac.uk/cancergenome/projects/cosmic'}]
                }
            ,
             'Germline':
                [
                    { 'dnSNP': 'http://www.ncbi.nlm.nih.gov/SNP' },
                    { 'Exome Aggregation Consortium':
                    'http://exac.broadinstitute.org'}
                ]
            }
        }
sample_meta = { 'awesome-cancer-variant-databases': 'A community-maintained repository of cancer clinical knowledge bases and databases focused on cancer and normal variants. [Contributions welcome](https://github.com/seandavi/awesome-cancer-variant-databases/blob/master/CONTRIBUTE.md]).',
                'CanDL': 'an expert-curated database of potentially actionable driver mutations for molecular pathologists and laboratory directors to facilitate literature-based annotation of genomic testing of tumors. [web app, Download]'
                }

sample_info = { 'author': 'Sean Davis',
                'gituser': 'seandavi',
                'date': '10-16-2016',
                'total': 16
              }

# Ugly parsing code

def txt2dict(text):
    cnt = 0
    doc = {}
    depth = 0
    depth_pointer = {}
    pointer = doc
    istitle = False
    for line in text.split("\n"):
        if not len(line):
            continue
        line_type = find_type(line)
        text = line.split(" ")[1:]
        text = " ".join(text)
        if line_type[0] == "H":
            if not pointer: # is empty
                if depth <= int(line_type[1:]):
                    pointer[text] = {}
                    if not istitle:
                        istitle = True
                        depth_pointer[0] = pointer[text]
                    pointer = pointer[text]
            else:
                pointer = depth_pointer[int(line_type[1:]) - 1]
                pointer[text] = {}
                pointer = pointer[text]
            depth = int(line_type[1:])
            depth_pointer[depth] = pointer
        if line_type == "L":
            ldict = parsing(text)
            if not pointer:
                pointer['LIST'] = [{ldict['name']:ldict['url']}]
            else:
                pointer['LIST'].append({ldict['name']:ldict['url']})

        cnt += 1
    return doc

def find_type(text):
    if text[0] == "#":
        header = text.split(" ")[0]
        return "H" + str(len(header))
    if text[0] == ("-" or "*"):
        return "L"
    if text[0] == " ":
        islist = text.find('-')
        if islist:
            return "SubL" + str(islist)
    return "Else"

def main():

    with open(sys.argv[1], "r") as f:
        lines = f.read()
        new = txt2dict(lines)
        pprint (new)

def parsing(inputtext):

    # [name](url) description
    line = re.compile(r'\[([^\]]*)\]\s*\(([^\)]*)\)([^$]*)')
    depth = 0
    result = line.match(inputtext)
    return { "name": result.group(1),  "url": result.group(2), "description":
            result.group(3)}

main()
