__author__ = 'mdavey'
import  csv
import re
from .models import DNAKitUpload,Family,ExampleModel,DNAKit,DNAMatch,DNASegment,DNAICW
import dateparser


def readCSV(filename,encodingType):
        with open(filename,'rU',encoding=encodingType) as csvFF:
            lineNum = 1
            _lines=[]
            for line1 in csvFF:
                for line in line1.split("\r\n"):
                    if lineNum==1:
                        gedItems= line.split(",")
                        _header=[]
                        for headers in gedItems:
                            _header.append(headers.rstrip('\n'))
                        lineNum=2

                    else:
                        gedItems = re.findall(r'".+?"|[^"]+?(?=,)|(?<=,)[^"]+', line)
                        item={}
                        if len(gedItems) == len(_header):
                            for i in range(0,len(gedItems)):
                                if (i < len(_header)):
                                    if gedItems[i][:1]==',':
                                        item[_header[i]]=gedItems[i][1:]
                                    else:
                                        item[_header[i]]=gedItems[i].rstrip('\n')
                                else:
                                    print("***"+gedItems[i])
                            _lines.append(item)
                        #print(item)
        return _lines


def readFile(kit,file):
    #sys.stdout = codecs.getwriter("iso-8859-1")(sys.stdout, 'xmlcharrefreplace')
    print(kit.family)
    dnakit = DNAKit.objects.get(pk=kit.id)
    #print(dnakit.family)
    #print(dnakit.family)
    file = file.replace("\\\\","\\")
    if file.find("Family_Finder_Matches") != -1:
            DNAMatch.objects.filter(resultSet=kit).delete()
            ffreader = readCSV(file,"ISO-8859-1")
            for arow in ffreader:
                aMatch = DNAMatch(resultSet=kit,fullName=arow['Full Name'],matchDate=dateparser.parse(arow['Match Date']),
                                  relationshipRange =arow['Relationship Range'],suggestedRelationship=arow['Suggested Relationship'],
                                  sharedCM = arow['Shared cM'],    longestBlock = arow['Longest Block'],    knownRelationship = arow['Known Relationship'],
                                  email = arow['E-mail'],    ancestralSurnames = arow['Ancestral'],
                                  YDNAHaplogroup=arow['YDNA Haplogroup'],mtDNAHaplogroup=arow['mtDNA Haplogroup'],resultID2=arow['ResultID2'],
                                  notes=arow['Notes'],name=arow['Name'])
                aMatch.save()

    if file.find("_ICW") != -1:
         ffICWreader = readCSV(file,"ISO-8859-1")
         for arow in ffICWreader:
            try:
                dnakit1 = DNAMatch.objects.get(resultSet=kit,resultID2=arow['Profile KitID'])
                dnakit2 = DNAMatch.objects.get(resultSet=kit,resultID2=arow['Match KitID'])
                aICW = DNAICW(kit=kit,first_match=dnakit1,second_match=dnakit2)
                aICW.save()
            except DNAMatch.DoesNotExist:
                # no kit found
                print(arow['Profile KitID'])
            except DNAMatch.MultipleObjectsReturned:
                # to many kits found
                print(arow['Profile KitID'])


    if file.find("_ChromosomeBrowser") != -1:
            reader = readCSV(file,"ISO-8859-1")
            for arow in reader:
                try:
                    dnakit = DNAMatch.objects.get(resultSet=kit,resultID2=arow['KitID'])
                    aDNAseg = DNASegment(matchname =dnakit,    chromosome = arow['Chromosome'], startLocation = arow['Start'],    endLocation = arow['End'],    centimorgans = arow['cM'],    matchingSnps = arow['SNPS'])
                    aDNAseg.save()
                except DNAMatch.DoesNotExist:
                    # no kit found
                    print(arow['KitID'])
                except DNAMatch.MultipleObjectsReturned:
                    # to many kits found
                    print(arow['KitID'])


