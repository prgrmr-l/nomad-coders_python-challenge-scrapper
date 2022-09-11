from bs4 import BeautifulSoup
import requests


def extract_wwr2_jobs(keyword):
    url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={keyword}"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        results = []
        soup = BeautifulSoup(request.text, "html.parser")
        # write your ✨magical✨ code here
        pages = soup.find_all('section', class_="jobs")
        for page in pages:
            features = page.find_all('li', class_="feature")

            for feature in features:
                anchors = feature.find_all('a', recursive=False)
                for anchor in anchors:
                    link = anchor['href']
                    if not link.startswith("https://"):
                        link = f"https://weworkremotely.com{link}"

                    companys = anchor.find('span', class_="company")
                    for company in companys:
                        company = company.string

                    jobs = anchor.find_all('span', class_="title")
                    for job in jobs:
                        job = job.string

                    job_data = {
                        'company':
                        company,
                        'job':
                        job,
                        'link':link
                    }
                    results.append(job_data)
        return results
