# JANGAN LUPA ISI & GANTI !!!!!
job_category = "Computer-Science"
keyword_name = "Computer-Science"
ISorCS_Jobs = "CSJobs"

url = "https://www.linkedin.com/voyager/api/voyagerJobsDashJobCards?decorationId=com.linkedin.voyager.dash.deco.jobs.search.JobSearchCardsCollection-220&count=25&q=jobSearch&query=(currentJobId:4249179077,origin:JOB_SEARCH_PAGE_SEARCH_BUTTON,keywords:Informatics%20Engineering,locationUnion:(geoId:102478259),selectedFilters:(distance:List(25),experience:List(2),function:List(it),timePostedRange:List(r604800)),spellCorrectionEnabled:true)&start=0"

# start 0 & 25 tidak pake tambahan &start=0/25 di akhir referer, berlaku mulai 25 dan kelipatannya untuk start 50 keatas (mulai kelipatan 25)
referer = "https://www.linkedin.com/jobs/search/?currentJobId=4249179077&distance=25&f_E=2&f_F=it&f_TPR=r604800&geoId=102478259&keywords=Informatics%20Engineering&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true"

csrf_token = "ajax:8372420043254646202"

cookies = """
bcookie="v=2&771833d2-423a-46f9-8ecd-b52e09c2e556"; bscookie="v=1&2023072700333299471909-a833-485a-8462-f011737abf7dAQHdvQXrNON792YHdZlrj8FHFqWy0DpN"; liap=true; li_theme=light; li_theme_set=app; dfpfpt=1643f42aa061488396eb44d9a6c075e1; JSESSIONID="ajax:8372420043254646202"; li_sugr=40a7dad7-86ec-41a3-8999-9070ceea57cd; timezone=Asia/Jakarta; aam_uuid=46975863097411011281491107078370194806; gpv_pn=www.linkedin.com%2Flegal%2Fcrawling-terms; s_ips=695; s_tp=2498; s_tslv=1746611665613; sdui_ver=sdui-flagship:0.1.3340; _guid=760d6bbe-43d3-4a1a-8197-ea76c153e72c; _gcl_au=1.1.1565081617.1749465310; lang=v=2&lang=en-us; li_at=AQEDAVQ7CoMEaL50AAABktGKaZYAAAGXqigMTk4AwBwigNRvnOqZiTX5b8rRSfmsFC3Fax1OMahcwj5WkarXPWVRoRTPrFfSi7LNbUPm4woSCM25qOiHlDMMXwyw6FDrTxOdfdxwY42-oRqzWiZ7tt7h; AnalyticsSyncHistory=AQKlgSDC3U262gAAAZeGG6IxAO0jwIrh7JgrrSgGma9VqJCDQuLM4rpajdDs8ejWjWvhdfwrgAkEIUyPsLIiDA; lms_ads=AQHv3E0Xfg-EngAAAZeGG6OwrU5YwisZCtfsWxzriXpX7Jt1miVGSqTn2N0bS_tZKiUlPe9fXrF_PJKMa10Lx8H--Kn0gXsR; lms_analytics=AQHv3E0Xfg-EngAAAZeGG6OwrU5YwisZCtfsWxzriXpX7Jt1miVGSqTn2N0bS_tZKiUlPe9fXrF_PJKMa10Lx8H--Kn0gXsR; fptctx2=taBcrIH61PuCVH7eNCyH0Iitb%252bEMfwlgK%252fM8w%252f28Ebfh%252ba9j16eYgjwSsiVSJ%252foSduFNVCHtJFFukofO6bTD6wAHHzdQ625xF5ofLQAUQun2yN7nHXyjuVvZTX6c2U2xm19A%252bQgm8Vm3r2%252bP3EDBGduiRR%252bCEjEmYqCatmZIamIdUZlxLH4ofSeoZMwq9Kn3jyDN8Yy4gcos8PHJLOUjyx%252bSQW%252b4su2EzMqG%252fBEgfsXSSYSSy6STPAiGWEm2KzIrPCB4bKS22oST7vvPIMo0M4H6gk9Hx%252bivMUIo%252fJbuEfHRS%252fMT75TLnqpGPKKABtHws4ze2Sy0iCeN7GrYK6q1UmqtzB2sYHoHJC8UxiZPA28%253d; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C20259%7CMCMID%7C47552414203496170271476713112280336061%7CMCAAMLH-1750914115%7C3%7CMCAAMB-1750914115%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1750316515s%7CNONE%7CMCCIDH%7C-415792049%7CvVersion%7C5.1.1; __cf_bm=FbUHhEd.O62UxFQ14fv1udaa.Peb4oh.yi3wS4UdFKA-1750310691-1.0.1.1-B8QbDLhSvXI8M66.0s7ZXlK6NoRzI42yM_Gm8OQSYB6AKCO1rYuAVMpCFuvrQe1pGcBXfVIH.Rzssm6UqIJZ6yESoCLIpxKrH8go4TuAgHE; UserMatchHistory=AQLJq-c7-rzrmwAAAZeGpnmvdexQrU7AGNzopb_kfFrAt6mtuU-_dLyAB4MgxaT8YpLNajZYcwYtR6F_GKaxdWvGigWSXUZOkHX4A54ZY04goEvH0Na5Ss0HkOgNAvyn75N1oJEOlpHc0MXTNKqtI_SXZbSlIo1ihHRAyeqYidy6FmHCCnU-w8Co3DfDX8tTlk1fde1C-mo0mzs1gcNmJEv8Ve26eY2zL05t34H4ZbFso6WwGtYZLNVBrSGevBr-5YwOb2VV61Xrul5btDYIqEFpKCd6RC8Bv_0DT56NWpEx22r3yv8OuzJbcJuEVlCrTzRLYTAgsYnzxNOEakN_mhee8S8X4iFuJlfpXer7tHhf0Ztkug; lidc="b=VB59:s=V:r=V:a=V:p=V:g=4614:u=14:x=1:i=1750310750:t=1750314774:v=2:sig=AQE2DFpXpSLcLl_fje24h_0rTSaDD3It"
"""

job_portal = "LinkedIn"

full_id_path_is = "Scraping/LinkedIn/id/fullID-ISJobs-Information-Systems-7_days.json"
full_id_path_cs = "Scraping/LinkedIn/id/fullID-CSJobs-Computer-Science-7_days.json"