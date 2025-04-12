from pprint import pprint

class Course(object):
    """
    Custom class that can parse the custom xml schemea
    """
    def __init__(self, data:str):
        self.SubjectAbbreviation = data.split('</')[0]
        
        data = data.split('<CourseNumber>')[1]
        self.Number = data.split('</CourseNumber>')[0]
        
        data = data.split('<CourseShortTitle>')[1]
        self.ShortTitle = data.split('</CourseShortTitle>')[0].title()

        data = data.split('<CourseLongTitle>')[1]
        self.LongTitle = data.split('</CourseLongTitle')[0].title()
        try:
            data = data.split('<CourseDescription>')[1]
            self.Description = data.split('</CourseDescription>')[0]
        except IndexError:
            self.Description = 'NO DESCRIPTION AVAILABLE'
        data = data.split('<CourseEffectiveDate>')[1]
        self.EffectiveDate = data.split('</CourseEffectiveDate>')[0]
        
        data = data.split('<CourseCreditBasis>')[1]
        self.CreditBasis = data.split('</CourseCreditBasis')[0]

        data = data.split('<CourseCreditUnits>')[1]
        self.CreditUnits = data.split('</CourseCreditUnits')[0]

        data = data.split('<CourseCreditMinimumValue>')[1]
        self.CreditBasis = data.split('</CourseCreditMinimumValue')[0]

        data = data.split('<CourseLevelCode>')[1]
        self.LevelCode = data.split('</CourseLevelCode')[0]

        data = data.split('<CourseLevelDescription>')[1]
        self.LevelDescription = data.split('</CourseLevelDescription')[0]

        data = data.split()
    def __repr__(self):
        return f"{self.SubjectAbbreviation} {self.Number} {self.ShortTitle}"
        

# Load the XML file
xml_file_location = 'file.xml'

# read the file
with open(xml_file_location, 'r') as xml_file:
    xml_text = xml_file.read()

courses = xml_text.split('<CourseSubjectAbbreviation>')
courses = courses[1:]

courses_obj = []
for i in courses:
    print(f'\n{i}')
    new_course = Course(i)
    courses_obj.append(new_course)
    

print(courses_obj)
for i in courses_obj:
    print(i)
    print(i.Description)
    print()

