#https://www.earthdatascience.org/courses/scientists-guide-to-plotting-data-in-python/plot-with-matplotlib/introduction-to-matplotlib-plots/customize-plot-colors-labels-matplotlib/

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib as mplt

#   plot olusturma
#   renklendirme
#   eksenleri isimlendirme
#   iki plot ı aynı anda gosterme


# Monthly average precipitation
boulder_monthly_precip = [0.70, 0.75, 1.85, 2.93, 3.05, 2.02, 
                          1.93, 1.62, 1.84, 1.31, 1.39, 0.84]

# Month names for plotting
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", 
          "Aug", "Sept", "Oct", "Nov", "Dec"]


#Plot Your Data Using Matplotlib:

fig, ax1 = plt.subplots(figsize=(10,6))
#ax1.plot(x_axis, y_axis)
ax1.plot(months, boulder_monthly_precip)
#plt.show()

# **************************************
# *******************************
# dosyadan sonucları cekerek plot yapmak istedim
# once direkt sutun ismiyle cekebilecegimi dusundum olmadi
# dataframe e cevirip yapmam gerektigini dusundum yine olmadi
# sonra list yapmam gerektigini anladim
# list i range(len...) seklinde yapacaktim fakat sonra python oldugu aklima geldi,
#  asagidaki yontemle yaptim
results = pd.read_csv('exam_results.csv')
results.columns = ["İsim", "Soyisim", "SSN", "T1", "T2", "T3", "T4",
                "Final", "Grade"]

sonuc = pd.DataFrame(results["Grade"])
isim = results["İsim"][0]
print(isim)

print(type(isim))
#print(len(results))

#for i in range(len(results)):
    
def ExamPlot1():
    isimList = []
    for i in results["İsim"]:
        isimList.append(i)

    #print(isimList)
    gradeList = []
    for i in results["Grade"]:
        gradeList.append(i)
    fig2, ax2 = plt.subplots(figsize=(50,50))
    ax2.plot(isimList, gradeList)
    plt.show()

def ExamPlot2():
    finalList = []
    isimList = []
    for i in results["İsim"]:
        isimList.append(i)
    for i in results["Final"]:
        finalList.append(i)

    fig3, ax3 = plt.subplots(figsize=(20,20))
    ax3.scatter(finalList, isimList)
    #scatter arada cizgi olmadan plot cizer
    plt.show()

def BarPlot():
    
    boulder_monthly_precip = [0.70, 0.75, 1.85, 2.93, 3.05, 2.02, 
                            1.93, 1.62, 1.84, 1.31, 1.39, 0.84]

    months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", 
            "Aug", "Sept", "Oct", "Nov", "Dec"]

    fig, ax = plt.subplots(figsize=(10,6))

    ax.bar(months, boulder_monthly_precip)
    plt.show()
#BarPlot()

#Customize Plot Title and Axes Labels

def TitlePlot():
    boulder_monthly_precip = [0.70, 0.75, 1.85, 2.93, 3.05, 2.02, 
                            1.93, 1.62, 1.84, 1.31, 1.39, 0.84]

    months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", 
            "Aug", "Sept", "Oct", "Nov", "Dec"]

    fig, ax = plt.subplots(figsize=(10,6))

    ax.bar(months, boulder_monthly_precip)

    # Set plot title and axes labels
    ax.set(title = "Average Monthly Precipitation in Boulder, CO",
       xlabel = "Month",
       ylabel = "Precipitation (inches)")

    plt.show()
#TitlePlot()

def RotateLabels():
    boulder_monthly_precip = [0.70, 0.75, 1.85, 2.93, 3.05, 2.02, 
                            1.93, 1.62, 1.84, 1.31, 1.39, 0.84]

    months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", 
            "Aug", "Sept", "Oct", "Nov", "Dec"]

    fig, ax = plt.subplots(figsize=(10,6))

    ax.plot(months, boulder_monthly_precip)

    ax.set(title = "Average Monthly Precipitation in Boulder, CO",
       xlabel = "Month",
       ylabel = "Precipitation (inches)")

    plt.setp(ax.get_xticklabels(), rotation = 45)

    plt.show()
#RotateLabels()

def ChangeMarker():

    boulder_month_prec = boulder_monthly_precip
    mon = months
    fig, ax = plt.subplots(figsize=(10,3))
    ax.scatter(mon, 
        boulder_month_prec,
        marker = '<')

    ax.set(title = "Average Monthly Precipitation\nBoulder, CO",
       xlabel = "Month",
       ylabel = "Precipitation\n(inches)")

    plt.show()

#ChangeMarker()

