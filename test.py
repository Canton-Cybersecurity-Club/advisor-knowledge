import requests

class Course(object):
    """
    Custom class that can parse the banweb custom xml schemea
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
# SUMMER 2025:202505
# FALL 2025: 202509
# WINTER 2025-26: 202512
# SPRING 2026: 202602
term_year = "2025" 
term_month = {'spring':'02', 'summer':'05','fall':'09','winter':'12'}
term = f'{term_year}{term_month["summer"]}'
# subject= "%25"
subject= "%09CYBR%09" #CYBR Subject
url = f"https://banweb.canton.edu/pls/prod/bwckctlg.xml?term_in={term}&subj_in={subject}&title_in=%25%25&divs_in=%25&dept_in=%25&coll_in=%25&schd_in=%25&levl_in=%25&attr_in=%25&crse_strt_in=&crse_end_in=&cred_from_in=&cred_to_in=&last_updated="
response = requests.get(url).content.decode('UTF-8')
print(url)
# xml_file_location = 'file.xml'

# with open(xml_file_location, 'r') as xml_file:
#     xml_text = xml_file.read()

course_list = response.split('<CourseSubjectAbbreviation>')
course_list = course_list[1:]


courses_obj = []
for course in course_list:
    new_course = Course(course)
    courses_obj.append(new_course)
    

print(courses_obj)


