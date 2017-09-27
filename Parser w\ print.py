import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials


FILENAME = 'save games/mp_Shimazu1507_02_17.eu4'

regex = '''^(  |\t)(?P<country>[A-Z]{3})={
.+?capped_development=(?P<dev>[0-9]+\.[0-9]{3})
.+?realm_development=(?P<eff_dev>[0-9]+\.[0-9]{3})
.+?max_land_morale=(?P<land_morale>[0-9]+\.[0-9]{3})
.+?max_naval_morale=(?P<naval_morale>[0-9]+\.[0-9]{3})
.+?(  |\t)score=(?P<score>[0-9]+\.[0-9]{3})
.+?treasury=(?P<treasury>[0-9]+\.[0-9]{3})
.+?estimated_monthly_income=(?P<income>[0-9]+\.[0-9]{3})
.+?army_tradition=(?P<army_tradition>[0-9]+\.[0-9]{3})
.+?navy_tradition=(?P<navy_tradition>[0-9]+\.[0-9]{3})
.+?max_manpower=(?P<manpower>[0-9]+\.[0-9]{3})'''
data = open(FILENAME, "r").read()
x = re.compile(regex, re.MULTILINE | re.DOTALL)

countries = data.split("\ncountries={")[1]
result = x.finditer(countries)

print ('{0:7s}  {1:7s} {2:7s} {3:7s} {4:7s} {5:7s} {6:7s} {7:7s} {8:7s} {9:7s} {10:7s}'.format('Country', 'Total_dev', 'Effective_dev', 'Land_morale', 'Naval_morale', 'Score', 'Treasury', 'Income', 'Army_tradition', 'Navy_tradition', 'Manpower'))

for match in result:
    print("%(country)7s %(dev)7s %(eff_dev)7s %(land_morale)7s %(naval_morale)7s %(score)7s %(treasury)7s %(income)7s %(army_tradition)7s %(navy_tradition)7s %(manpower)7s" % match.groupdict())

    






