#!/usr/bin/env python3

from pptx import Presentation
from pptx.util import Inches, Pt
import itertools
import sys

file1 = "nameoffile"
file2 = "nameoffile"
file3 = "nameoffile"

with open(file1) as f1, open(file2) as f2, open(file3) as f3:
	filelist1 = f1.read().splitlines()
	filelist2 = f2.read().splitlines()
	filelist3 = f3.read().splitlines()
	lines = filelist1 + filelist2 + filelist3
	f1.close()
	f2.close()
	f3.close()
	#print(len(lines))

prs = Presentation()
bullet_slide_layout = prs.slide_layouts[1]

cycle = itertools.cycle(lines)
next(cycle)
for i in lines:
	next_line = next(cycle)
	slide = prs.slides.add_slide(bullet_slide_layout)
	shapes = slide.shapes
	body_shape = shapes.placeholders[1]
	tf = body_shape.text_frame
	tf.text = next_line

prs.save('test.pptx')
