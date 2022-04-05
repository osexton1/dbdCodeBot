import requests as rq

class CodeScraper():
    def __init__(self):
        self.codes = []
        self.codesToSend = {}

        self.permanentCodes = ["PRIDE"]
        # usedCodesBSA = usedCodesButStillAvailable
        self.usedCodesBSA = ["NICE"]

        self.page = rq.get("https://progameguides.com/dead-by-daylight/dead-by-daylight-codes/")

    def getWorkingCodes(self):
        workingCodes = str(self.page.content).split("<ul>")[1:3]
        for code in workingCodes:
            for cohd in code.split("<li><strong>"):
                for code in cohd.split("</strong>&mdash;"):
                    self.codes.append(code)

    def formatCodes(self):
        self.codes.pop(0)
        self.codes.pop(0)
        self.codes.pop(0)

        while len(self.codes) > 0:
            code = self.codes.pop(0)
            codeReward = self.codes.pop(0).strip("</li>").split("<")[0].split("Redeem for ")
            if code.upper() not in (self.permanentCodes + self.usedCodesBSA):
                self.codesToSend[code] = codeReward[1].strip()

    def getCodes(self):
        return self.codesToSend

# This was for testing purposes to check the functions work properly
if __name__ == "__main__":
    testScraper = CodeScraper()
    testScraper.getWorkingCodes()
    testScraper.formatCodes()
    print(testScraper.getCodes())