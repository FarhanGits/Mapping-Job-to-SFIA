import time, random, json, pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import linkedin_params

# Cek lama waktu scraping
print(
    f"Scraping dimulai pada jam {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"
)
start = time.perf_counter()

# Import data berisi kumpulan job_id yang didapat, Run menggunakan venv di directory "Code - Mapping to SFIA", ganti path sesuai kebutuhan!
with open(
    f"./Scraping/{linkedin_params.job_portal}/id/7 days v5/jobID-{linkedin_params.ISorCS_Jobs}-{linkedin_params.keyword_name}-7_days_v5.json", "r", encoding='utf-8'
) as data:
    job_list = json.load(data)

# Load Cookies
with open(f"./Scraping/LinkedIn/dump/cookies.json", "r", encoding="utf-8") as f:
    cookies = json.load(f)

job_data = []
scraped = 0
for i, job in enumerate(job_list):
    job_title = job["job_title"]
    job_url = f"https://www.linkedin.com/jobs/view/{job['job_id']}/"

    driver = webdriver.Chrome()
    driver.get(job_url)

    # Add cookies
    for cookie in cookies:
        if "sameSite" in cookie:
            if cookie["sameSite"] not in ["Strict", "Lax", "None"]:
                cookie["sameSite"] = "None"

        # if "expiry" in cookie:
        #     cookie["expiry"] = int(cookie["expiry"])
        driver.add_cookie(cookie)
    driver.refresh()

    # Semakin lama semakin aman (tidak mencurigakan), tapi semakin memakan waktu pula
    secs = random.randint(7, 10)
    time.sleep(secs)

    try:
        companyDiv = driver.find_element(
            By.CLASS_NAME, "job-details-jobs-unified-top-card__company-name"
        )
        company = companyDiv.text

        div = driver.find_element(
            By.CLASS_NAME, "jobs-description-content__text--stretch"
        )
        descDiv = div.find_element(By.CSS_SELECTOR, "p[dir='ltr']")
        html_content = descDiv.get_attribute("innerHTML")

        desc_soup = BeautifulSoup(html_content, "html.parser")

        ul = desc_soup.find_all("ul")

        if len(ul) == 0:

            # Periksa tag <ol>, LinkedIn biasanya menggunakan tag tersebut juga
            ol = desc_soup.find_all("ol")

            if len(ol) == 0:
                # Jika tag <ol> juga tidak ada, maka yg disimpan adalah full description dari tag <div>, termasuk job_title dan company
                job_data.append(
                    {
                        "job_title": job_title,
                        "company": company,
                        "job_description": desc_soup.get_text(separator='\n', strip=True),
                    }
                )
                scraped += 1

            else:
                # Jika job description mengandung <ol>, maka:
                # Simpan menjadi data berisi job description yg didapat dari tag <ol>, termasuk job_title dan company
                job_desc = ""
                for ol in desc_soup.find_all("ol"):
                    for li in ol.find_all("li"):
                        job_desc += li.get_text(strip=True) + "\n"

                # append dilakukan diluar looping for, menghindari data terinput ganda jika terdapat lebih dari 1 element <ol>
                job_data.append(
                    {
                        "job_title": job_title,
                        "company": company,
                        "job_description": job_desc,
                    }
                )
                scraped += 1
        else:
            # Jika job description mengandung <ul>
            # Simpan menjadi data berisi job description yg didapat dari tag <ul>, termasuk job_title dan company
            job_desc = ""
            for ul in desc_soup.find_all("ul"):
                for li in ul.find_all("li"):
                    job_desc += li.get_text(strip=True) + "\n"

            # append dilakukan diluar looping for, menghindari data terinput ganda jika terdapat lebih dari 1 element <ul>
            job_data.append(
                {
                    "job_title": job_title,
                    "company": company,
                    "job_description": job_desc,
                }
            )
            scraped += 1

        print(f"Job ke-{i+1} Selesai")
    except NoSuchElementException:
        print(
            f"Job ke-{i+1} yaitu {job_title} dari perusahaan {company} (((MUNGKIN))) sudah dihapus, lanjut ke job selanjutnya!"
        )
    finally:
        driver.quit()

scraped_job = pd.DataFrame(job_data)

# Run menggunakan venv di directory "Code - Mapping to SFIA", ganti path sesuai kebutuhan!
scraped_job.to_excel(
    f"./Scraping/docs/{linkedin_params.job_category.lower()}/7 days v5/{linkedin_params.ISorCS_Jobs}_{linkedin_params.keyword_name.lower()}_{linkedin_params.job_portal}_7_days_v5.xlsx",
    index=False,
    engine="openpyxl"
)

print(
    f"Scraping berakhir pada jam {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"
)

end = time.perf_counter()
print(f"Scraping selesai dalam {end - start:.6f} detik")

print(f"Dari total {len(job_list)} job ID, total {scraped} job yg terscrap")