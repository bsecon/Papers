# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 12:42:51 2021

@author: kevin
"""
import numpy as np
import matplotlib.pyplot as plt
import xlrd

def Confidence_plot(coefvals,civals,xrange, yrange, xlabel, ylabel, header) :

    coefvals_normalized=[i-coefvals[2] for i in coefvals]
    civals[2]=0

    #Plot graph
    plt.scatter(x, coefvals_normalized, color='blue')
    # plt.plot(x,Coef,color='blue',ls='',marker='o',markersize=5)
    plt.ylabel(ylabel, size = 'large')
    plt.xlabel(xlabel, size = 'large')
    plt.ylim(yrange)
    plt.xlim([xrange[0]-.5,xrange[1]+.5])
    plt.suptitle('Outcome: ' + header, fontsize = 'x-large')

    #Draw in red vertical line and black horizontal line
    plt.axvline(x=0, color='r', ls='--', lw=1)
    plt.axhline(y=0, color='black', lw=1)


    #Create the
    error=plt.errorbar(x, coefvals_normalized, yerr = civals, capsize = 3, fmt = '.',color='blue',marker='o',markersize=6)
    error[-1][0].set_linestyle('--')
    error[-1][0].set_linewidth(1.2)

    plt.xticks(np.arange(xrange[0],xrange[1]+1), fontsize=9)

    plt.tight_layout()
    
    #Save graph as pdf
    plt.savefig('Confidence_plot.pdf')    
    return 


if __name__ == "__main__":
    #location of file
    path = (r"event_study_employment.xls")

    #Read file and extract relevant columns for plot

    wb = xlrd.open_workbook(path)
    sheet = wb.sheet_by_index(0)
    coef = sheet.col_values(1, 17, 33)
    se = sheet.col_values(2, 17, 33)

    ci = [i*1.96 for i in se]
    x = [-1, -2, -3, -4, -5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    Confidence_plot(coef,ci,[-5,10], [-.04,.005], 'Year $\it{t}$ relative to job displacement', 'Employed', 'Employment Status')
