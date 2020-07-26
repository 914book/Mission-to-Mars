{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'flask_pymongo'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-a51437e71967>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mflask\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mFlask\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrender_template\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mflask_pymongo\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mPyMongo\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mscraping\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'flask_pymongo'"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template\n",
    "from flask_pymongo import PyMongo\n",
    "import scraping"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'PyMongo' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-8d92e18fbc0d>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m# Use flask_pymongo to set up mongo connection\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mapp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mconfig\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m\"MONGO_URI\"\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m\"mongodb://localhost:27017/mars_app\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mmongo\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mPyMongo\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mapp\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'PyMongo' is not defined"
     ]
    }
   ],
   "source": [
    "# Use flask_pymongo to set up mongo connection\n",
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/mars_app\"\n",
    "mongo = PyMongo(app)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
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
   "execution_count": 5,
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
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-6-866eed795106>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-6-866eed795106>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    .update(query_parameter, data, options)\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    ".update(query_parameter, data, options)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n"
     ]
    }
   ],
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
