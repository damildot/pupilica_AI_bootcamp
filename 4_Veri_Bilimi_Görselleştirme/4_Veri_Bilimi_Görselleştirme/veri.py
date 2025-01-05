# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 11:23:26 2025

@author: Monster
"""

import plotly as py
import plotly.graph_objs as go
import plotly.offline as plot
from plotly.offline import plot


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

veri=pd.read_csv("universite_siralamasi.csv")
"""
eksik verilerin giderilmesi :
    öğrenci_sayısı
    öğrenci_çalışan_oranı
    uluslararası ögrenci
    kadın erkek oranı
    
    

boş değerlerden kurtulmanın en iyi çözümü silmek ancak başka değerleri çok fazla etkileyecekse 
bu yöntemi kullanmayız
gerçek projelerde direkt olarak ortalamayla dolduramayız

"""

"""
dünya_sıralaması 
veri.info
str

=, -, 600-800 ,aynı değerden birden fazla bu karakterlerin kaldırıp integera çevir
native language karakterler var (problem çıkarmaz ama sevmeyiz)
"""

"""
ulke de yazım yanlışları var unıted ->unted gibi
aynı ülke farklı isimlerle yazzılmış mı diye bakmak gerekiyor 
countplotla görselleştirilmesi gerekir
veri.ulke.unique()

öğretim de sıkıntı yok

international: nan değerler var ve floata çevrilmesi lazım

gelir ve toplam puan : kayıp veri ve floata çevrilmesi lazım
öğrenci_sayisi: kayıp veri ve floata çevrilmesi lazım

uluslararası_ögrenci : yüzdeleri kaldır
female_male_ratio : uluslarrası öğrenciler oranı gibi yazılması lazım kadınların oranı ayrılabilir 48:52 yerine -> 48

year: problem yok
"""


#%% plotly line + scatter plot


df =veri.iloc[:100,:]
#bir tane scatter plot oluşturalım 
cizgi1=go.Scatter(x=df.world_rank, #x ekseninde dünya sıralaması olsun
                  y=df.citations,
                  mode="lines+markers", #çizgi ve saçılım grafiği
                  name="citations",
                  marker= dict(color="rgba(78,78,250,0.85)"), #renk
                  text=df.university_name
                  
                  )
cizgi2=go.Scatter(x=df.world_rank, #x ekseninde dünya sıralaması olsun
                  y=df.teaching,
                  mode="lines+markers", #çizgi ve saçılım grafiği
                  name="teaching",
                  marker= dict(color="rgba(254,0,0,1)"), #renk
                  text=df.university_name
                  
                  )
#veri_= [cizgi1,cizgi2]

#yerlesim= dict(title ="ilk 100 alıntı puanı",xaxis=dict(title="dünya sıralaması"))
#fig=dict(data=veri_, layout=yerlesim)

#plot(fig, filename="plotly_cizgi1.html")

#%%bar plot 
veri2014=veri[veri.year==2014].iloc[:5,:]
bar1=go.Bar(x=veri2014.university_name,
            y=veri2014.citations,
            name="citations",
            marker=dict(color="rgba(255,255,39,0.5)", line=dict(color="rgba(0,0,0,0)",width=1.5)),
            text=veri2014.country)



bar2=go.Bar(x=veri2014.university_name,
            y=veri2014.teaching,
            name="teaching",
            marker=dict(color="rgba(255,255,39,0.5)", line=dict(color="rgba(0,0,0,0)",width=1.5)),
            text=veri2014.country)

                
veri_= [bar1,bar2]
"""
yerlesim= go.Layout(barmode="group")
fig=go.Figure(data=veri_,layout=yerlesim)
plot(fig,filename="plotly_bar.html")
"""

#%% exercise
"""
2015 yılına ait ilk 10 üninin öğretim skorlarını bar plot olarak alıntı skorlarını ise line+scatter
pllot olarak çizdirelim

"""




veri2015=veri[veri.year==2015].iloc[:10,:]
bar3=go.Bar(x=veri2015.university_name,
            y=veri2015.teaching,
            name="teaching",
            marker=dict(color="rgba(255,255,39,0.5)", line=dict(color="rgba(0,0,0,0)",width=1.5)),
            text=veri2015.country)



line3=go.Scatter(x=veri2015.university_name, #x ekseninde dünya sıralaması olsun
                  y=df.citations,
                  mode="lines+markers", #çizgi ve saçılım grafiği
                  name="citations",
                  marker= dict(color="rgba(254,0,0,1)"), #renk
                  text=df.university_name
                  
                  )
               
veri_= [bar3,line3]
"""
yerlesim= go.Layout(barmode="group")
fig=go.Figure(data=veri_,layout=yerlesim)
plot(fig,filename="plotly_bar_new.html")
"""

#%%pie chart

veri2016=veri[veri.year==2016].iloc[:10,:]
dilim1=veri2016.num_students
dilim1_list=[float(i.replace(",","")) for i in veri2016.num_students]
etiketler=veri2016.university_name

pie=go.Pie(labels= etiketler,
           values=dilim1_list,
           hoverinfo="label+value+percent",
           textinfo="value+percent",
           rotation=180,
           hole=0,
           marker=dict(line=dict(color="rgba(0,0,0,1)",width=1)))
"""
veri_=[pie]

yerlesim= dict(title="2016 yılı verileri")
fig=dict(data=veri_, layout=yerlesim)
plot(fig, filename="plotly_pie.html")
"""


#%% exercise
"""

