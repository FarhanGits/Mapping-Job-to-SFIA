import time, random, json, pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# Import data berisi kumpulan job_id yang didapat, Run menggunakan venv di directory "Code - Mapping to SFIA", ganti path sesuai kebutuhan!
with open("./Scraping/docs/information-systems/jobID-IS-dump.json", "r") as data:
    job_list = json.load(data)

job_data_example = []
for job in job_list[:5]:  # hapus [:5] kalo mau mulai scraping benerannya
    job_title = job["title"]
    company = job["company"]
    job_url = f"https://id.jobstreet.com/job/{job['job_id']}"
    # print(job_url)

    driver = webdriver.Chrome()
    driver.get(job_url)

    # Semakin lama semakin aman (tidak mencurigakan), tapi semakin memakan waktu pula
    secs = random.randint(10, 15)
    time.sleep(secs)

    div = driver.find_element(By.CSS_SELECTOR, "div[data-automation='jobAdDetails']")

    ul = div.find_elements(By.TAG_NAME, "ul")

    if len(ul) == 0:

        # Periksa tag <ol>, Jobstreet biasanya menggunakan tag tersebut juga
        ol = div.find_elements(By.TAG_NAME, "ol")

        if len(ol) == 0:
            # Jika tag <ol> juga tidak ada, maka yg disimpan adalah full description dari tag <div>, termasuk job_title dan company
            # print(div.text)
            job_data_example.append(
                {
                    "job_title": job_title,
                    "company": company,
                    "job_description": div.text,
                }
            )

        else:
            # Jika job description mengandung <ol>, maka:
            # Simpan menjadi data berisi job description yg didapat dari tag <ol>, termasuk job_title dan company
            # print(list.text)
            job_desc = ""
            for list in ol:
                job_desc = job_desc + list.text + "\n"

            # append dilakukan diluar looping for, menghindari data terinput ganda jika terdapat lebih dari 1 element <ol>
            job_data_example.append(
                {
                    "job_title": job_title,
                    "company": company,
                    "job_description": job_desc.strip(),  # Hapus baris kosong di akhir karena terdapat newline (\n)
                }
            )
    else:
        # Jika job description mengandung <ul>
        # Simpan menjadi data berisi job description yg didapat dari tag <ul>, termasuk job_title dan company
        # print(list.text)
        job_desc = ""
        for list in ul:
            job_desc = job_desc + list.text + "\n"

        # append dilakukan diluar looping for, menghindari data terinput ganda jika terdapat lebih dari 1 element <ul>
        job_data_example.append(
            {
                "job_title": job_title,
                "company": company,
                "job_description": job_desc.strip(),  # Hapus baris kosong di akhir karena terdapat newline (\n)
            }
        )

    driver.quit()

dump_scraped_job = pd.DataFrame(job_data_example)

# Run menggunakan venv di directory "Code - Mapping to SFIA", ganti path sesuai kebutuhan!
dump_scraped_job.to_excel(
    "./Scraping/docs/information-systems/ISJobs-example-v2.xlsx", index=False
)
