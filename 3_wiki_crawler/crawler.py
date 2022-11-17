import os
import requests
from bs4 import BeautifulSoup
import random
from tqdm import tqdm


#Return list of the URL-addresses of types links or url-images
def get_images_urls(link):	
	images_urls = []
	try:
		html = requests.get(link, timeout=2.50)
		if html.status_code == 200:
			html_page = html.text
			soup = BeautifulSoup(html_page, 'html.parser')
			links = soup.find_all('img')
			for img in links:
				url = img.get('src', None)
				if url is not None:
					images_urls.append(fix_url(url))
	except:
		print("Unexpected error, unable to open the link")
	return images_urls


def get_urls_links(url_link):
	urls = []
	html = requests.get(url_link, timeout=2.50)
	if html.status_code == 200:
		html_page = html.text
		soup = BeautifulSoup(html_page, 'html.parser')
		links = soup.find_all('a')
		for link in links:
			url = link.get('href',None)
			if url is not None and not url.startswith('#'):
				urls.append(fix_url(url))
	return urls

# Return correct URL_address by adding the missing prefix
def fix_url(url_link):
	prefix_wiki = 'https://en.wikipedia.org'
	if url_link.startswith ('https:') or url_link.startswith ('http:'):
		return url_link
	elif url_link.startswith('//') or url_link.startswith('/author/'):
		url_fix_link = 'https:' + url_link
	else:
		url_fix_link = prefix_wiki + url_link
	return url_fix_link

#Save the images from the URLS in the dest_folder
def downlods_images(images_urls, dest_folder):
	os.chdir(dest_folder)
	for i in tqdm(range(len(images_urls))):
		try:
			response = requests.get(images_urls[i], timeout=2.50)
			if response.status_code == 200:
				fp = open(f'{i}.png', 'wb')
				fp.write(response.content)
				fp.close()
		except:
			print("Unexpected error, unable to download the image")
	os.chdir('..')

		
def remove_duplicates(list_urls):
	uniqe_list = []
	for url in list_urls:
		if url not in uniqe_list:
			uniqe_list.append(url)
	return uniqe_list
	
#Return the folder_name from the last section of the URL 
def folder_name(page_link):
	split_url = page_link.split('/')
	if split_url[-1] == '':
		split_url[-1] = split_url[-2]
	split_url[-1] = split_url[-1].translate({ord(i): None for i in '!@#?/+.$%^&*'})
	split_url[-1] = split_url[-1].translate({ord(i): ' ' for i in '-_)(][=:'})
	return split_url[-1]
	
#The main function, create a folder and save all the images from the page_link, and repeat recursively by width and depth number
def crawl(page_link, depth, width):
		name_for_folder = folder_name(page_link)
		if not os.path.isdir(name_for_folder):
			os.mkdir(name_for_folder)
			urls_images = get_images_urls(page_link)
			uniqe_urls_images = remove_duplicates(urls_images)
			downlods_images(uniqe_urls_images, name_for_folder)
			if depth > 1 and width > 0:
				os.chdir(name_for_folder)
				urls_links = get_urls_links(page_link)
				width_places = random.sample(urls_links ,min(width, len(urls_links)))
				for width_place in tqdm(width_places):
					crawl(width_place, depth-1, width)
				os.chdir('..')
	

def main():
	page_link = input("Enter page link: ")
	depth = int(input("Enter number for depth: "))
	width = int(input("Enter number for width: "))
	crawl(page_link, depth,width)
	
if __name__ == "__main__":
    main()

