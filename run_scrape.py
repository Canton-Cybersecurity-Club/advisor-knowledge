import json
from scraperoo import rooquest as rq
from pprint import pp as pp
from tqdm import tqdm

terms = rq.terms(3)
term = terms[1]

crns = rq.term_crns(term)
print(f"{len(crns)} CRNs found for term {term['code']}")
input('Press any button to continue...')

filename = f"2courses_{term['code']}.jsonl"
error_log = "errors.log"

# Open the output and error log files outside the loop
with open(filename, 'a') as outfile, open(error_log, 'a') as errfile:
    for crn in tqdm(crns, desc="Scraping courses"):
        try:
            print(f"\nFetching: {crn=}, {term['code']=}")
            course_data = rq.course_data(term['code'], crn)
            pp(course_data)

            # Save course data
            json.dump(vars(course_data), outfile)
            outfile.write('\n')

        except Exception as e:
            # Log any errors
            err_msg = f"Error with CRN {crn} for term {term['code']}: {str(e)}\n"
            print(f"⚠️ {err_msg.strip()}")
            errfile.write(err_msg)

print(f"\n✅ Done. Courses saved to '{filename}'. Errors (if any) logged to '{error_log}'.")
