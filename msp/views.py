from django.shortcuts import render
from .models import cropmsp
from plotly.offline import plot
from plotly.graph_objs import Scatter,Layout,Bar

#Rabi
def wheatmsp(request):
       
        b=cropmsp.objects.filter(crop_price=1975) 

        year = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020','2020-2021']
        msp = [1120, 1285, 1350, 1400, 1450, 1525,1625,1735, 1840, 1925, 1975]
        plot_div = plot({"data":[Bar(x=year, y=msp,marker_color="green",)] ,
        "layout":Layout(xaxis_title="Year from 2010-2021",yaxis_title="Market Support Price",plot_bgcolor="white",)},output_type='div')
        
        return render(request, "msp.html",{'plot_div': plot_div,'b':b})

def grammsp(request):

        b=cropmsp.objects.filter(msp_crop_title="Gram") 

        year = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020','2020-2021']
        msp = [2100,2800,3000,3100,3175,3500,4000,4400,4620,4875,5100]
        plot_div = plot({"data":[Bar(x=year, y=msp,marker_color="green",)] ,
        "layout":Layout(xaxis_title="Year from 2010-2021",yaxis_title="Market Support Price",plot_bgcolor="white",)},output_type='div')
        
        return render(request, "msp.html",{'plot_div': plot_div,'b':b})

def sunflowermsp(request):

        b=cropmsp.objects.filter(msp_crop_title="Sunflower")

        year = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020','2020-2021']
        msp = [2350,2800,3700,3700,3750,3800,3950,4100,5388,5650,5885]
        plot_div = plot({"data":[Bar(x=year, y=msp,marker_color="green",)] ,
        "layout":Layout(xaxis_title="Year from 2010-2021",yaxis_title="Market Support Price",plot_bgcolor="white",)},output_type='div')
        
        return render(request, "msp.html",{'plot_div': plot_div,'b':b})

def potatomsp(request):

        b=cropmsp.objects.filter(msp_crop_title="Potato")

        year = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020','2020-2021']
        msp = [800, 500, 1000, 1200, 2000, 625,650,300, 1100, 3500, 1500]
        plot_div = plot({"data":[Bar(x=year, y=msp,marker_color="green",)] ,
        "layout":Layout(xaxis_title="Year from 2010-2021",yaxis_title="Market Support Price",plot_bgcolor="white",)},output_type='div')
        
        return render(request, "msp.html",{'plot_div': plot_div,'b':b})

def onionmsp(request):

        b=cropmsp.objects.filter(msp_crop_title="Onion")

        year = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020','2020-2021']
        msp = [1500, 500,400, 2500, 1000, 600,700,300, 3700, 3200, 1000]
        plot_div = plot({"data":[Bar(x=year, y=msp,marker_color="green",)] ,
        "layout":Layout(xaxis_title="Year from 2010-2021",yaxis_title="Market Support Price",plot_bgcolor="white",)},output_type='div')
        
        return render(request, "msp.html",{'plot_div': plot_div,'b':b})

def tomatomsp(request):

        b=cropmsp.objects.filter(msp_crop_title="Tomato")

        year = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020','2020-2021']
        msp = [400, 200, 350, 500, 550, 1200,350,2800, 1100, 1400, 800]
        plot_div = plot({"data":[Bar(x=year, y=msp,marker_color="green",)] ,
        "layout":Layout(xaxis_title="Year from 2010-2021",yaxis_title="Market Support Price",plot_bgcolor="white",)},output_type='div')
        
        return render(request, "msp.html",{'plot_div': plot_div,'b':b})


#Kharif
def ricemsp(request):

        b=cropmsp.objects.filter(msp_crop_title="Rice")

        year = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020','2020-2021']
        msp = [1030,1110,1280,1345,1400,1450,1510,1590,1770,1835,1888]
        plot_div = plot({"data":[Bar(x=year, y=msp,marker_color="green",)] ,
        "layout":Layout(xaxis_title="Year from 2010-2021",yaxis_title="Market Support Price",plot_bgcolor="white",)},output_type='div')
        
        return render(request, "msp.html",{'plot_div': plot_div,'b':b})

def cornmsp(request):

        b=cropmsp.objects.filter(msp_crop_title="Corn")

        year = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020','2020-2021']
        msp = [880,980,1175,1310,1310,1325,1365,1425,1700,1760,1850]
        plot_div = plot({"data":[Bar(x=year, y=msp,marker_color="green",)] ,
        "layout":Layout(xaxis_title="Year from 2010-2021",yaxis_title="Market Support Price",plot_bgcolor="white",)},output_type='div')
        
        return render(request, "msp.html",{'plot_div': plot_div,'b':b})

def soyabeanmsp(request):

        b=cropmsp.objects.filter(msp_crop_title="Soyabean")

        year = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020','2020-2021']
        msp = [1440,1690,2240,2560,2560,2600,2775,3050,3399,3710,3880]
        plot_div = plot({"data":[Bar(x=year, y=msp,marker_color="green",)] ,
        "layout":Layout(xaxis_title="Year from 2010-2021",yaxis_title="Market Support Price",plot_bgcolor="white",)},output_type='div')
        
        return render(request, "msp.html",{'plot_div': plot_div,'b':b})

def cottonmsp(request):

        b=cropmsp.objects.filter(msp_crop_title="Cotton")

        year = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020','2020-2021']
        msp = [3000,3300,3900,4000,4050,4100,4160,4320,5450,5550,5825]
        plot_div = plot({"data":[Bar(x=year, y=msp,marker_color="green",)] ,
        "layout":Layout(xaxis_title="Year from 2010-2021",yaxis_title="Market Support Price",plot_bgcolor="white",)},output_type='div')
        
        return render(request, "msp.html",{'plot_div': plot_div,'b':b})

def sugarcanemsp(request):

        b=cropmsp.objects.filter(msp_crop_title="Sugarcane")

        year = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020','2020-2021']
        msp = [129.840, 139.120, 145, 170, 210, 220,230,255, 275, 285]
        plot_div = plot({"data":[Bar(x=year, y=msp,marker_color="green",)] ,
        "layout":Layout(xaxis_title="Year from 2010-2021",yaxis_title="Market Support Price",plot_bgcolor="white",)},output_type='div')
        
        return render(request, "msp.html",{'plot_div': plot_div,'b':b})

def moongmsp(request):

        b=cropmsp.objects.filter(msp_crop_title="Moong")

        year = ['2010-2011','2011-2012','2012-2013','2013-2014','2014-2015','2015-2016','2016-2017','2017-2018','2018-2019','2019-2020','2020-2021']
        msp = [3170,3500,4400,4500,4600,4850,5225,5575,6975,7050,7196]
        plot_div = plot({"data":[Bar(x=year, y=msp,marker_color="green",)] ,
        "layout":Layout(xaxis_title="Year from 2010-2021",yaxis_title="Market Support Price",plot_bgcolor="white",)},output_type='div')
        
        return render(request, "msp.html",{'plot_div': plot_div,'b':b})