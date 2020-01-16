import requests,bs4

class Review:
    reviewTitle=''
    reviewWriter=''
    reviewRating=''
    review=''
    reviewDate=''
    def __init__(self,reviewTitle,reviewWriter,reviewRating,review,reviewDate):
        self.reviewDate=reviewDate
        self.reviewTitle =reviewTitle
        self.reviewWriter =reviewWriter
        self.reviewRating = reviewRating
        self.review =review
    def toString(self):
        return self.reviewTitle+','+self.reviewWriter+','+sel.reviewDate+','+self.reviewRating+','+self.review

###get url
url = input('enter the imdb url:')

### TODO: Get webpage (Data Acquistion)
def getWebpage(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
    except:
        print('check url'+url)
    return res
            
### remove irrevelent data (Data Ingestion)

def getDataFromIMDB(htmlPage):
    webpageParsed = bs4.BeautifulSoup(htmlPage)
    dataFromWeb= webpageParsed.select('.review-container')
    return dataFromWeb
    
###  Identify required info(Data Label)
def identifyElements(reviewSoup):
    title=reviewSoup.select('.title')
    writer=reviewSoup.select('.display-name-link')
    date=reviewSoup.select('.review-date')
    rating=reviewSoup.select('.rating-other-user-rating')[0].text.strip()
    review=reviewSoup.select('.content')
    return Review(title,writer,rating,review,date)

imdbPage=getWebpage(url)
allReviewData = getDataFromIMDB(imdbPage.text)
results = []
for rawData in allReviewData:
    if rawData :
        results.append(identifyElements(rawData))


reviewsFile = open('reviews.csv','w')
reviewsFile.write(Review('Title','Writer','Rating','Review','Date').toString())
reviewsFile.write('\n')
for review in results:
    reviewsFile.write(review.tostring())
    reviewsFile.write('\n')
reviewsFile.close()

