from flask import Flask,request,render_template,make_response,send_from_directory
import os


import urllib
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pdfkit
import cgi
from IPython.display import HTML
# form = cgi.FieldStorage()
# searchterm =  form.getvalue('searchbox')
# In[67]:

import bs4
from bs4 import BeautifulSoup as bs


def func(link):
    # fl = open('newDoc.txt')
    # s = fl.readline()

    # link = "https://www.flipkart.com/search?q=watches&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY"


    # In[69]:


    # f = urllib.request.urlopen(link)


    # In[70]:


    # myfile = f.read()


    # In[71]:


    # print(myfile)


    # In[72]:


    # my_request = urllib.request.urlopen("https://www.flipkart.com/search?q=watches&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY")


    # In[73]:


    # my_HTML = my_request.read().decode("utf8")


    # In[74]:


    # print(my_HTML)


    # In[ ]:





    # In[75]:


    # current_link = "https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    # link = current_link


    # In[76]:


    # page = requests.get(link)


    # In[77]:


    # page.content
    # # Gives the Raw Data of the Web Page


    # In[78]:


    names = []
    links = []
    prices = []
    star_list = []
    rating_list =[]


    # In[79]:


    link_list=[]
    var='https://www.flipkart.com'


    # In[80]:


    for i in range(5):
        current_link = link
        link = current_link+"&page="+str(i)
        page = requests.get(link)
        soup = bs(page.content, 'html.parser')
        products =soup.findAll('div',class_="_2kHMtA")
        for prod in products:
            prod_name = prod.find('div', attrs={'class':'_4rR01T'})
            prod_link = prod.find('a', attrs={'class':'_1fQZEK'})
            price = prod.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
            stars = prod.find('div', attrs={'class':'_3LWZlK'})
            no_of_ratings = prod.find('span', attrs={'class':'_2_R_DZ'})


            names.append(prod_name.text)
            links.append(prod_link.text)
            # prices.append(price.text)
            if price != None:
                prices.append(price.text)
            else:
                prices.append("Out of Stock")
            if stars != None:
                star_list.append(stars.text)
            else:
                star_list.append("0")

            if no_of_ratings != None:
                rating_list.append(no_of_ratings.text)
            else:
                rating_list.append("0")


        parser = 'html.parser'
        resp = urllib.request.urlopen(link)
        soup = bs(resp, parser, from_encoding=resp.info().get_param('charset'))

        for link_ in soup.find_all('a',attrs={'class':'_1fQZEK'}):
            link_list.append(var+link_['href'])



    # In[81]:


    # len(star_list)
    # print(star_list)
    # print(rating_list)


    # In[82]:


    #  soup = bs(page.content, 'html.parser')
     #it gives us the visual representation of data
    #  print(soup.prettify())


    # In[83]:


    # products =soup.findAll('div',class_="_2kHMtA")
    # print(products)


    # In[ ]:





    # In[84]:


    # for i in products:
    #     print(i.text)
    #     print('----------------------------------------------')


    # In[ ]:





    # In[85]:


    # for prod in products:
    #     prod_name = prod.find('div', attrs={'class':'_4rR01T'})
    #     prod_link = prod.find('a', attrs={'class':'_1fQZEK'})

    #     price = prod.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    #     stars = prod.find('div', attrs={'class':'_3LWZlK'})
    #     no_of_ratings = prod.find('span', attrs={'class':'_2_R_DZ'})

    #     names.append(prod_name.text)
    #     links.append(prod_link.text)
    #     prices.append(price.text)
    #     star_list.append(stars.text)
    #     rating_list.append(no_of_ratings.text)

    # print(names)
    # print('----------------------------------------------')
    # print(links)
    # print('----------------------------------------------')
    # print(prices)
    # print('----------------------------------------------')
    # print(star_list)
    # print('----------------------------------------------')
    # print(rating_list)




    # In[86]:


    # new_list=[]
    # for i in star_list:
    #     new_list.append(star_list[i])


    # In[87]:


    # len(names)


    # In[ ]:





    # In[88]:


    # pro_df=pd.DataFrame({'Product Name':names,'Links':links,'Price':prices,'STars':star_list,'No_of_Ratings':rating_list})


    # In[89]:


    # pro_df.head(10)


    # In[90]:


    # print(pro_df.STars)


    # In[91]:




    # parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed
    # resp = urllib.request.urlopen(link)
    # soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))

    # for link_ in soup.find_all('a',attrs={'class':'_1fQZEK'}):
    #     link_list.append(var+link_['href'])


    # In[ ]:





    # In[92]:



    # len(link_list)


    # In[93]:


    #  print(link_list)


    # In[94]:


    pro_df=pd.DataFrame({'Product Name':names,'Links':link_list,'Price':prices,'STars':star_list,'No_of_Ratings':rating_list})


    # In[95]:


    pro_df


    # In[96]:


    temp=[]
    new_temp=[]
    for i in rating_list:
        temp=i.split(' ')
        new_temp.append(temp[0])


    # In[97]:


    # print(new_temp)


    # In[98]:


    pro_df=pd.DataFrame({'Product Name':names,'Links':link_list,'Price':prices,'Stars':star_list,'No_of_Ratings':new_temp})
    # pro_df.head(10)


    # In[99]:


    rating_list=[]
    # rating_list=pro_df['No_of_Ratings'].astype(str)
    for i in pro_df['No_of_Ratings']:
        rating_list.append(int(i.replace(",","")))
    # print(rating_list)
    # type(rating_list[0])


    # In[100]:


    pro_df=pd.DataFrame({'Product Name':names,'Links':link_list,'Price':prices,'Stars':star_list,'No_of_Ratings':rating_list})
    # pro_df.head(10)



    # In[ ]:





    # In[101]:


    pro_df['Stars']=pro_df['Stars'].astype(float)


    # In[102]:


    pro_df['TOTAL']=pro_df['Stars']*pro_df['No_of_Ratings']


    # In[103]:


    # pro_df.head(10)


    # In[104]:


    pro_df.sort_values(['TOTAL'],axis=0,ascending=[False],inplace = True)


    # In[105]:


    # pro_df


    # In[106]:


    pro_df.reset_index(drop=True, inplace=True)


    # In[107]:


    # pro_df


    # In[108]:


    rank_list=[]
    temp=[]
    count=1
    temp=pro_df['TOTAL'].astype(float)

    for i in range(0,len(temp)-1):
        if  temp[i]==temp[i+1]:
            rank_list.append(count)
        else:
            rank_list.append(count)
            count=count+1
    rank_list.append(count)



    # In[109]:


    # rank_list


    # In[110]:


    pro_df['Rank'] = rank_list


    # In[111]:


    # pro_df


    # In[112]:


    df1, df2 = [x for _, x in pro_df.groupby(pro_df['Rank'] >= 11)]


    # In[113]:


    # df1


    # In[114]:


    df2 = df1[['Product Name', 'Links','Price','Rank']].copy()
    # print(df2)
    df2 = pd.DataFrame(df2)
    # df2


    # In[115]:


    temp = []
    price_rs = []
    temp = df2['Price']
    for s in temp:
        s = s[1:]
        s = "Rs."+s
        price_rs.append(s)

    # price_rs



    # In[116]:


    df2['Price'] = price_rs


    # In[117]:


    # pip install fpdf


    # In[118]:


    def make_clickable(url,name):
        return '<a href="{}" rel="noopener noreferrer" target="_blank">{}</a>'.format(url,name)

    df2['Links'] = df2.apply(lambda x: make_clickable(x['Links'],"Link"), axis=1)
    df2.style


    # In[119]:


    # df2.to_excel("output.xlsx")


    # In[120]:


    # # def make_clickable(val):
    # #     return '<a href="{}">{}</a>'.format(val,val)

    # df2.style.format({'Links': make_clickable})


    # In[121]:


    # import fpdf
    # from fpdf import FPDF


    # In[122]:


    # from pandas.plotting import table
    # import matplotlib.pyplot as plt

    # ax = plt.subplot(111, frame_on=True)
    # ax.xaxis.set_visible(0)
    # ax.yaxis.set_visible(0)
    # table(ax, df2, loc='upper center')
    # plt.savefig('res.pdf')


    # In[123]:



    # In[124]:


    result = df2.to_html(escape = False)
    # print(result)


    # In[125]:


    # HTML(df2.to_html(classes='table table-stripped'))


    # In[126]:


    type(result)


    # In[127]:


    # get_ipython().system('pip install pdfkit')


    # In[128]:


    # In[129]:


    config = pdfkit.configuration(wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    pdf = pdfkit.from_string(result, 'output.pdf', configuration = config)

    # In[130]:
    workingdir = os.path.abspath(os.getcwd())
    # filepath = workingdir + '/Flask/'
    return send_from_directory(workingdir, 'output.pdf')



    # response = make_response(pdf)
    # response.headers["Content-Type"] = "application/pdf"
    # response.headers["Content-Disposition"] = "inline; filename=output.pdf"
    # return response
