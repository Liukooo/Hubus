{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "61aa95aa8b7a43b793a5c28af32015b4",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "VBox(children=(HTML(value='<h1 style=\"color:blue; text-align:center\" >REAL TIME TRANSPORT</h1>'), HBox(childre…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from ipywidgets import Button,IntSlider, Label, VBox, HTML, HBox, Layout, Accordion,SelectMultiple\n",
    "import ipywidgets as widgets\n",
    "from IPython.display import display,clear_output\n",
    "from bqplot import pyplot as plt\n",
    "%matplotlib inline\n",
    "import matplotlib\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "\n",
    "limm=[]\n",
    "label = HTML( value='<h1 style=\"color:blue; text-align:center\" >REAL TIME TRANSPORT</h1>')\n",
    "\n",
    "\n",
    "\n",
    "#foto linea 6:\n",
    "imm=HTML(\"\"\"<img src=\"temp.png\">\"\"\")\n",
    "limm.append(imm)\n",
    "\n",
    "imm=HTML(\"\"\"<img src=\"l625.png\">\"\"\")\n",
    "limm.append(imm)\n",
    "\n",
    "imm=HTML(\"\"\"<img src=\"l626.png\">\"\"\")\n",
    "limm.append(imm)\n",
    "\n",
    "#foto grafico linea 9:\n",
    "imm=HTML(\"\"\"<img src=\"l92218.png\">\"\"\")\n",
    "limm.append(imm)\n",
    "\n",
    "\n",
    "imm=HTML(\"\"\"<img src=\"l925.png\">\"\"\")\n",
    "limm.append(imm)\n",
    "\n",
    "imm=HTML(\"\"\"<img src=\"temp2.png\">\"\"\")\n",
    "limm.append(imm)\n",
    "\n",
    "#foto grafico linea 11:\n",
    "imm=HTML(\"\"\"<img src=\"l1122.png\">\"\"\")\n",
    "limm.append(imm)\n",
    "\n",
    "imm=HTML(\"\"\"<img src=\"l1125.png\">\"\"\")\n",
    "limm.append(imm)\n",
    "\n",
    "imm=HTML(\"\"\"<img src=\"l1126.png\">\"\"\")\n",
    "limm.append(imm)\n",
    "\n",
    "accordion = widgets.Accordion(children=[widgets.SelectMultiple(options=['select','22/11/18', '25/11/18', '26/11/18'],value=['select'],rows=4,description='',disabled=False), \n",
    "                                        widgets.SelectMultiple(options=['select','22/11/18', '25/11/18', '26/11/18'],value=['select'],rows=4,description='',disabled=False),\n",
    "                                        widgets.SelectMultiple(options=['select','22/11/18', '25/11/18', '26/11/18'],value=['select'],rows=4,description='',disabled=False)])\n",
    "accordion.set_title(0, 'LINEA 6')\n",
    "accordion.set_title(1, 'LINEA 9')\n",
    "accordion.set_title(2, 'LINEA 11')\n",
    "\n",
    "\n",
    "width = 0.3\n",
    "i=0\n",
    "out = widgets.Output()\n",
    "\n",
    "        \n",
    "def pr0(change):\n",
    "    if change['new'][0]=='22/11/18':\n",
    "        t.layout.visibility = 'visible'\n",
    "        t.children = [limm[0]]\n",
    "    elif change['new'][0]=='25/11/18':\n",
    "        t.layout.visibility = 'visible'\n",
    "        t.children = [limm[1]]\n",
    "    elif change['new'][0]=='26/11/18':\n",
    "        #manual=(6,15,14,24,11,23,17,25,71,17,20,13,16,35,16,15)\n",
    "        t.layout.visibility = 'visible'\n",
    "        t.children = [limm[2]]\n",
    "        \n",
    "                        \n",
    "        \n",
    "def pr1(change):\n",
    "    if change['new'][0]=='22/11/18':\n",
    "        #manual=(3,16,6,13,8,2,5,10,9,9,10)\n",
    "        #dalle 7 alle 17\n",
    "        t.layout.visibility = 'visible'\n",
    "        t.children = [limm[3]]\n",
    "    elif change['new'][0]=='25/11/18':\n",
    "        t.layout.visibility = 'visible'\n",
    "        t.children = [limm[4]]\n",
    "         #N=15\n",
    "         #manual(1,1,2,6,7,5,5,7,6,8,2,5,8,6,4)\n",
    "         #dalle 7 alle 21\n",
    "    elif change['new'][0]=='26/11/18':\n",
    "        t.layout.visibility = 'visible'\n",
    "        t.children = [limm[5]]\n",
    "        #N=5\n",
    "        #dalle 7 alle 11\n",
    "        #manual=(3,17,15,18,17)\n",
    "\n",
    "def pr2(change):\n",
    "    if change['new'][0]=='22/11/18':\n",
    "        t.layout.visibility = 'visible'\n",
    "        t.children = [limm[6]]\n",
    "        #dalle 6 alle 21\n",
    "        #N=17\n",
    "        #manual=(5,11,32,19,7,10,13,11,11,16,15,10,18,12,10,5,1)\n",
    "    elif change['new'][0]=='25/11/18':\n",
    "        t.layout.visibility = 'visible'\n",
    "        t.children = [limm[7]]\n",
    "        #dalle 6 alle 21\n",
    "        #N=16\n",
    "        #manual=(2,3,5,6,9,26,12,21,22,15,20,16,11,15,15,9)\n",
    "    elif change['new'][0]=='26/11/18':\n",
    "        t.layout.visibility = 'visible'\n",
    "        t.children = [limm[8]]\n",
    "        #dalle 6 alle 21\n",
    "        #N=16\n",
    "        #manual=(5,14,21,11,5,11,14,12,18,16,11,17,17,8,7,8)\n",
    "\n",
    "\n",
    "accordion.children[0].observe(pr0,names=\"value\")\n",
    "accordion.children[1].observe(pr1,names=\"value\")\n",
    "accordion.children[2].observe(pr2,names=\"value\")\n",
    "\n",
    "\n",
    "gh=[]\n",
    "#Grafico home\n",
    "imm=HTML(\"\"\"<img src=\"sensor.png\">\"\"\")\n",
    "gh.append(imm)\n",
    "\n",
    "imm=HTML(\"\"\"<img src=\"manuale.png\">\"\"\")\n",
    "gh.append(imm)\n",
    "\n",
    "g=HBox([gh[0],gh[1]], layout= Layout(justify_content='center'))\n",
    "g.layout.positioning=\"right\"\n",
    "\n",
    "t = HBox([limm[8]],layout= Layout(justify_content='center'))\n",
    "t.layout.visibility='hidden'\n",
    "VBox([label,g,accordion,t])\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
