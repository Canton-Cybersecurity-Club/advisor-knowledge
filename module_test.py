from scraperoo import rooquest as rq
from pprint import pp as pp

terms = rq.terms(1)
term = terms[0]

crns = rq.term_crns(term)
print(len(crns))
input('Press any button to continue...')
# crn = crns[0]

# print(f"{crn=},{term['code']=}")
# course1 = rq.course_data(term['code'],crn)
# pp(course1)

for crn in crns:
    print(f"{crn=},{term['code']=}")
    course_data = rq.course_data(term['code'],crn)
    pp(course_data)