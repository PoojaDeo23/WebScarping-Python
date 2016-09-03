
# coding: utf-8

# In[4]:

#Author: Pooja Deo, Abhishika Mittal, Ankit Gupta ,Andre 

import re, urllib2,os,sys,time
from bs4 import BeautifulSoup


# coding: utf-8

import urllib2,os,sys,time
browser=urllib2.build_opener()
urllib2.install_opener(browser)
browser.addheaders=[('User-agent', 'Mozilla/5.0')]

if not os.path.exists('Data'):
    os.mkdir('Data')

pagesToGet=80
page=1
Pg=1
for r in range(1,pagesToGet+1):
    #This url is used to iterate through search pages
    url='http://www.imdb.com/search/title?countries=us&has=business-info&languages=en&production_status=released&release_date=2005,2015&start='+str(page)+'&title_type=feature&user_rating=1.0,10'
    print url
    try:
        response=browser.open(url)
    except Exception as e:
        error_type, error_obj, error_info = sys.exc_info()
        print 'ERROR FOR LINK:',url
        print error_type, 'Line:', error_info.tb_lineno
        continue
    html=response.read()
    html= re.sub('[\s+]', '', html)
    matches=re.finditer('(?:<trclass="evendetailed">.*?<tdclass="title">.*?<ahref="(.*?)">.*?</tr>)|(?:<trclass="odddetailed">.*?<tdclass="title">.*?<ahref="(.*?)">.*?</tr>)',html)
    
    for M in matches:
        if M.group(1):
            movieURL=M.group(1)
        else: 
            movieURL=M.group(2)
        #This url is used to get movie html page 
        MoviepageURL=' http://www.imdb.com'+str(movieURL)
        try:
            response=browser.open(MoviepageURL)
       
    #interests=re.finditer('<a class="gsc_co_int" .*?>(.*?)</a>',InterestString)
        except Exception as e:
            error_type, error_obj, error_info = sys.exc_info()
            print 'ERROR FOR LINK:',url
            print error_type, 'Line:', error_info.tb_lineno
            continue
        html_movie=response.read()
        #write the page to a new html file
   
        fwriter=open('Data/'+str(Pg)+'.html','w')
        fwriter.write(str(html_movie))
        fwriter.close()
        Pg+=1
    
        #wait for 2 seconds
        time.sleep(2)
    page+=50


# In[ ]:



