import json
from scraperoo import rooquest as rq
from pprint import pp as pp
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

terms = rq.terms(3)
term = terms[1]

crns = rq.term_crns(term)
print(f"{len(crns)} CRNs found for term {term['code']}")
input('Press any button to continue...')

filename = f"courses_{term['code']}.jsonl"
error_log = "errors.log"

# Function to process a single CRN
def process_crn(crn):
    try:
        course_data = rq.course_data(term['code'], crn)
        return {'crn': crn, 'data': vars(course_data), 'error': None}
    except Exception as e:
        return {'crn': crn, 'data': None, 'error': str(e)}

max_threads = 10  # You can increase or decrease this depending on your system / API rate limits

with open(filename, 'a') as outfile, open(error_log, 'a') as errfile:
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {executor.submit(process_crn, crn): crn for crn in crns}
        for future in tqdm(as_completed(futures), total=len(futures), desc="Scraping courses"):
            result = future.result()
            if result['error']:
                err_msg = f"Error with CRN {result['crn']} for term {term['code']}: {result['error']}\n"
                print(f"⚠️ {err_msg.strip()}")
                errfile.write(err_msg)
            else:
                pp(result['data'])
                json.dump(result['data'], outfile)
                outfile.write('\n')

print(f"\n✅ Done. Courses saved to '{filename}'. Errors (if any) logged to '{error_log}'.")
