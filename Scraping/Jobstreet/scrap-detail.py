import time, random, json, pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import jobstreet_params

# Cek lama waktu scraping
print(
    f"Scraping dimulai pada jam {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"
)
start = time.perf_counter()

# Import data berisi kumpulan job_id yang didapat, Run menggunakan venv di directory "Code - Mapping to SFIA", ganti path sesuai kebutuhan!
with open(f"./Scraping/{jobstreet_params.job_portal}/id/7 days v5/jobID-{jobstreet_params.ISorCS_Jobs}-{jobstreet_params.keyword_name}-7_days_v5.json", "r", encoding="utf-8") as data:
    job_list = json.load(data)

job_data_example = []
scraped = 0
for i, job in enumerate(job_list):
    job_title = job["job_title"]
    company = job["company"]
    job_url = f"https://id.jobstreet.com/job/{job['job_id']}"
    # print(job_url)

    # # Menghilangkan log warning saja
    # chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-logging")
    # chrome_options.add_argument("--log-level=3")

    driver = webdriver.Chrome()
    driver.get(job_url)

    # Semakin lama semakin aman (tidak mencurigakan), tapi semakin memakan waktu pula
    secs = random.randint(7, 10)
    time.sleep(secs)

    try:
        div = driver.find_element(
            By.CSS_SELECTOR, "div[data-automation='jobAdDetails']"
        )

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
                scraped += 1

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
                scraped += 1
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
            scraped += 1

        print(f"Job ke-{i+1} Selesai")
    except NoSuchElementException:
        print(
            f"Job ke-{i+1} yaitu {job_title} dari perusahaan {company} sudah dihapus, lanjut ke job selanjutnya!"
        )
    finally:
        driver.quit()

scraped_job = pd.DataFrame(job_data_example)

# Run menggunakan venv di directory "Code - Mapping to SFIA", ganti path sesuai kebutuhan!
scraped_job.to_excel(
    f"./Scraping/docs/{jobstreet_params.job_category.lower()}/7 days v5/{jobstreet_params.ISorCS_Jobs}_{jobstreet_params.keyword_name.lower()}_{jobstreet_params.job_portal}_7_days_v5.xlsx",
    index=False, engine="openpyxl"
)

print(
    f"Scraping berakhir pada jam {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"
)

end = time.perf_counter()
print(f"Scraping {jobstreet_params.job_portal} kategori {jobstreet_params.job_category} u/ keyword {jobstreet_params.keyword_name} selesai dalam {end - start:.6f} detik")

print(f"Dari total {len(job_list)} job ID, total {scraped} job yg terscrap")