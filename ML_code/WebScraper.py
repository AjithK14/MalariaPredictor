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