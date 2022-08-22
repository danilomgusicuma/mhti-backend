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

  def isAgender(self, gender):
    if gender == 'Agender':
      return 1
    return 0

  def isCisFemale(self, gender):
    if gender == 'Cis Female':
      return 1
    return 0

  def isCisMale(self, gender):
    if gender == 'Cis Male':
      return 1
    return 0

  def isNonBinary(self, gender):
    if gender == 'Non Binary':
      return 1
    return 0

  def isTransFemale(self, gender):
    if gender == 'Trans Female':
      return 1
    return 0

  def isTransMale(self, gender):
    if gender == 'Trans Male':
      return 1
    return 0

  def otherGender(self, gender):
    if gender != 'Agender' and gender != 'Cis Female' and gender != 'Cis Male' and gender != 'Non Binary' and gender != 'Trans Female' and gender != 'Trans Male':
      return 1
    return 0

  def isIndianOrAlaska(self, race):
    if race == 'American Indian or Alaska Native':
      return 1
    return 0

  def isAsian(self, race):
    if race == 'Asian':
      return 1
    return 0

  def isBlack(self, race):
    if race == 'Black':
      return 1
    return 0

  def isCaucasian(self, race):
    if race == 'Caucasian':
      return 1
    return 0

  def isEuropeanAmerican(self, race):
    if race == 'European American':
      return 1
    return 0

  def isHispanic(self, race):
    if race == 'Hispanic':
      return 1
    return 0

  def isWhite(self, race):
    if race == 'White':
      return 1
    return 0

  def isWhiteHispanic(self, race):
    if race == 'White Hispanic':
      return 1
    return 0

  def isMoreThanOneRace(self, race):
    if race == 'More than one of the above':
      return 1
    return 0

  def dontWannaAnswerRace(self, race):
    if race == 'I prefer not to answer':
      return 1
    return 0

  def otherRace(self, race):
    if race != 'White' and race != 'White Hispanic' and race != 'More than one of the above' and race != 'I prefer not to answer' and race != 'American Indian or Alaska Native' and race != 'Asian' and race != 'Black' and race != 'Caucasian' and race != 'European American' and race != 'Hispanic':
      return 1
    return 0

  def hasReceivedTreatment(self, hasReceivedTreatment):
    if hasReceivedTreatment:
      return 1
    return 0

  def openToDiscussionWorkspace(self, openToDiscussionWorkspace):
    if openToDiscussionWorkspace:
      return 1
    return 0

  def difficultMedicalLeave(self, medicalLeave):
    if medicalLeave == 'Difficult to ask for a medical leav':
      return 1
    return 0

  def dontKnowMedicalLeave(self, medicalLeave):
    if medicalLeave == "Don't know how difficult to ask for a medical leave":
      return 1
    return 0

  def mediumMedicalLeave(self, medicalLeave):
    if medicalLeave == "Neither easy nor difficult to ask for a medical leave":
      return 1
    return 0

  def somewhatDifficultMedicalLeave(self, medicalLeave):
    if medicalLeave == "Somewhat difficult to ask for a medical leave":
      return 1
    return 0

  def somewhatEasyMedicalLeave(self, medicalLeave):
    if medicalLeave == "Somewhat easy to ask for a medical leave":
      return 1
    return 0

  def veryDifficultMedicalLeave(self, medicalLeave):
    if medicalLeave == "Very difficult to ask for a medical leave":
      return 1
    return 0

  def veryEasyMedicalLeave(self, medicalLeave):
    if medicalLeave == "Very easy to ask for a medical leave":
      return 1
    return 0

  def talkToSupervisor(self, talkToSupervisor):
    if talkToSupervisor == 'No':
      return 0
    elif talkToSupervisor == 'Maybe':
      return 1
    return 2

  def talkToCoworker(self, talkToCoworker):
    if talkToCoworker == 'No':
      return 0
    elif talkToCoworker == 'Maybe':
      return 1
    return 2

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
