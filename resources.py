import xlsxwriter

class Resource:
  #a Resource should have a name, role, position, region, and a list of hours for each week
  def __init__(self,details):
    self.name = details['name']
    self.position = details['position']
    self.role = details['role']
    self.region = details['region']
    self.hours = details['hours']
  def describe(self):
    description = self.name + " is our " + self.position + " " + self.role + " in " + self.region + ". Gonna work " + self.totalHours() + " hours in total."
    return description
  def totalHours(self):
    totalHours = 0
    if hasattr(self,'hours'):
      totalHours = sum(self.hours)
    return str(totalHours)

class Project:
    #a Project should have a code, start date, end date, and a list of resources
    def __init__(self,details):
        self.code = details['code']
        self.start = details['start']
        self.end = details['end']
        self.resources = details['resources']
    def describe(self):
        description = "The " + self.code + " project starts on " + self.start + ", ends on " + self.end + ", and has " + str(len(self.resources)) + " resources"
        return description
    def writeXLSX(self):
        print("I really want to create an Excel file with A1 set to " + self.code)
        workbook = xlsxwriter.Workbook(self.code + ".xlsx")
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', self.code)
        workbook.close()


#Convenience function to get Project details from the command line
def getProjectCL():
    code = input('Project Code: ')
    start = input('Start Date: ')
    end = input('End Date: ')
    print("Project " + code + " will start on " + start + " and end on " + end + ".")
    resources = []
    resYN = input('Do you want to add some resources (Y/N)? ')
    while resYN == 'Y':
        resName = input('  Resource Name: ')
        resPos = input('  Resource Position: ')
        resRole = input(' Resource Role: ')
        resRegion = input('  Resource Region: ')
        res_details = {'name':resName,
                'position':resPos,
                'role':resRole,
                'region':resRegion,
                'hours':[40,40,40]
        }
        res = Resource(res_details)
        resources.append(res)
        resYN = input(' Cool. Adding ' + res.name + ' to the RP. Add another (Y/N)? ')
    print('AdddCreated ' + str(len(resources)) + " resources.")

    prj_details = {'code': code,
                'start': start,
                'end': end,
                'resources': resources}
    
    prj = Project(prj_details)
    print("OK, I created " + prj.code + " with " + str(len(prj.resources)) + " resources. Bye!")
    return prj