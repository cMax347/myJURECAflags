#!/usr/bin/env python3
import numpy as np
from lxml import etree
from os import path
#~
#~
#
#	read in kpt list
if path.exists('kpts'):
	kpts	=	np.loadtxt('kpts',skiprows=1, usecols=(0,1,2))
	nkpts	=	len(kpts)
	kweight	=	1.0/float(nkpts)
else:
	print('ERROR  no kpts file present')
	exit(1)
#~
#
#
# init the xml tree
xml_tree = etree.Element('kPointList')
xml_tree.set('posScale',	str(1.0))
xml_tree.set('weightScale',	str(1.0))
xml_tree.set('count',str(nkpts))
#
#
# add kpts to xml tree
for kpt in kpts:
	xml_kpt 		= etree.SubElement(xml_tree, 'kPoint')
	xml_kpt.set(		'weight',		str(kweight))	
	xml_kpt.text	= str(kpt[0])+' '+str(kpt[1])+' '+str(kpt[2])	
#~
#
# create a new XML file with the results
xml_out = etree.ElementTree(xml_tree)
xml_out.write("kpts.xml", pretty_print=True)
exit(0)
#~~~~~~~~~~~~~~~~~~~