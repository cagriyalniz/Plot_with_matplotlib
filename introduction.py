#https://www.earthdatascience.org/courses/scientists-guide-to-plotting-data-in-python/plot-with-matplotlib/introduction-to-matplotlib-plots/
import matplotlib.pyplot as plt

def Plt1():
    fig, ax = plt.subplots()
    plt.show()

#plt.show() denildiginde tum plotları actigi icin fonksiyona gectim
def Plt2():
    fig2, ax2 = plt.subplots(figsize =(10,6))
    plt.show()

#multiplot figures
def MultiPlot():
    fig3, (ax3_1, ax3_2) = plt.subplots(1,2,figsize =(10,6))
    plt.show()

def MultiPlot2():
    fig, (ax1, ax2) = plt.subplots(2,1, figsize=(10,6))
    plt.show()

def MultiPlot3():
    fig, (ax1,ax2, ax3) = plt.subplots(1,3, figsize=(5,5))
    plt.show()

