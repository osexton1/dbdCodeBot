from InstaBot import InstaBot
from CodeScraper import CodeScraper

dbdCodes = {}

dbdCodeScraper = CodeScraper()

dbdCodeScraper.getWorkingCodes()
dbdCodeScraper.formatCodes()

dbdCodes = dbdCodeScraper.getCodes()

dbdCodeBot = InstaBot()

dbdCodeBot.login()
dbdCodeBot.open_messages()

for code in dbdCodes.keys():
    dbdCodeBot.send_message(code + " => " + dbdCodes[code])

dbdCodeBot.close_browser()