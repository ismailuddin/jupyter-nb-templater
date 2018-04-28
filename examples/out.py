# `nb_templater` generated Python script
# Generated from .ipynb template: test.ipynb
# www.github.com/ismailuddin/nb-templater/
# Generated on: 2018-04-28 15:00 

import nbformat as nbf 
import sys
nb = nbf.v4.new_notebook() 

cell_0="""\
## Test template notebook
"""

cell_1="""\
Paragraph
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Donec odio. Quisque volutpat mattis eros. Nullam malesuada erat ut turpis. Suspendisse urna nibh, viverra non, semper suscipit, posuere a, pede.

Donec nec justo eget felis facilisis fermentum. Aliquam porttitor mauris sit amet orci. Aenean dignissim pellentesque felis.

Morbi in sem quis dui placerat ornare. Pellentesque odio nisi, euismod in, pharetra a, ultricies in, diam. Sed arcu. Cras consequat.

Praesent dapibus, neque id cursus faucibus, tortor neque egestas auguae, eu vulputate magna eros eu erat. Aliquam erat volutpat. Nam dui mi, tincidunt quis, accumsan porttitor, facilisis luctus, metus.
"""

cell_2="""\
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
"""

cell_3="""\
sns.set(style="ticks")

df = sns.load_dataset("iris")
sns.pairplot(df, hue="species")
"""

nb['cells'] = [
    nbf.v4.new_markdown_cell(cell_0),
    nbf.v4.new_markdown_cell(cell_1),
    nbf.v4.new_code_cell(cell_2),
    nbf.v4.new_code_cell(cell_3)
]


nbf.write(nb, '_test.ipynb')
print("Jupyter notebook _test.ipynb successfully generated.")
