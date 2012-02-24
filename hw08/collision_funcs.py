#!/usr/bin/python env

# Calculate if a point is within a box
#    check if a point is inside a given box.  
#
#    Parameters:
#       pt: list of 2 numbers (x,y)
#       box: list of 4 numbers (x,y,w,h).  x,y is the top left point.  w,h is the width and height

def point_in_box(pt, box):
    pt1, pt2 = pt[0], pt[1]
    bpt1, bpt2 = box[0], box[1]
    wid, hi = box[2], box[3]

    return pt1 >= bpt1 and pt1 < bpt1 + wid and pt2 >= bpt2 and pt2 < bpt2 + hi
