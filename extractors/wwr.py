from bs4 import BeautifulSoup
import requests


def extract_wwr_jobs(keyword):
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})
    if request.status_code == 200:
        results = []
        soup = BeautifulSoup(request.text, "html.parser")
        # write your ✨magical✨ code here
        pages = soup.find_all('tr')
        for page in pages:
            company_and_positions = page.find_all(
                'td', class_="company_and_position")
            for company_and_position in company_and_positions:

                companys = company_and_position.find_all('h3')
                for company in companys:
                    company = company.string

                jobs = company_and_position.find_all('h2')
                for job in jobs:
                    job = job.string

                anchors = company_and_position.find_all('a')
                for anchor in anchors:
                    link = anchor['href']
                    if not link.startswith("https://"):
                        link = f"https://remoteok.com{link}"
                job_data = {
                    'company': company,
                    'job': job,
                    'link': link
                }
                results.append(job_data)
        results.pop(0)
        return results


