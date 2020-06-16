#!/usr/bin/env python3

from pptx import Presentation
from pptx.dml.color import RGBColor
import itertools

##################-Fill Out-###################
###############################################
file1 = "nameoffile"
file2 = "nameoffile"
file3 = "nameoffile"
###############################################
###############################################
powerpoint = powerpoint_name + ".pptx"
slide_master_template = "slide_master.pptx"
save_message = "Powerpoint was created!"
error_message = "Looks like there was an error :("

with open(file1) as f1, open(file2) as f2, open(file3) as f3:
	file1_list = f1.read().splitlines()
	file2_list = f2.read().splitlines()	
	file3_list = f3.read().splitlines()
	lines = list(file1_list + file2_list + file3_list)
	f1.close()
	f2.close()
	f3.close()
	
prs = Presentation(slide_master_template)
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

save = prs.save(powerpoint)
save
if [ save ]:
	print(save_message)
else:
	print(error_message)
