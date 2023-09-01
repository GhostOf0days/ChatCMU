import requests
from bs4 import BeautifulSoup


# get all text from a url
def get_p_tags(url):
    try:
        r = requests.get(url)
    except:
        return []
    soup = BeautifulSoup(r.text, 'html.parser')
    text = (soup.find_all('p') + 
            soup.find_all('li') + 
            soup.find_all('hr') +
            soup.find_all('div'))
    return text

# get all urls from a url. make sure they contain cmu.edu
def get_urls(url, key):
    try:
        r = requests.get(url)
    except:
        return []
    soup = BeautifulSoup(r.text, 'html.parser')
    urls = [] 
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is not None:
            if key in href:
                urls.append(href)
    return urls

# write all p tags to a file
def write_to_file(p_tags, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for p in p_tags:
            f.write(p.text)

key = "cmu.edu"
path = "../text/"
urls = [
    "https://www.cmu.edu/",
    "https://cmucourses.com/",
    "https://cmu.edu/academics/",
    "https://en.wikipedia.org/wiki/Carnegie_Mellon_University",
    "https://www.cmu.edu/admission/majors-programs",
    "https://www.cmu.edu/admission/majors-programs/school-of-computer-science",
    "https://www.cmu.edu/admission/majors-programs/information-systems",
    "https://tartanconnect.cmu.edu/club_signup",
    "https://scottylabs.org/"
    "https://cmueats.com"
    
    ]
visited = []
url = "cmu.edu"
counter = 0
while (len(urls) != 0):
    #remove http or https from url
    url = url.replace("https://", "").replace("http://", "")
    if url in visited:
        url = urls.pop()
        continue
    visited.append(url)
    url = urls.pop()
    p_tags = get_p_tags(url)
    print(url)
    write_to_file(p_tags, path + str(counter) + ".txt")
    urls += get_urls(url, key)
    counter += 1
