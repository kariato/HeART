__author__ = 'mdavey'
import  csv
from .models import DNAKitUpload,Family,ExampleModel,DNAKit


def readFile(kit,file):
    print(kit.family)
    dnakit = DNAKit.objects.get(pk=kit.id)
    print(dnakit.family)
    print(dnakit.family)
    file = file.replace("\\\\","\\")
    if file.find("Family_Finder_Matches") != -1:
        with open(file) as csvFF:
            ffreader = csv.DictReader(csvFF, dialect="excel")
            for arow in ffreader:
                print( arow['Full Name'],arow['Match Date'],arow['Relationship Range'],
                                arow['Suggested Relationship'],arow['Shared cM'],arow['Longest Block'],arow['Known Relationship'],
                                arow['E-mail'],arow['Ancestral'],arow['YDNA Haplogroup'],arow['mtDNA Haplogroup'],arow['ResultID2'],
                                arow['Notes'],arow['Name'])
    if file.find("_ICW") != -1:
        with open(file) as csvICW:
            ffICWreader = csv.DictReader(csvICW, dialect="excel")
            for arow in ffICWreader:
                print(arow['Profile Name'],
                               arow['Full Name'],arow['0'],arow['0'],arow['E-Mail'],arow['Profile KitID'],arow['Match KitID'])
    if file.find("_ChromosomeBrowser") != -1:
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile, dialect="excel")
            for arow in reader:
               print(arow['Profile Name'],arow['Full Name'],
                              arow['Chromosome'],arow['Start'],arow['End'],arow['cM'],arow['SNPS'],arow['KitID'])


