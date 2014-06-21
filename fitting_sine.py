import numpy as np
import pylab as plb

def generate_data(Amp, freq, noise_amp):
    """
    Generates data x,y where 
    y= amp * sin(freq*x) + noise*randn()
    """
    x = np.arange(0.,80.,0.01)
    y= Amp * np.sin(freq*x) + 0.1*np.random.randn(len(y))
    return x,y

def plot_data(x,y,Amp,freq):
    """
    Plot the actual data point x,y along with the fit Amp*sin(freq*x)
    """
    plb.plot(x,y,'b',linestyle=':')
    y_fit = Amp*np.sin(freq*x)
    plb.plot(x,y_fit,'r')

def fit_data(x,y,fmin_method,init_guess=np.array([0.,0.])):
    """
    Fits data x,y to a sin wave using the fit method fimin_method. Returns fitted amplitude and frequency. Probably is unstable, so plot to check
    """
    def objective_func(A):
        return sum((y-A)**2)
    return fmin_method(objective_func,init_guess)
