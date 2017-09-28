import gspread
from oauth2client.service_account import ServiceAccountCredentials


FILENAME = 'save games/mp_Shimazu1507_02_17.eu4'

regex = '''^(  |\t)(?P<country>[A-Z]{3})={(?!\n\t\t(has|gov))
.+?was_player=yes
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

###Connect to google sheets through API
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
gc = gspread.authorize(credentials)
sh = gc.open("[PunchClub] EU4 Multiplayer")
worksheet = sh.worksheet("Test")


#Paste data to google sheets

i=2
for match in result:
    worksheet.update_cell(i,1,("%(country)7s %(dev)7s %(eff_dev)7s %(land_morale)7s %(naval_morale)7s %(score)7s %(treasury)7s %(income)7s %(army_tradition)7s %(navy_tradition)7s %(manpower)7s" % match.groupdict()))
    i=i+1
    
