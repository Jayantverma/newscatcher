from flask import Flask, jsonify, render_template
from flask import abort
from flask import make_response
from flask import request
import feedparser

def news(key):
	ans=[]
	
	company=key.lower()
	url=["https://economictimes.indiatimes.com/news/rssfeeds/1715249553.cms",
	"http://www.moneycontrol.com/rss/business.xml",
	"https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms",
	"http://rss.cnn.com/rss/money_news_companies.rss",
	"http://www.business-standard.com/rss/finance-103.rss",
	"http://www.business-standard.com/rss/companies-101.rss",
	"http://www.business-standard.com/rss/economy-policy-102.rss",
	"http://timesofindia.indiatimes.com/rssfeeds/1898055.cms",
	"https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms",
	"https://www.indiainfoline.com/rss/corporatenews.xml",
	"http://www.moneycontrol.com/rss/iponews.xml",
	]
	for u in url:
		feed=feedparser.parse(u)
		for item in feed["items"]:
			if item["title"].lower().find(company)!=-1:
				print(item["title"])
				ans.append(item["link"])
				ans.append(item["title"])





	return ans	

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['GET','POST'])
def get_tasks():
	if request.method == 'POST':
		na = request.form["Name"]
		return render_template('result.html', result = news(na))

if __name__ == '__main__':
    app.run(debug=True)




