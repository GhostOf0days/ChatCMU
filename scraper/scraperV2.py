import requests
from bs4 import BeautifulSoup

# Define a list of unwanted file extensions
unwanted_extensions = ['.doc', '.ppt', '.pdf', '.xls']

# Function to check if a URL has an unwanted file extension
def has_unwanted_extension(url):
    for extension in unwanted_extensions:
        if url.endswith(extension):
            return True
    return False
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Define a list of unwanted file extensions
unwanted_extensions = ['.doc', '.ppt', '.pdf', '.xls']

# Function to check if a URL has an unwanted file extension
def has_unwanted_extension(url):
    for extension in unwanted_extensions:
        if url.endswith(extension):
            return True
    return False

# Normalize a URL by stripping off fragments and query parameters
def normalize_url(url):
    parsed = urlparse(url)
    return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

# Get all text from a URL
def get_p_tags(url):
    try:
        r = requests.get(url)
    except:
        return []
    soup = BeautifulSoup(r.text, 'lxml')
    return soup.find_all(['p', 'li', 'hr', 'div'])

# Get all URLs from a URL, making sure they contain a key and not an exclude_key
def get_urls(url, key, exclude_key):
    try:
        r = requests.get(url)
    except:
        return []
    soup = BeautifulSoup(r.text, 'lxml')
    urls = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href is not None:
            full_url = urljoin(url, href)
            if key in full_url and not full_url.startswith(exclude_key) and not has_unwanted_extension(full_url):
                urls.append(normalize_url(full_url))
    return urls

# Write all p tags to a file
def write_to_file(p_tags, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for p in p_tags:
            f.write(p.text + '\n')

key = "cmu.edu"
exclude_key = "https://lists.andrew.cmu.edu/mailman/listinfo"
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
    "https://scottylabs.org/",
    "https://cmueats.com"
    
]
visited = set()
counter = 0

while len(urls) != 0:
    url = urls.pop()
    normalized_url = normalize_url(url)
    
    if normalized_url in visited:
        continue
    
    visited.add(normalized_url)
    p_tags = get_p_tags(url)
    print(f"Scraping: {url}")
    write_to_file(p_tags, f"{path}{counter}.txt")
    
    new_urls = get_urls(url, key, exclude_key)
    urls.extend([u for u in new_urls if normalize_url(u) not in visited])
    
    counter += 1