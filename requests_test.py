import requests

s = requests.Session()
s.get("https://banweb.canton.edu/StudentRegistrationSsb/ssb/classSearch/classSearch")
print(s.cookies)

cookies_string = ";".join([f"{name}={value}" for name, value in s.cookies.items()])
print(cookies_string)
headers = {
    "Host": "banweb.canton.edu",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://banweb.canton.edu/StudentRegistrationSsb/ssb/classSearch/classSearch",
    "Connection": "keep-alive",
    "Cookie": cookies_string,
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-origin",
    "DNT": "1",
    "Sec-GPC": "1",
    "Priority": "u=4",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}

response = requests.get("https://banweb.canton.edu/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_term=202509&startDatepicker=&endDatepicker=&uniqueSessionId=vpxxf1744505342624&pageOffset=0&pageMaxSize=10&sortColumn=subjectDescription&sortDirection=asc", headers=headers)

print(response.status_code)
print(response.text)
