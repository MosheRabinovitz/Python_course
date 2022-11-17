import json
import csv
from urllib.request import urlopen
from tqdm import tqdm

#Get list of ids of the 60 best works from thehackernews.com
def get_ids():
	try:
		with urlopen("https://hacker-news.firebaseio.com/v0/jobstories.json?print=pretty") as data:
			jobs_ids = json.loads(data.read())
		return jobs_ids
	except:
		print("An error occured in get_ids function")

#Get a list of specific details according to the id number
def get_job(job_id):
	try:
		with urlopen(f'https://hacker-news.firebaseio.com/v0/item/{job_id}.json?print=pretty') as job_id:
			job = json.loads(job_id.read())
			clean_job = [job.pop("id", None), job.pop("title", None), job.pop("url", None), job.pop("text", None)]
		return clean_job
	except:
		   print("An error occured in get_job function")

#Get a list of specific details of the jobs according to a list of id numbers
def get_all_jobs(jobs_ids):
	try:
		all_jobs = []
		for job in tqdm(jobs_ids):
			all_jobs.append(get_job(job))
		return all_jobs
	except:
		print("An error occured in get_all_jobs function")

#Create csv file named <file_name> and write the details 
def write_to_csv(file_name, all_jobs):
    with open(file_name, 'w+') as file:
        writer = csv.writer(file)
        writer.writerow(["ID","title","URL", "text"])
        for row in all_jobs:
            writer.writerow(row)

#The main function
def main():
	try:
		file_name = input("Please enter file name: ")
		while not (len(file_name) > 4 and file_name.endswith(".csv")):
			file_name = input("The file name must be csv file, Please enter a valid name: ")
		ids = get_ids()
		all_jobs = get_all_jobs(ids)
		write_to_csv(file_name, all_jobs)
		print("complete")
	except:
		print("something went wrong")

if __name__ == "__main__":
    main()
