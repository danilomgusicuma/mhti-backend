from datetime import date

class Preprocessor():

  female_list = ["Female", "female", "I identify as female.", "I identify as female", "female ", "Female assigned at birth ",
            "Female assigned at birth", "F", "Woman", "fm", "f", "Cis female ", "Cis female", "Female ", "woman", "female/woman", 
            "Cisgender Female", "fem", "Female (props for making this a freeform field, though)", " Female", "Cis-woman", "femail",
            "AFAB"] 
  male_list = ["Male", "male", "Male ", "M", "m", "man", "Cis male", "Male.", "Male (cis)", "Man", "Sex is male", "cis male", 
             "Malr", "Dude",
             "I'm a man why didn't you make this a drop down question. You should of asked sex? And I would of answered yes please. Seriously how much text can this take? ", 
             "mail", "M|", "male ",  "Cis Male", "cisdude", "cis man", "AMAB", "MALE"] 
  
  def age(self, birthDate):
    return date.today().year - birthDate.year

  def familyHistory(self, familyHistory):
    if familyHistory:
      return 1
    return 0

  def employeeHistory(self, employeeHistory):
    if employeeHistory:
      return 1
    return 0
  
  def isTechCompany(self, isTechCompany):
    if isTechCompany:
      return 1
    return 0

  def hasBenefits(self, hasBenefits):
    if hasBenefits:
      return 1
    return 0

  def isFemale(self, gender):
    if gender in set(self.female_list):
      return 1
    return 0

  def isMale(self, gender):
    if gender in set(self.male_list):
      return 1
    return 0

  def otherGender(self, gender):
    if gender in set(self.female_list) or gender in set(self.male_list):
      return 0
    return 1

  def isMicroEnterprise(self, numberOfEmployees):
    if numberOfEmployees <= 5:
      return 1
    return 0
  
  def isSmallEnterprise(self, numberOfEmployees):
    if numberOfEmployees >= 6 and numberOfEmployees <= 100:
      return 1
    return 0

  def isMediumEnterprise(self, numberOfEmployees):
    if numberOfEmployees >= 101 and numberOfEmployees <= 500:
      return 1
    return 0

  def isLargeEnterprise(self, numberOfEmployees):
    if numberOfEmployees >= 501 and numberOfEmployees <= 1000:
      return 1
    return 0

  def isEnterprise(self, numberOfEmployees):
    if numberOfEmployees >= 1001:
      return 1
    return 0
