from bs4 import BeautifulSoup
import csv
import urllib.request

outfile = open('data_output.csv', 'w')
writer = csv.writer(outfile)

soup = BeautifulSoup(urllib.request.urlopen("http://nvbdcp.gov.in/malaria3.html").read(), 'lxml')
table = soup("table", {"width":"618"})[0].find_all('tr')
for row in table:
    cols = row.findChildren(recursive=False)
    cols = [ele.text.strip() for ele in cols]
    writer.writerow(cols)
    print(cols)

writer.writerow('\n')

soup = BeautifulSoup(urllib.request.urlopen("https://malariajournal.biomedcentral.com/articles/10.1186/1475-2875-13-126").read(), 'lxml')
table = soup("table", {"xmlns":"http://www.w3.org/1999/xhtml"})[0].find_all('tr')
for row in table:
    cols = row.findChildren(recursive=False)
    cols = [ele.text.strip() for ele in cols]
    writer.writerow(cols)
    print(cols)