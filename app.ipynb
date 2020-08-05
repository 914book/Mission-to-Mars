{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template\n",
    "from flask_pymongo import PyMongo\n",
    "import scraping"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use flask_pymongo to set up mongo connection\n",
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/mars_app\"\n",
    "mongo = PyMongo(app)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\")\n",
    "def index():\n",
    "   mars = mongo.db.mars.find_one()\n",
    "   return render_template(\"index.html\", mars=mars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "   mars = mongo.db.mars\n",
    "   mars_data = scraping.scrape_all()\n",
    "   mars.update({}, mars_data, upsert=True)\n",
    "   return \"Scraping Successful!\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    ".update(query_parameter, data, options)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "if __name__ == \"__main__\":\n",
    "   app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visit the mars nasa news site\n",
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Optional delay for loading the page\n",
    "browser.is_element_present_by_css(\"ul.item_list li.slide\", wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert the browser html to a soup object and then quit the browser\n",
    "html = browser.html\n",
    "news_soup = soup(html, 'html.parser')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "slide_elem = news_soup.select_one('ul.item_list li.slide')\n",
    "slide_elem.find(\"div\", class_='content_title')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use the parent element to find the first 'a' tag and save it as 'news_title'\n",
    "news_title = slide_elem.find(\"div\", class_='content_title').get_text()\n",
    "news_title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use the parent element to find the paragraph text\n",
    "news_p = slide_elem.find('div', class_=\"article_teaser_body\").get_text()\n",
    "news_p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def mars_news(browser):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Scrape Mars News\n",
    "    # Visit the mars nasa news site\n",
    "    url = 'https://mars.nasa.gov/news/'\n",
    "    browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Optional delay for loading the page\n",
    "    browser.is_element_present_by_css(\"ul.item_list li.slide\", wait_time=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert the browser html to a soup object and then quit the browser\n",
    "    html = browser.html\n",
    "    news_soup = soup(html, 'html.parser')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Add try/except for error handling\n",
    "    try:\n",
    "        slide_elem = news_soup.select_one(\"ul.item_list li.slide\")\n",
    "        # Use the parent element to find the first 'a' tag and save it as 'news_title'\n",
    "        news_title = slide_elem.find(\"div\", class_=\"content_title\").get_text()\n",
    "        # Use the parent element to find the paragraph text\n",
    "        news_p = slide_elem.find(\"div\", class_=\"article_teaser_body\").get_text()\n",
    "\n",
    "    except AttributeError:\n",
    "        return None, None\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "return news_title, news_p"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def featured_image(browser):\n",
    "    # Visit URL\n",
    "    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "    browser.visit(url)\n",
    "\n",
    "    # Find and click the full image button\n",
    "    full_image_elem = browser.find_by_id('full_image')[0]\n",
    "    full_image_elem.click()\n",
    "\n",
    "    # Find the more info button and click that\n",
    "    browser.is_element_present_by_text('more info', wait_time=1)\n",
    "    more_info_elem = browser.links.find_by_partial_text('more info')\n",
    "    more_info_elem.click()\n",
    "\n",
    "    # Parse the resulting html with soup\n",
    "    html = browser.html\n",
    "    img_soup = soup(html, 'html.parser')\n",
    "\n",
    "    # Add try/except for error handling\n",
    "    try:\n",
    "        # Find the relative image url\n",
    "        img_url_rel = img_soup.select_one('figure.lede a img').get(\"src\")\n",
    "\n",
    "    except AttributeError:\n",
    "        return None\n",
    "\n",
    "    # Use the base url to create an absolute url\n",
    "    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'\n",
    "\n",
    "    return img_url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def mars_facts():\n",
    "    # Add try/except for error handling\n",
    "    try:\n",
    "        # Use 'read_html' to scrape the facts table into a dataframe\n",
    "        df = pd.read_html('http://space-facts.com/mars/')[0]\n",
    "\n",
    "    except BaseException:\n",
    "        return None\n",
    "    \n",
    "    # Assign columns and set index of dataframe\n",
    "    df.columns=['Description', 'Mars']\n",
    "    df.set_index('Description', inplace=True)\n",
    "    \n",
    "    # Convert dataframe into HTML format, add bootstrap\n",
    "    return df.to_html()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}