def CustomizePlotColor():
    
    isimList = []
    for i in results["İsim"]:
        isimList.append(i)

    #print(isimList)
    gradeList = []
    for i in results["Grade"]:
        gradeList.append(i)
    fig2, ax2 = plt.subplots(figsize=(16,10))

    ax2.plot(isimList, gradeList,
            marker = 'o', color = 'red',  alpha = 0.3)
#alpha rengin transparanligini ayarlar
    ax2.set(title = "Dersi Geçme Durumu",
            xlabel = "Kişiler", ylabel = "Notlar")
    
    plt.show()
#CustomizePlotColor()

def CustomizeBarColor():

    boulder_month_prec = boulder_monthly_precip
    mon = months
    fig, ax = plt.subplots(figsize=(10,3))
    ax.bar(mon, 
        boulder_month_prec,
        color = 'white',
        edgecolor = 'red')

    ax.set(title = "Average Monthly Precipitation\nBoulder, CO",
       xlabel = "Month",
       ylabel = "Precipitation\n(inches)")

    plt.show()
#CustomizeBarColor()

def CustomizeScatterColor():

    boulder_month_prec = boulder_monthly_precip
    mon = months
    fig, ax = plt.subplots(figsize=(10,3))
    ax.scatter(mon, 
        boulder_month_prec,
        c = boulder_monthly_precip,
        cmap = 'YlGnBu'
#colormap = https://matplotlib.org/3.1.1/gallery/color/colormap_reference.html
        )

    ax.set(title = "Average Monthly Precipitation\nBoulder, CO",
       xlabel = "Month",
       ylabel = "Precipitation\n(inches)")

    plt.show()

#CustomizeScatterColor()

def MultiPlotFigures():
    fig, (ax1, ax2) = plt.subplots(2,1, figsize=(12,30))
    boulder_month_prec = boulder_monthly_precip
    mon = months
    october = [1.31, 1.31, 1.31, 1.31, 1.30, 1.30, 1.29, 1.33, 1.35, 1.35,
                1.38, 1.38, 1.39, 1.39, 1.39, 1.40, 1.40, 1.40, 1.40, 1.41,
                1.40, 1.41, 1.44, 1.44, 1.39, 1.38, 1.39, 1.40, 1.40, 1.40, 1.42]

#ekim ayinin gunlerini alabilecegimiz fonksiyonu bulamadigim icin for dongusuyle
#kendim olusturdum :(
    octDays= []
    for i in range(1, 32):
        octDays.append(i)

    ax1.bar(months, 
       boulder_month_prec,
       color = 'cyan', 
       edgecolor = 'darkblue')

    ax1.set(title = "Average Monthly Precipitation\nBoulder, CO",
    xlabel = "Month",
    ylabel = "Precipitation\n(inches)")

    ax2.scatter(octDays, 
    october,
    c = october,
    cmap = 'autumn')

    ax2.set(title = "\nAverage October Precipitation\nBoulder, CO",
    xlabel = "Days",
    ylabel = "Precipitation\n(inches)")

    plt.show()
#MultiPlotFigures()

def OneTitleForTwoPlot():
    # Define plot space
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))

    fig.suptitle("Average Monthly Precipitation for Boulder, CO", fontsize = 16)

    # Define x and y axes
    ax1.bar(months, 
        boulder_monthly_precip,
        color = 'cyan', 
        edgecolor = 'darkblue')

    # Set plot title and axes labels
    ax1.set(title = "Bar Plot",
        xlabel = "Month",
        ylabel = "Precipitation\n(inches)")

    # Define x and y axes
    ax2.scatter(months, 
            boulder_monthly_precip,
            c = boulder_monthly_precip,
            cmap = 'YlGnBu')

    # Set plot title and axes labels
    ax2.set(title = "Scatter Plot",
        xlabel = "Month",
        ylabel = "Precipitation\n(inches)")

    plt.show()

#OneTitleForTwoPlot()

def SavePlotAsImage():

    finalList = []
    isimList = []
    gradeList = []

    for i in results["Grade"]:
        gradeList.append(i)

    for i in results["İsim"]:
        isimList.append(i)

    for i in results["Final"]:
        finalList.append(i)

    fig, (ax1, ax2) = plt.subplots(2,1 , figsize=(40,40))
    fig.suptitle('SINAV BAŞARISI', fontsize = 16)

    ax1.scatter(isimList, finalList)
    ax1.set(title = "final notları",
            xlabel = 'öğrenciler',
            ylabel = 'notlar')
    
    ax2.plot(isimList, gradeList,
            marker = 'o', color = 'red',  alpha = 0.3)
#alpha rengin transparanligini ayarlar
    ax2.set(title = "Dersi Geçme Durumu",
            xlabel = "Kişiler", ylabel = "Notlar")


    plt.savefig("exam.png")
    plt.show()

#SavePlotAsImage()