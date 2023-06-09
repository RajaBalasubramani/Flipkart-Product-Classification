import requests
from bs4 import BeautifulSoup
import os

# Function to download and save the image
import requests
import os

# Function to save the image from a URL
def save_image_from_url(image_url, directory_path,search_term,name,page_no):
    # Check if the directory exists
    if not os.path.exists(directory_path+'/'+search_term):
        # Create the directory
        os.makedirs(directory_path+'/'+search_term)

    # Extract the filename from the image URL
    image_filename = page_no+name+ '.jpg'
    print(image_filename)
    save_path = os.path.join(directory_path+'/'+search_term, image_filename)

    # Send a GET request to the image URL
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Image saved: {save_path}")
    else:
        print(f"Failed to save image from URL: {image_url}")

def scrapimages(url,dir,search_term,page_no):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    div_img_tags = soup.find_all({'img':'_396cs4'})
    j=0
    for i in div_img_tags:
        image_url = i['src']

        if image_url.startswith('http') and any(ext in image_url for ext in ['.jpg', '.jpeg', '.png']):
            j += 1
            save_image_from_url(image_url,dir,search_term,str(j),str(page_no))



# Set the directory to save the images
save_directory = 'ecom Images'
for search_term in ['Books']:
    for i in range(1,11):
        url = f'https://www.flipkart.com/search?q={search_term}&page={i}'
        scrapimages(url, save_directory,search_term,i)