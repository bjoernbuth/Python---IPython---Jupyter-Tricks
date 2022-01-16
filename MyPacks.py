from IPython.display import display_html
from itertools import chain,cycle

bj_imports_string = """import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print('import numpy as np')
print('import pandas as pd')
print('import matplotlib.pyplot as plt')
print('import seaborn as sns')
"""

bis = bj_imports_string

a = 3 
b = 4

def quad(x) :
    return(x*x)

class my_display(object):
    """Display HTML representation of multiple objects"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""

    def __init__(self, *args):
        self.args = args

    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                     for a in self.args)

    def __repr__(self):
       return '\n\n'.join(a + '\n' + repr(eval(a))
                       for a in self.args)


class myClass:
	def __init__(self,val):
		self.val=val
	def getVal(self):
		return self.val


def display_side_by_side(*args,titles=cycle([''])):
    html_str=''
    for df,title in zip(args, chain(titles,cycle(['</br>'])) ):
        html_str+='<th style="text-align:center"><td style="vertical-align:top">'
        html_str+=f'<h2>{title}</h2>'
        html_str+=df.to_html().replace('table','table style="display:inline"')
        html_str+='</td></th>'
    display_html(html_str,raw=True)
  
