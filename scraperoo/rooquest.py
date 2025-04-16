from urllib import request
import requests
from pprint import pp as pp
from bs4 import BeautifulSoup

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
        "getClassDetails",  # html text
        # "getSectionBookstoreDetails",  # html text
        "getCourseDescription",  # html text
        # "getSyllabus",  # html text
        "getSectionAttributes",  # html text
        # "getRestrictions",  # html text
        "getFacultyMeetingTimes",  # JSON
        "getEnrollmentInfo",  # html text
        "getCorequisites",  # html text
        "getSectionPrerequisites",  # html text
        "getCourseMutuallyExclusions",  # html text
        "getXlstSections",  # html text
        # "getLinkedSections",  # html text
        # "getFees",  # html text
        "getSectionCatalogDetails",  # html text
    ]

    response_data = {}
    for req in request_identifiers:
        url = f"{URLHEADER}{req}?term={term}&courseReferenceNumber={crn}"
        # print(url)

        if req == "getClassDetails":
            data = {}
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            status_labels = soup.select("span.status-bold")

            for label in status_labels:
                key = label.get_text(strip=True).rstrip(":")
                value_node = label.next_sibling

                # Skip empty text nodes (whitespace, \n, etc.)
                while value_node and (
                    value_node.name is None and not value_node.strip()
                ):
                    value_node = value_node.next_sibling

                if value_node:
                    if value_node.name:  # If it's a tag like <span id=...>
                        value = value_node.get_text(strip=True)
                    else:  # If it's plain text
                        value = value_node.strip()
                    data[key] = value
            response_data["details"] = data

        elif req == "getCourseDescription":
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            text = soup.get_text()
            response_data["description"] = text.strip()

        elif req == "getSectionAttributes":
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            text = soup.get_text()
            response_data["section_attributes"] = text.strip()

        elif req == "getFacultyMeetingTimes":
            response = requests.get(url).json()
            response_data["meeting_times"] = response["fmt"][0]

        elif req == "getEnrollmentInfo":
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            text = soup.get_text()
            text = text.strip().split("\n")
            result = {}
            for item in text:
                if item:
                    item = item.split(":")
                    result[item[0].strip()] = item[1].strip()
            response_data["enrollment_info"] = result

        elif req == "getCorequisites":
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            text = soup.get_text(separator=' ', strip=True)
            response_data['corequisites'] = text[13:]

        elif req == "getSectionPrerequisites":
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            text = soup.get_text(separator=' ', strip=True)
            response_data['catalog_prerequisites'] = text[22:]

        elif req == "getCourseMutuallyExclusions":
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            text = soup.get_text(separator=' ', strip=True)
            response_data['mutually_exclusions'] = text
        elif req == "getXlstSections":
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            text = soup.get_text(separator=' ', strip=True)
            response_data['xlist_sections'] = text
        elif req == "getSectionCatalogDetails":
            data = {}
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            status_labels = soup.select("span.status-bold")

            for label in status_labels:
                key = label.get_text(strip=True).rstrip(":")
                value_node = label.next_sibling

                # Skip empty text nodes (whitespace, \n, etc.)
                while value_node and (
                    value_node.name is None and not value_node.strip()
                ):
                    value_node = value_node.next_sibling

                if value_node:
                    if value_node.name:  # If it's a tag like <span id=...>
                        value = value_node.get_text(strip=True)
                    else:  # If it's plain text
                        value = value_node.strip()
                    data[key] = value

            response_data['catalog_details'] = data
    return response_data
