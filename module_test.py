from scraperoo import rooquest as rq


terms = rq.terms(1)
term = terms[0]

crns = rq.term_crns(term)
crn = crns[0]

print(f"{crn=},{term['code']=}")
course1 = rq.course_data(term['code'],crn)