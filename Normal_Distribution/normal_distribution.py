import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def unknown_area_plot(lower = None, upper = None, mu = 0, sigma = 1, 
                      color = 'cornflowerblue', figsize = (10,6), shade = 'inside',
                     meancolor = 'white'):

    '''
    Generate a plot of a normal distbution, shaded between lower and upper.
    '''
    
    fontsize = 24
    
    nd = norm(loc = mu, scale = sigma)
    
    xmin = nd.ppf(0.001)
    xmax = nd.ppf(0.999)

    x = np.linspace(xmin, xmax, 1000)
    y = nd.pdf(x)
    
    plt.figure(figsize = figsize)
    
    plt.plot(x, y, color = 'black')

    # The x-axis
    plt.plot(x, [0]*len(x), color = 'black')
    
    ymin, ymax = plt.ylim()
    plt.ylim(-0.1*ymax, ymax)
    
    for val in [lower, upper]:
        if val:
            plt.annotate(s = str(val), xy = (val, -0.01*ymax), 
                         ha = 'center', va = 'top',
                        fontsize = fontsize)
            plt.vlines(x = val, ymin = 0, ymax = nd.pdf(val))
            
    if mu != 0:
        plt.annotate(s = str(mu), xy = (mu, 0),
                    ha = 'center', va = 'bottom', color = meancolor,
                    fontsize = fontsize -2)
        plt.vlines(x = mu, ymin = 0.075*ymax, ymax = nd.pdf(mu), linestyle = '--', color = meancolor)
        
    if not lower:
        lower = xmin
    if not upper:
        upper = xmax    
    
    if shade == 'inside':
        mask = (x >= lower) & (x <= upper)
        plt.fill_between(x[mask], y[mask], color = color)

    if shade == 'outside':
        mask = (x <= lower)
        plt.fill_between(x[mask], y[mask], color = color)
        mask = (x >= upper)
        plt.fill_between(x[mask], y[mask], color = color)
    
    plt.axis('off');