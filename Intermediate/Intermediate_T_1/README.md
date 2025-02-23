INTERMEDIATE TASK 1

This folder contains a web scraper that can scrap data fron any website and stores it in csv file. This is a simple web scraper built using Python and BeautifulSoup. It extracts H1 and H2 headings from a webpage and saves them in a CSV file.

⚡ Features ✅ Extracts H1 and H2 headings from any webpage ✅ Saves the extracted data in a CSV file ✅ Uses BeautifulSoup for parsing HTML ✅ Simple and efficient automation

How to Run the Scraper :

1️⃣ Install Dependencies Make sure you have Python installed, then install BeautifulSoup: pip install beautifulsoup4 requests

2️⃣ Run the Script python scraper.py

3️⃣ Check the Output The extracted data is saved in scraped_data.csv. You can open it in Excel or a text editor.

🛠 How It Works

Sends a request to the target webpage
Parses the HTML using BeautifulSoup
Extracts H1 and H2 headings
Saves the data in scraped_data.csv
📝 Example Output (CSV File)

Heading Type,Text H1,Introduction to AI H2,Machine Learning Basics H2,Deep Learning Overview

🙌 Contributing Feel free to contribute! Fork the repo, create a new branch, and submit a pull request.

💡 Author Developed as part of ShadowFox Internship
