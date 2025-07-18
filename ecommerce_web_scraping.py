from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv
import time

def start_driver():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)

def get_categories(driver, url):
    driver.get(url)
    sidebar = driver.find_element(By.ID, "side-menu")
    links = sidebar.find_elements(By.TAG_NAME, "a")
    return [(a.text.strip(), a.get_attribute("href")) for a in links if a.text.strip() != "Home"]

def get_subcategories(driver, categories):
    subcategories = []
    for name, url in categories:
        driver.get(url)
        for sub in driver.find_elements(By.CLASS_NAME, "subcategory-link"):
            subcategories.append((name, sub.text.strip(), sub.get_attribute("href")))
    return subcategories

def extract_data(driver, category, subcategory, url):
    data = []
    driver.get(url)
    time.sleep(1)
    page = 1
    while True:
        products = driver.find_elements(By.CLASS_NAME, "product-wrapper")
        for p in products:
            name = p.find_element(By.CLASS_NAME, "title").text.strip()
            price = p.find_element(By.TAG_NAME, "h4").text.strip()
            desc = p.find_element(By.CLASS_NAME, "description").text.strip()
            reviews = p.find_element(By.CSS_SELECTOR, ".review-count span").text.strip()
            stars = len(p.find_element(By.CLASS_NAME, "ratings").find_elements(By.CSS_SELECTOR, "span.ws-icon-star"))
            data.append({
                'Category': category,
                'Subcategory': subcategory,
                'Name': name,
                'Price': price,
                'Description': desc,
                'Reviews': reviews,
                'Rating': stars
            })
        print(f"Scraping -> {category} > {subcategory} | Page {page} | Total produtos: {len(data)}", end="\r")
        try:
            next_btn = driver.find_element(By.CLASS_NAME, "next")
            if "disabled" in next_btn.get_attribute("class"):
                break
            next_btn.click()
            page += 1
            time.sleep(1)
        except:
            break
    print(f"Scraping -> {category} > {subcategory}")
    return data

def save_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def main():
    driver = start_driver()
    url = "https://webscraper.io/test-sites/e-commerce/ajax"
    categories = get_categories(driver, url)
    subcategories = get_subcategories(driver, categories)

    all_data = []
    for cat, sub, link in subcategories:
        all_data.extend(extract_data(driver, cat, sub, link))

    driver.quit()
    save_csv(all_data, 'ecommerce_data.csv')
    print("\nScraping complete. Data saved to 'ecommerce_data.csv'.")

if __name__ == "__main__":
    main()
