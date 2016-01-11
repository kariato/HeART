__author__ = 'mdavey'
import  csv
import re
from .models import DNAKitUpload,Family,ExampleModel,DNAKit


def readCSV(filename):
        with open(filename, encoding="utf8") as csvFF:
            lineNum = 1
            _lines=[]
            for line in csvFF:
                if lineNum==1:
                    gedItems= line.split(",")
                    _header=gedItems
                    lineNum=2

                else:
                    gedItems = re.findall(r'".+?"|[^"]+?(?=,)|(?<=,)[^"]+', line)
                    item={}
                    for i in range(0,len(gedItems)):
                        if (i < len(_header)):
                            if gedItems[i][:1]==',':
                                item[_header[i]]=gedItems[i][1:]
                            else:
                                item[_header[i]]=gedItems[i]
                        else:
                            print("***"+gedItems[i])
                    _lines.append(item)
                    #print(item)
        return _lines


def readFile(kit,file):
    print(kit.family)
    dnakit = DNAKit.objects.get(pk=kit.id)
    print(dnakit.family)
    print(dnakit.family)
    file = file.replace("\\\\","\\")
    if file.find("Family_Finder_Matches") != -1:
            ffreader = readCSV(file)
            for arow in ffreader:
                print( arow['Full Name'],arow['Match Date'],arow['Relationship Range'],
                                arow['Suggested Relationship'],arow['Shared cM'],arow['Longest Block'],arow['Known Relationship'],
                                arow['E-mail'],arow['Ancestral'],arow['YDNA Haplogroup'],arow['mtDNA Haplogroup'],arow['ResultID2'],
                                arow['Notes'],arow['Name'])
    if file.find("_ICW") != -1:
         ffICWreader = readCSV(file)
         for arow in ffICWreader:
            print(arow['Profile Name'],arow['Full Name'],arow['0'],arow['0'],arow['E-Mail'],arow['Profile KitID'],arow['Match KitID'])

    if file.find("_ChromosomeBrowser") != -1:
            reader = readCSV(file)
            for arow in reader:
               print(arow['Profile Name'],arow['Full Name'],
                              arow['Chromosome'],arow['Start'],arow['End'],arow['cM'],arow['SNPS'],arow['KitID'])


