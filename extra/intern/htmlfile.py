import urllib
import re,sys
url = 'https://www.indusind.com/personal-banking/payment-service/redeem-and-shop/offers/credit-card-offers.html'
htmlfile = urllib.urlopen(url)
htmltext = htmlfile.read()
titlelist = ["Dining Offers","Travel Offers","Lifestyle Offers","Entertainment Offers","Other Offers"]
i=0;
while i<len(titlelist):
	regextitle = '<a href="javascript:;" title="'+titlelist[i]+'">(.+?)</a>'
	patterntitle = re.compile(regextitle)
	title = re.findall(patterntitle,htmltext)
	print "title = ",
	print title
	print ""
	regextitledes = '<td>(.+?)</td>'
	patterntitledes = re.compile(regextitledes)
	titledes = re.findall(patterntitledes,htmltext)
	print "Image offer = ",
	print titledes[0]
	print ""
	print "title description =",
	print titledes[1]
	print ""
	regexterms = '<a class="tncLink" href="(.+?)" target="_blank">Click here</a>'
	patternterms = re.compile(regexterms)
	termsandconditions = re.findall(patternterms,htmltext)
	print "terms and conditions = ",
	print termsandconditions[i]
	print ""
	i+=1
linklist = ["www.flyingsquirrelholidays.com","http://www.expedia.co.in/indusind","http://www.flywidus.com"]
i=0
while i<len(linklist):
	regexlink = '<a target="_blank" href="(.+?)">'+linklist[i]+'</a>'
	patternlink = re.compile(regexlink)
	link = re.findall(patternlink,htmltext)
	print "Offer links = ",
	print link
	print ""
	i+=1
