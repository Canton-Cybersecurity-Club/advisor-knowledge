import requests
import pprint

URLHEADER = "https://banweb.canton.edu/StudentRegistrationSsb/ssb/searchResults/"


class Course(object):
    """
    docstring
    """
    def __init__(self):
        pass


def terms(last_n_terms):
    """
    docstring
    """
    url = f"https://banweb.canton.edu/StudentRegistrationSsb/ssb/classSearch/getTerms?searchTerm=&offset=1&max={last_n_terms}"
    response = requests.get(url)
    return response.json()


def term_crns(term):
    """
    docstring
    """
    print(f"Getting CRN numbers for {term}")
    url = f"https://banweb.canton.edu/pls/prod/canton_rtn.P_SelectCourses?term={term['code']}"
    response = requests.get(url).content.decode()
    crn_list = []
    for line in response.split("\n"):
        if "crn_arr" in line:
            crn = line.split('value="')[1].strip('" />')
            crn_list.append(crn)
    return crn_list


def course_data(term, crn):
    """
    docstring
    """
    request_identifiers = [
    "getClassDetails", #html text
    "getSectionBookstoreDetails", #html text
    "getCourseDescription", #html text
    "getSyllabus", #html text
    "getSectionAttributes", #html text
    "getRestrictions", #html text
    "getFacultyMeetingTimes", #JSON
    "getEnrollmentInfo",#html text
    "getCorequisites", #html text
    "getSectionPrerequisites", #html text
    "getCourseMutuallyExclusions", #html text
    "getXlstSections",#html text
    "getLinkedSections", #html text
    "getFees", #html text
    "getSectionCatalogDetails", #html text
    ]
    
    for req in request_identifiers:
        url = f"{URLHEADER}{req}?term={term}&courseReferenceNumber={crn}"
        print(url)
        response = requests.get(url)
        print(response.text,'\n')