"""
              
veri2016=veri[veri.year==2016].iloc[:8,:]
pie1=veri2016.income


pie=go.Pie(labels= veri2016.university_name,
           values=pie1,
           hoverinfo="label+value+percent",
           textinfo="value+percent",
           rotation=180,
           hole=0,
           marker=dict(line=dict(color="rgba(0,251,0,1)",width=1)))
"""
veri_=[pie]
yerlesim= dict(title="2016 yılı verileri")
fig=dict(data=veri_, layout=yerlesim)
plot(fig, filename="plotly_pie_new.html")
"""

#%%histogram
"""
veri2011=veri.student_staff_ratio[veri.year==2011]
veri2012=veri.student_staff_ratio[veri.year==2012]

hist1=go.Histogram(x=veri2011,
                   name=2011,
                   opacity=0.75,
                   marker=dict(color="rgba(0,251,0,1)"))

hist2=go.Histogram(x=veri2012,
                   name=2012,
                   opacity=0.75,
                   marker=dict(color="rgba(254,250,0,1)"))

veri_=[hist1,hist2]

yerlesim=go.Layout(title="2011 ve 2012 öğrenci çalışan oranı",xaxis=dict(title="öğrenci çalışan oranı"),yaxis=dict(title="frekans"))

fig=go.Figure(data=veri_,layout=yerlesim)

plot(fig,filename="plotly_histogram.html")
"""

#%%boxplot
"""
veri2015=veri[veri.year==2015].iloc[:100,:]

kutu1=go.Box(y=veri2015.total_score.astype(float),
             name="2015 toplam puan")

kutu2=go.Box(y=veri2015.research,
             name="2015 araştırma")


veri_=[kutu1,kutu2]

plot(veri_,filename="plotly_box.html")
"""
#toplam puan = sıralı olmayan yani float olmayan değerler sıralı gelmiyor düzenlememiz lazım


#%% exercise

"""
13 14 15 yılları için ilk 100 üniversite  box plot gösterimi
"""
"""
veri2015=veri[veri.year==2015].iloc[:100,:]
veri2014=veri[veri.year==2014].iloc[:100,:]
veri2013=veri[veri.year==2013].iloc[:100,:]

kutu1=go.Box(y=veri2015.student_staff_ratio.astype(float),
             name="2015 araştırma",
             text=veri2015.university_name+"/"+veri2015.country
             )

kutu2=go.Box(y=veri2014.student_staff_ratio,
             name="2014 araştırma",
             text=veri2014.university_name+"/"+veri2014.country)

kutu3=go.Box(y=veri2013.student_staff_ratio,
             name="2013 araştırma",
             text=veri2013.university_name+"/"+veri2013.country)

veri_=[kutu1,kutu2,kutu3]

plot(veri_,filename="plotly_box_new.html")
"""
#%% subplot
"""
veri2015=veri[veri.year==2015]
sub1=go.Scatter(x=veri2015.world_rank,
                y=veri2015.research,
                name="research",
                xaxis="x1",
                yaxis="y1")

sub2=go.Scatter(x=veri2015.world_rank,
                y=veri2015.citations,
                name="citations",
                xaxis="x2",
                yaxis="y2")


sub3=go.Scatter(x=veri2015.world_rank,
                y=veri2015.income,
                name="income",
                xaxis="x3",
                yaxis="y3")




sub4=go.Scatter(x=veri2015.world_rank,
                y=veri2015.total_score,
                name="total_score",
                xaxis="x4",
                yaxis="y4")



veri_=[sub1,sub2,sub3,sub4]

yerlesim=go.Layout(xaxis=dict(domain=[0,0.45]),
                   yaxis=dict(domain=[0,0.45]),
                   xaxis2=dict(domain=[0.55,1]),
                   yaxis2=dict(domain=[0,0.45],anchor="x2"),
                   xaxis3=dict(domain=[0,0.1],anchor="y3"),
                   yaxis3=dict(domain=[0.55,1]),
                   xaxis4=dict(domain=[0.2,1],anchor="y4"),
                   yaxis4=dict(domain=[0.55,1],anchor="x4")
                   )


fig=go.Figure(data=veri_,layout=yerlesim)
plot(fig,"plotly_subplot.html")
"""

#%% 3d
"""
veri2015=veri[veri.year==2015]
threeD=go.Scatter3d(x=veri2015.world_rank,
                    y=veri2015.research,
                    z=veri2015.citations,
                    mode="markers",
                    marker=dict(size=10,color="green"),
                    opacity=0.5)


veri_=[threeD]
yerlesim=go.Layout()
fig=go.Figure(data=veri_, layout=yerlesim)
plot(fig,filename="plotly_3d.html")
"""
#%% world map

veri2016=veri[veri.year==2016]
#veri2016.country.value_counts()

ulkeye_gore_toplam_veriler=veri2016.groupby("country").sum()
world_map=go.Choropleth(locations=ulkeye_gore_toplam_veriler.index,
              locationmode="country names",
              z=ulkeye_gore_toplam_veriler.index,
              autocolorscale=False,
              reversescale=True,
              colorscale="iceFire",
              colorbar=dict(title="araştırma puani"))


veri_=[world_map]
yerlesim=go.Layout(title="ülkelerin toplam araştırma puanları",
                   geo=dict(showframe=True,
                            showlakes=False,
                            showcoastlines=True,
                            projection=dict(type="natural earth")))


fig=dict(data=veri_, layout=yerlesim)
plot(fig,filename="plotly_world_map.html")


""""eksik verileri doldurmak için harici kaynak kullanabilirsiniz"""


