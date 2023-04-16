"""
If it doesn't work, uncomment lines  42 48 49 and 71
Remove lines 45 46 47 48
"""

import requests, wget, os
import re #, fitz, io, wget
from urllib.error import HTTPError


listPages=["https://www.ftc.gov/legal-library/browse/cases-proceedings"]
#Add all the other pages with filters etc. 
allLinks = {'Accounting': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1379', 'Alcohol': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1381', 'Appliances': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1380','Automobiles': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1382', 'Clothing & Textiles': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1383', 'Construction': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1384', 'Defense': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1385', 'Finance': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1386', 'Food & Beverages': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1387', 'Franchises, Business Opportunities, & Investments': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1388', 'Funerals': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1389', 'Human Resources': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1390', 'Jewelry': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1391', 'Non-Profits': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1392', 'Professional Services': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1393', 'Real Estate & Mortgages': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1394', 'Telecommunications': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1395', 'Tobacco': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1396', 'Transportation': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1397', 'Veterinarians': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1398', 'Government': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1399', 'Entertainment': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1400', 'Technology: Mobile': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1401', 'Government: Policy': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1402', 'Environment': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1404', 'Energy': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1352', 'Healthcare': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1357', 'Manufacturing': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1366', 'Retail': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1370', 'Technology': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1374', 'Technology: Cable TV': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1376', 'Technology: Patents & IP': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1375', 'Technology: Hardware': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1377', 'Technology: Software & Databases': 'https://www.ftc.gov/legal-library/browse/cases-proceedings?sort_by=field_date&search=&field_competition_topics=All&field_federal_court=All&field_case_status=All&search_matter_number=&search_civil_action_number=&start_date=&end_date=&items_per_page=100&field_consumer_protection_topics=All&field_enforcement_type=All&field_mission%5B29%5D=29&field_industry=1378'}

regCaseH3 = '<h3 class="node-title"><a href=.*?</h3>'
regPDFs = '<a href=\".*?\.pdf\"'
regTitle = '<h1 class="margin-0"><span>.*?</span></h1>'

def getCaselinks(k,v):
    caseLinks=[]
    r = requests.get(v)
    #Find the h3 elements, meaning each case
    AllCaseList = re.findall(regCaseH3, r.text)

    for case in AllCaseList:
        a = str(case)
        b = a.strip('<h3 class="node-title"><a href="')
        c = b.split('" hreflang="en">')
        d = "https://www.ftc.gov"+c[0]
        e = [d,k] #url, industry
        caseLinks.append(e)

    return caseLinks

def getPDFlinks(caseLinks):
    pdfs = []
    thisdir = os.path.dirname(__file__)
    dirnum = 0
    for i in caseLinks:
        casenum = "/case"+str(dirnum)
        relativefolder ='/downloads/'+i[1]+casenum
        outFolder = thisdir + relativefolder
        print(outFolder)
        try: 
            os.makedirs(outFolder)
            urlname = outFolder+'/urlname.txt'
            with open(urlname,'w') as f:
                f.write(i[0])
        except:
            pass
        dirnum+=1

        r = requests.get(i[0])
        #Get all PDFs
        x = re.findall(regPDFs,r.text) #x = all instances of PDF links on the case page
        print(x)
        for j in x:
            
            a = j.strip('<a href="')
            if 'a href' in a:
                c = a.split('<a href="')
                a = c[len(c)-1]
                a = a.strip("")
#            industry = i[1]
            #I know these nested ifs are awful but I kept finding different weird variations of url and it just exploded
            if a[0:4] == "http" and a[len(a)-1]=="f":
                print(1)
                try:
                    wget.download(j,out=outFolder)
                except HTTPError:
                    print(j)
                    a = j.split('<a href="')
                    b = a[len(a)-1]
            elif a[0:4] == "http" and a[len(a)-1]=="d":
                print(2)
                b = a+"f"
                wget.download(b,out=outFolder)
            elif a[0:3] == "ttp" and a[len(a)-1]=="d":
                print(3)
                print(a)
                b = "h"+a+"f"
                print(b)
                wget.download(b,out=outFolder)
            elif a[0:3] == "ttp" and a[len(a)-1]=="f":
                print(4)
                b = "h"+a
                wget.download(b,out=outFolder)
            else:
                print(5)
                b = "https://www.ftc.gov"+a+'f'
                print(a[0:3])
                print(b)
                wget.download(b,out=outFolder)
                print('\n\n')
            #c = [b,industry]
            #pdfs.append(c)
       
    return pdfs

def downloadPDFs(pdflinks):
    for i in pdflinks:

        outFolder = './downloads/'+i[1]
        try:
            print(i)
            wget.download(i[0],out=outFolder)
        except:
            print("passing"+i[0])


for k,v in allLinks.items():
    print(k)
    caselinks = getCaselinks(k,v)
    print("Found case links")
    pdflinks = getPDFlinks(caselinks)
    print("Found PDF links")
    #downloadPDFs(pdflinks)