from django.shortcuts import render

from astro import astrocpp

import numpy as np
from scipy.spatial import Delaunay

import plotly.offline as py
import plotly.figure_factory as FF
import plotly.graph_objs as go

# Create your views here

def index(request):
    
    u = np.linspace(0, 2*np.pi, 24)
    v = np.linspace(-1, 1, 8)
    u,v = np.meshgrid(u,v)
    u = u.flatten()
    v = v.flatten()

    tp = 1 + 0.5*v*np.cos(u/2.)
    x = tp*np.cos(u)
    y = tp*np.sin(u)
    z = 0.5*v*np.sin(u/2.)

    points2D = np.vstack([u,v]).T
    tri = Delaunay(points2D)
    simplices = tri.simplices

    fig1 = FF.create_trisurf(x=x, y=y, z=z,
                             colormap="Portland",
                             simplices=simplices,
                             title="Mobius Band")
                             
    div = py.plot(fig1, auto_open=False, output_type='div')
    
    context = {
        'page': 'astro',
        'cpp_out': astrocpp.bindfunction(4),
        'graph': div,
    }
    
    return render(request, 'astro/index.html', context)