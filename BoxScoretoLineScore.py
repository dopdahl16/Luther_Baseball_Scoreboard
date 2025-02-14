# Copyright (C) 2019 Daniel Opdahl (dopdahl16@gmail.com) Some Rights Reserved. 
# Permission to copy and modify is granted under the GNU General Public License v3.0 license
# Last revised 8/26/2019

import os

for file in os.listdir("\\path\\to\\LCBoxScores"):
    box_score = open("\\path\\to\\LCBoxScores\\"+file, "r")
    filename = file[:-5]
    line_score = open("\\path\\to\\LCBoxScores\\"+filename+".txt", "w")
    write_flag = False
    lines_to_write = 4
    
    ### The below iterates through the .html files line by line and finds the keyphrase "Score by Innings" which indicates that it and the next 3 lines are the line score. 
    
    for Line in box_score:
        if "Score by Innings" in Line:
            write_flag = True
        if write_flag == True:
            line_score.write(Line)
            lines_to_write-=1
        if lines_to_write == 0:
            write_flag = False
            break