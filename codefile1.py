import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch as fb
from matplotlib.patches import Arrow as Ar
from matplotlib.patches import FancyArrowPatch as Ar_f
from matplotlib.patches import Circle as cr
import matplotlib.image as mpimg
import matplotlib.patches as mpatches
import matplotlib.path as mpath
ducker_red_img = mpimg.imread('ducker_icon_red.png')
ducker_blue_img = mpimg.imread('ducker_icon_cyan.png')
ducker_yellow_img = mpimg.imread('ducker_icon_yellow.png')
ducker_orange_img = mpimg.imread('ducker_icon_orange.png')
ducker_purple_img = mpimg.imread('ducker_icon_purple.png')
fig,ax=plt.subplots()
x_limit=1350+100
y_limit=1000
x_offset=0
y_offset=0
ax.set_xlim(-100,x_limit+x_offset)
ax.set_ylim(-100,y_limit+y_offset)
plt.axis('off')

#
left_down_fb_width=600+350
left_down_fb_hight=600
left_down_fb_x=20
left_down_fb_y=20
left_down_fb=fb((left_down_fb_x,left_down_fb_y),left_down_fb_width,left_down_fb_hight,boxstyle="round,pad=0,rounding_size=50",linestyle='--',facecolor="white")
ax.add_patch(left_down_fb)
##
left_down_fb_inner_right_gap_width=180+50

left_down_inner_fb_horizantal_margin=40
left_down_inner_fb_vertical_margin=18

left_down_inner_fb_width=left_down_fb_width-2*left_down_inner_fb_horizantal_margin-left_down_fb_inner_right_gap_width
left_down_inner_fb_hight=left_down_fb_hight-2*left_down_inner_fb_vertical_margin
left_down_inner_fb_x=left_down_fb_x+left_down_inner_fb_horizantal_margin
left_down_inner_fb_y=left_down_fb_y+left_down_inner_fb_vertical_margin
left_down_inner_fb_=fb((left_down_inner_fb_x,left_down_inner_fb_y),left_down_inner_fb_width,left_down_inner_fb_hight,boxstyle="round,pad=0,rounding_size=50",linestyle='-',facecolor="white",linewidth=0.5)
ax.add_patch(left_down_inner_fb_)
##
left_down_inner_fb_right_horizantal_margin=20
left_down_inner_fb_right_width=left_down_fb_width-2*left_down_inner_fb_horizantal_margin-left_down_inner_fb_width-left_down_inner_fb_right_horizantal_margin
left_down_inner_fb_right_up_margin=80
left_down_inner_fb_right_down_margin=40
left_down_inner_fb_right_hight=left_down_inner_fb_hight-left_down_inner_fb_right_up_margin-left_down_inner_fb_right_down_margin
left_down_inner_fb_right_x=left_down_inner_fb_x+left_down_inner_fb_width+left_down_inner_fb_horizantal_margin
left_down_inner_fb_right_y=left_down_inner_fb_y+left_down_inner_fb_right_down_margin
left_down_inner_fb_right_=fb((left_down_inner_fb_right_x,left_down_inner_fb_right_y),left_down_inner_fb_right_width,left_down_inner_fb_right_hight,boxstyle="round,pad=0,rounding_size=50",linestyle='-',facecolor="whitesmoke",linewidth=0.3)
ax.add_patch(left_down_inner_fb_right_)


###
left_down_inner_fb_right_text_gap=80
left_down_inner_fb_right_y_offset=30
left_down_inner_fb_right_inner_box_vertical_gap=30
left_down_inner_fb_right_inner_box_horizantal_margin=20

left_down_inner_fb_right_inner_upper_fb_width=left_down_inner_fb_right_width-left_down_inner_fb_right_inner_box_horizantal_margin*2
left_down_inner_fb_right_inner_upper_fb_hight=(left_down_inner_fb_right_hight-left_down_inner_fb_right_text_gap-left_down_inner_fb_right_y_offset-left_down_inner_fb_right_inner_box_vertical_gap*2)/3
left_down_inner_fb_right_inner_upper_fb_x=left_down_inner_fb_right_x+left_down_inner_fb_right_inner_box_horizantal_margin
left_down_inner_fb_right_inner_upper_fb_y=left_down_inner_fb_right_y+left_down_inner_fb_right_hight-left_down_inner_fb_right_text_gap-left_down_inner_fb_right_inner_upper_fb_hight
left_down_inner_fb_right_inner_upper_fb=fb((left_down_inner_fb_right_inner_upper_fb_x,left_down_inner_fb_right_inner_upper_fb_y),left_down_inner_fb_right_inner_upper_fb_width,left_down_inner_fb_right_inner_upper_fb_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="white",linewidth=0.2)
ax.add_patch(left_down_inner_fb_right_inner_upper_fb)
###
left_down_inner_fb_right_inner_middle_fb_y=left_down_inner_fb_right_inner_upper_fb_y-left_down_inner_fb_right_inner_box_vertical_gap-left_down_inner_fb_right_inner_upper_fb_hight
left_down_inner_fb_right_inner_middle_fb=fb((left_down_inner_fb_right_inner_upper_fb_x,left_down_inner_fb_right_inner_middle_fb_y),left_down_inner_fb_right_inner_upper_fb_width,left_down_inner_fb_right_inner_upper_fb_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="white",linewidth=0.2)
ax.add_patch(left_down_inner_fb_right_inner_middle_fb)
###
left_down_inner_fb_right_inner_lower_fb_y=left_down_inner_fb_right_inner_middle_fb_y-left_down_inner_fb_right_inner_box_vertical_gap-left_down_inner_fb_right_inner_upper_fb_hight
left_down_inner_fb_right_inner_lower_fb=fb((left_down_inner_fb_right_inner_upper_fb_x,left_down_inner_fb_right_inner_lower_fb_y),left_down_inner_fb_right_inner_upper_fb_width,left_down_inner_fb_right_inner_upper_fb_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="white",linewidth=0.2)
ax.add_patch(left_down_inner_fb_right_inner_lower_fb)
###-->
mid_margin=30

down_mid_Arrow_x=left_down_inner_fb_right_inner_upper_fb_x+left_down_inner_fb_right_inner_upper_fb_width+left_down_inner_fb_right_inner_box_horizantal_margin
down_mid_Arrow_upper_y= left_down_inner_fb_right_inner_upper_fb_y+left_down_inner_fb_right_inner_upper_fb_hight/2
down_mid_Arrow_dx= mid_margin+left_down_inner_fb_right_horizantal_margin
down_mid_Arrow_upper=Ar(down_mid_Arrow_x,down_mid_Arrow_upper_y,down_mid_Arrow_dx,0, width=50,facecolor="black")
ax.add_patch(down_mid_Arrow_upper)
###-->
down_mid_Arrow_middle_y=left_down_inner_fb_right_inner_middle_fb_y+left_down_inner_fb_right_inner_upper_fb_hight/2
down_mid_Arrow_middle=Ar(down_mid_Arrow_x,down_mid_Arrow_middle_y,down_mid_Arrow_dx,0, width=50,facecolor="black")
ax.add_patch(down_mid_Arrow_middle)
###-->
down_mid_Arrow_lower_y=left_down_inner_fb_right_inner_lower_fb_y+left_down_inner_fb_right_inner_upper_fb_hight/2
down_mid_Arrow_lower=Ar(down_mid_Arrow_x+down_mid_Arrow_dx,down_mid_Arrow_lower_y,-down_mid_Arrow_dx,0, width=50,facecolor="black")
ax.add_patch(down_mid_Arrow_lower)
##txt
plt.text(left_down_inner_fb_right_inner_upper_fb_x+left_down_inner_fb_right_inner_upper_fb_width/2,left_down_inner_fb_right_y+left_down_inner_fb_right_hight+left_down_inner_fb_right_up_margin/2,"MWMS",fontsize="small",ha="center")
###txt
plt.text(left_down_inner_fb_right_inner_upper_fb_x+left_down_inner_fb_right_inner_upper_fb_width/2,left_down_inner_fb_right_y+left_down_inner_fb_right_hight-left_down_inner_fb_right_text_gap/1.5,"Controller",fontsize="small",ha="center")
####txt
plt.text(left_down_inner_fb_right_inner_upper_fb_x+left_down_inner_fb_right_inner_upper_fb_width/2,left_down_inner_fb_right_inner_upper_fb_y+left_down_inner_fb_right_inner_upper_fb_hight/2+10,"Cloud",fontsize="x-small",ha="center")
####txt
plt.text(left_down_inner_fb_right_inner_upper_fb_x+left_down_inner_fb_right_inner_upper_fb_width/2,left_down_inner_fb_right_inner_upper_fb_y+left_down_inner_fb_right_inner_upper_fb_hight/2-30,"Manager",fontsize="x-small",ha="center")

####txt
plt.text(left_down_inner_fb_right_inner_upper_fb_x+left_down_inner_fb_right_inner_upper_fb_width/2,left_down_inner_fb_right_inner_middle_fb_y+left_down_inner_fb_right_inner_upper_fb_hight/2+10,"Container",fontsize="x-small",ha="center")
####txt
plt.text(left_down_inner_fb_right_inner_upper_fb_x+left_down_inner_fb_right_inner_upper_fb_width/2,left_down_inner_fb_right_inner_middle_fb_y+left_down_inner_fb_right_inner_upper_fb_hight/2-30,"Alocator",fontsize="x-small",ha="center")

####txt
plt.text(left_down_inner_fb_right_inner_upper_fb_x+left_down_inner_fb_right_inner_upper_fb_width/2,left_down_inner_fb_right_inner_lower_fb_y+left_down_inner_fb_right_inner_upper_fb_hight/2,"Monitor",fontsize="x-small",ha="center")

#

right_fb_width=x_limit-mid_margin-left_down_fb_x-left_down_fb_width-left_down_fb_x
right_fb_x=left_down_fb_x+mid_margin+left_down_fb_width
right_fb_y=20
right_fb_hight=y_limit-right_fb_y-20
right_fb=fb((right_fb_x,right_fb_y),right_fb_width,right_fb_hight,boxstyle="round,pad=0,rounding_size=50",linestyle='--',facecolor="white")
ax.add_patch(right_fb)
##
right_text_gap=70
right_loweer_gap=400
right_inner_upper_fb_horizantal_margin=15
right_inner_upper_fb_vertical_margin=20
right_inner_upper_fb_width=right_fb_width-right_inner_upper_fb_horizantal_margin*2
right_inner_upper_fb_hight=right_fb_hight-right_text_gap-right_loweer_gap-right_inner_upper_fb_vertical_margin*2
right_inner_upper_fb_x=right_fb_x+right_inner_upper_fb_horizantal_margin
right_inner_upper_fb_y=right_fb_y+right_loweer_gap+right_inner_upper_fb_vertical_margin
right_inner_upper_fb=fb((right_inner_upper_fb_x,right_inner_upper_fb_y),right_inner_upper_fb_width,right_inner_upper_fb_hight,boxstyle="round,pad=0,rounding_size=50",linestyle='-',facecolor="white",linewidth=0.4)
ax.add_patch(right_inner_upper_fb)
##
right_inner_lower_fb_width=right_inner_upper_fb_width
right_inner_lower_fb_hight=right_loweer_gap-right_inner_upper_fb_vertical_margin*2
right_inner_lower_fb_x=right_inner_upper_fb_x
right_inner_lower_fb_y=right_fb_y+right_inner_upper_fb_vertical_margin
right_inner_lower_fb=fb((right_inner_lower_fb_x,right_inner_lower_fb_y),right_inner_lower_fb_width,right_inner_lower_fb_hight,boxstyle="round,pad=0,rounding_size=50",linestyle='-',facecolor="white",linewidth=0.4)
ax.add_patch(right_inner_lower_fb)
###
right_small_boxes_horizantal_margin=20
right_small_boxes_verital_gap=30
right_small_boxes_parent_fb_horizantal_padding=40
right_small_box_template_x=right_inner_lower_fb_x+right_small_boxes_horizantal_margin
right_small_box_template_width=right_inner_lower_fb_width-right_small_boxes_horizantal_margin*2
right_small_box_template_hight=(right_inner_lower_fb_hight-2*right_small_boxes_parent_fb_horizantal_padding-right_small_boxes_verital_gap*2)/3

right_small_box_1=fb((right_small_box_template_x,right_inner_lower_fb_y+right_small_boxes_parent_fb_horizantal_padding+right_small_box_template_hight+right_small_boxes_verital_gap),right_small_box_template_width,right_small_box_template_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="whitesmoke",linewidth=0.2)
ax.add_patch(right_small_box_1)

right_small_box_2=fb((right_small_box_template_x,right_inner_lower_fb_y+right_small_boxes_parent_fb_horizantal_padding),right_small_box_template_width,right_small_box_template_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="whitesmoke",linewidth=0.2)
ax.add_patch(right_small_box_2)

right_small_box_3=fb((right_small_box_template_x,right_inner_lower_fb_y+right_small_boxes_parent_fb_horizantal_padding+right_small_box_template_hight*2+right_small_boxes_verital_gap*2),right_small_box_template_width,right_small_box_template_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="whitesmoke",linewidth=0.2)
ax.add_patch(right_small_box_3)

#now upper box
right_small_box_4=fb((right_small_box_template_x,right_inner_upper_fb_y+right_small_boxes_parent_fb_horizantal_padding),right_small_box_template_width,right_small_box_template_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="whitesmoke",linewidth=0.2)
ax.add_patch(right_small_box_4)
right_small_box_5=fb((right_small_box_template_x,right_inner_upper_fb_y+right_small_boxes_parent_fb_horizantal_padding+right_small_box_template_hight+right_small_boxes_verital_gap),right_small_box_template_width,right_small_box_template_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="whitesmoke",linewidth=0.2)
ax.add_patch(right_small_box_5)
right_small_box_6=fb((right_small_box_template_x,right_inner_upper_fb_y+right_inner_upper_fb_hight-right_small_boxes_parent_fb_horizantal_padding-right_small_box_template_hight),right_small_box_template_width,right_small_box_template_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="whitesmoke",linewidth=0.2)
ax.add_patch(right_small_box_6)
#now box texts
right_small_box_text_gaps=70
plt.text(right_small_box_template_x+right_small_box_template_width-right_small_box_text_gaps,right_small_box_4.get_y()+right_small_box_template_hight/2,"VMa3",fontsize="xx-small")
plt.text(right_small_box_template_x+right_small_box_template_width-right_small_box_text_gaps,right_small_box_5.get_y()+right_small_box_template_hight/2,"VMa2",fontsize="xx-small")
plt.text(right_small_box_template_x+right_small_box_template_width-right_small_box_text_gaps,right_small_box_6.get_y()+right_small_box_template_hight/2,"VMa1",fontsize="xx-small")
plt.text(right_small_box_template_x+right_small_box_template_width-right_small_box_text_gaps,right_small_box_3.get_y()+right_small_box_template_hight/2,"VMb3",fontsize="xx-small")
plt.text(right_small_box_template_x+right_small_box_template_width-right_small_box_text_gaps,right_small_box_2.get_y()+right_small_box_template_hight/2,"VMb2",fontsize="xx-small")
plt.text(right_small_box_template_x+right_small_box_template_width-right_small_box_text_gaps,right_small_box_1.get_y()+right_small_box_template_hight/2,"VMb1",fontsize="xx-small")

#now upper text 
plt.text(right_small_box_template_x,right_fb_y+right_fb_hight-right_text_gap/1.5,"Hybrid cloud",fontsize="small")
#now lower text
plt.text(right_small_box_template_x,right_inner_lower_fb_y+right_inner_lower_fb_hight-right_small_boxes_parent_fb_horizantal_padding/1.4,"  cloud to",fontsize="x-small")
###########icons
whale_icon_size=100
ducker_image_horizantal_gap=20
ducker_image_vertical_gap=20
#orange ones
extent_r_1 = [right_small_box_template_x+ducker_image_horizantal_gap, right_small_box_template_x-ducker_image_horizantal_gap + whale_icon_size, right_small_box_1.get_y()+right_small_box_template_hight/2-whale_icon_size/2+ducker_image_vertical_gap,right_small_box_1.get_y()+right_small_box_template_hight/2+whale_icon_size/2-ducker_image_vertical_gap]
plt.imshow(ducker_orange_img, extent=extent_r_1,zorder=4)
extent_r_2 = [right_small_box_template_x+ducker_image_horizantal_gap, right_small_box_template_x-ducker_image_horizantal_gap + whale_icon_size, right_small_box_2.get_y()+right_small_box_template_hight/2-whale_icon_size/2+ducker_image_vertical_gap,right_small_box_2.get_y()+right_small_box_template_hight/2+whale_icon_size/2-ducker_image_vertical_gap]
plt.imshow(ducker_orange_img, extent=extent_r_2,zorder=4)
extent_r_3 = [right_small_box_template_x+ducker_image_horizantal_gap, right_small_box_template_x-ducker_image_horizantal_gap + whale_icon_size, right_small_box_3.get_y()+right_small_box_template_hight/2-whale_icon_size/2+ducker_image_vertical_gap,right_small_box_3.get_y()+right_small_box_template_hight/2+whale_icon_size/2-ducker_image_vertical_gap]
plt.imshow(ducker_orange_img, extent=extent_r_3,zorder=4)
#purple ones
extent_r_1_2 = [extent_r_1[1]+ducker_image_horizantal_gap*2, extent_r_1[1] + whale_icon_size, right_small_box_1.get_y()+right_small_box_template_hight/2-whale_icon_size/2+ducker_image_vertical_gap,right_small_box_1.get_y()+right_small_box_template_hight/2+whale_icon_size/2-ducker_image_vertical_gap]
plt.imshow(ducker_purple_img, extent=extent_r_1_2,zorder=4)
extent_r_2_2 = [extent_r_2[1]+ducker_image_horizantal_gap*2, extent_r_2[1] + whale_icon_size, right_small_box_2.get_y()+right_small_box_template_hight/2-whale_icon_size/2+ducker_image_vertical_gap,right_small_box_2.get_y()+right_small_box_template_hight/2+whale_icon_size/2-ducker_image_vertical_gap]
plt.imshow(ducker_purple_img, extent=extent_r_2_2,zorder=4)
extent_r_3_2 = [extent_r_3[1]+ducker_image_horizantal_gap*2, extent_r_3[1] + whale_icon_size, right_small_box_3.get_y()+right_small_box_template_hight/2-whale_icon_size/2+ducker_image_vertical_gap,right_small_box_3.get_y()+right_small_box_template_hight/2+whale_icon_size/2-ducker_image_vertical_gap]
plt.imshow(ducker_purple_img, extent=extent_r_3_2,zorder=4)
#red ones
extent_r_6 = [right_small_box_template_x+ducker_image_horizantal_gap, right_small_box_template_x-ducker_image_horizantal_gap + whale_icon_size, right_small_box_6.get_y()+right_small_box_template_hight/2-whale_icon_size/2+ducker_image_vertical_gap,right_small_box_6.get_y()+right_small_box_template_hight/2+whale_icon_size/2-ducker_image_vertical_gap]
plt.imshow(ducker_red_img, extent=extent_r_6,zorder=4)
extent_r_5 = [right_small_box_template_x+ducker_image_horizantal_gap, right_small_box_template_x-ducker_image_horizantal_gap + whale_icon_size, right_small_box_5.get_y()+right_small_box_template_hight/2-whale_icon_size/2+ducker_image_vertical_gap,right_small_box_5.get_y()+right_small_box_template_hight/2+whale_icon_size/2-ducker_image_vertical_gap]
plt.imshow(ducker_red_img, extent=extent_r_5,zorder=4)
#yellow ones
extent_r_6_2 = [extent_r_6[1]+ducker_image_horizantal_gap*2, extent_r_6[1] + whale_icon_size, right_small_box_6.get_y()+right_small_box_template_hight/2-whale_icon_size/2+ducker_image_vertical_gap,right_small_box_6.get_y()+right_small_box_template_hight/2+whale_icon_size/2-ducker_image_vertical_gap]
plt.imshow(ducker_yellow_img, extent=extent_r_6_2,zorder=4)
extent_r_5_2 = [extent_r_5[1]+ducker_image_horizantal_gap*2, extent_r_5[1] + whale_icon_size, right_small_box_5.get_y()+right_small_box_template_hight/2-whale_icon_size/2+ducker_image_vertical_gap,right_small_box_5.get_y()+right_small_box_template_hight/2+whale_icon_size/2-ducker_image_vertical_gap]
plt.imshow(ducker_yellow_img, extent=extent_r_5_2,zorder=4)
extent_r_4 = [right_small_box_template_x+ducker_image_horizantal_gap, right_small_box_template_x-ducker_image_horizantal_gap + whale_icon_size, right_small_box_4.get_y()+right_small_box_template_hight/2-whale_icon_size/2+ducker_image_vertical_gap,right_small_box_4.get_y()+right_small_box_template_hight/2+whale_icon_size/2-ducker_image_vertical_gap]
plt.imshow(ducker_yellow_img, extent=extent_r_4,zorder=4)
#blue ones
extent_r_6_3 = [extent_r_6_2[1]+ducker_image_horizantal_gap*2, extent_r_6_2[1] + whale_icon_size, right_small_box_6.get_y()+right_small_box_template_hight/2-whale_icon_size/2+ducker_image_vertical_gap,right_small_box_6.get_y()+right_small_box_template_hight/2+whale_icon_size/2-ducker_image_vertical_gap]
plt.imshow(ducker_blue_img, extent=extent_r_6_3,zorder=4)
extent_r_5_3 = [extent_r_5_2[1]+ducker_image_horizantal_gap*2, extent_r_5_2[1] + whale_icon_size, right_small_box_5.get_y()+right_small_box_template_hight/2-whale_icon_size/2+ducker_image_vertical_gap,right_small_box_5.get_y()+right_small_box_template_hight/2+whale_icon_size/2-ducker_image_vertical_gap]
plt.imshow(ducker_blue_img, extent=extent_r_5_3,zorder=4)
extent_r_4_2 = [extent_r_4[1]+ducker_image_horizantal_gap*2, extent_r_4[1] + whale_icon_size, right_small_box_4.get_y()+right_small_box_template_hight/2-whale_icon_size/2+ducker_image_vertical_gap,right_small_box_4.get_y()+right_small_box_template_hight/2+whale_icon_size/2-ducker_image_vertical_gap]
plt.imshow(ducker_blue_img, extent=extent_r_4_2,zorder=4)
#now fancy box
#down
ax.add_patch(fb((right_small_box_template_x,right_inner_lower_fb_y+right_small_boxes_parent_fb_horizantal_padding),whale_icon_size,right_small_box_template_hight*3+right_small_boxes_verital_gap*2,boxstyle="round,pad=0,rounding_size=50",linestyle='--',facecolor=(0.1, 0.2, 0.5, 0)))
#up
ax.add_patch(fb((right_small_box_template_x,right_small_box_5.get_y()),whale_icon_size,right_small_box_template_hight*3+right_small_boxes_verital_gap*2,boxstyle="round,pad=0,rounding_size=50",linestyle='--',facecolor=(0.1, 0.2, 0.5, 0)))

#
top_horizantal_margin=15
midle_gap_size=260
top_fb_width=left_down_fb_width-top_horizantal_margin*2
top_fb_x=left_down_fb_x+top_horizantal_margin
top_fb_y=20+left_down_fb_hight+midle_gap_size
top_fb_hight=y_limit-top_fb_y-20
top_fb=fb((top_fb_x,top_fb_y),top_fb_width,top_fb_hight,boxstyle="round,pad=0,rounding_size=50",linestyle='--',facecolor=(0,0,0,0))
ax.add_patch(top_fb)
##
user_img = mpimg.imread('user-286.png')
image_size=top_fb_hight
image_horizantal_gap=150
##lower section
extent1 = [top_fb_x+image_horizantal_gap-image_size/2, top_fb_x +image_horizantal_gap+ image_size/2, top_fb_y, top_fb_y+image_size]
plt.imshow(user_img, extent=extent1)

extent2 = [top_fb_x-image_horizantal_gap+top_fb_width-image_size/2, top_fb_x -image_horizantal_gap+top_fb_width+ image_size/2, top_fb_y, top_fb_y+image_size]
plt.imshow(user_img, extent=extent2)

extent3 = [top_fb_x+top_fb_width/2-image_size/2, top_fb_x +top_fb_width/2+ image_size/2, top_fb_y, top_fb_y+image_size]
plt.imshow(user_img, extent=extent3)
#text
plt.text(top_fb_x+top_fb_width-55,top_fb_y+top_fb_hight/2.5,"Users",fontsize="small",ha="center")


plt.imshow(user_img, extent=extent1)

extent2 = [top_fb_x-image_horizantal_gap+top_fb_width-image_size/2, top_fb_x -image_horizantal_gap+top_fb_width+ image_size/2, top_fb_y, top_fb_y+image_size]
plt.imshow(user_img, extent=extent2)
#
small_fb_margins=20
small_left_fb_width=(left_down_fb_width-2*small_fb_margins-2*top_horizantal_margin)/3
small_left_fb_x=left_down_fb_x+top_horizantal_margin
small_left_fb_y=20+left_down_fb_hight+40
small_left_fb_hight=midle_gap_size-80
small_left_fb=fb((small_left_fb_x,small_left_fb_y),small_left_fb_width,small_left_fb_hight,boxstyle="round,pad=0,rounding_size=50",linestyle='-',facecolor="white",linewidth=0.5)
ax.add_patch(small_left_fb)
##
small_box_template_width=30
small_box_template_hight=50
#
small_mid_fb=fb((small_left_fb_x+small_fb_margins+small_left_fb_width,small_left_fb_y),small_left_fb_width,small_left_fb_hight,boxstyle="round,pad=0,rounding_size=50",linestyle='-',facecolor="white",linewidth=0.5)
ax.add_patch(small_mid_fb)
#
small_right_fb=fb((small_left_fb_x+small_fb_margins*2+small_left_fb_width*2,small_left_fb_y),small_left_fb_width,small_left_fb_hight,boxstyle="round,pad=0,rounding_size=50",linestyle='-',facecolor="white",linewidth=0.5)
ax.add_patch(small_right_fb)
#
##-->
top_To_mid_ar_left=Ar(extent1[0]+30,top_fb_y,0,-(top_fb_y-small_left_fb_y-small_left_fb_hight), width=30,facecolor="black")
ax.add_patch(top_To_mid_ar_left)
top_from_mid_ar_left=Ar(extent1[1]-30,small_left_fb_y+small_left_fb_hight,0,(top_fb_y-small_left_fb_y-small_left_fb_hight), width=30,facecolor="black")
ax.add_patch(top_from_mid_ar_left)
top_To_mid_ar_mid=Ar(extent3[0]+30,top_fb_y,0,-(top_fb_y-small_left_fb_y-small_left_fb_hight), width=30,facecolor="black")
ax.add_patch(top_To_mid_ar_mid)
top_from_mid_ar_mid=Ar(extent3[1]-30,small_left_fb_y+small_left_fb_hight,0,(top_fb_y-small_left_fb_y-small_left_fb_hight), width=30,facecolor="black")
ax.add_patch(top_from_mid_ar_mid)
top_To_mid_ar_right=Ar(extent2[0]+30,top_fb_y,0,-(top_fb_y-small_left_fb_y-small_left_fb_hight), width=30,facecolor="black")
ax.add_patch(top_To_mid_ar_right)
top_from_mid_ar_right=Ar(extent2[1]-30,small_left_fb_y+small_left_fb_hight,0,(top_fb_y-small_left_fb_y-small_left_fb_hight), width=30,facecolor="black")
ax.add_patch(top_from_mid_ar_right)
##
small_mid_boxes_vertical_padding=10
smalle_c_fb_template_hight=(small_left_fb_hight-small_mid_boxes_vertical_padding*4)/2
smalle_c_fb_template_width=30
##middle one
small_mid_boxes_midle_horizantal_padding=30
s_m_fb_inner_1_fb_x=small_mid_fb.get_x()+ small_left_fb_width/2-smalle_c_fb_template_width/2
s_m_fb_inner_1_fb_y=small_left_fb_y+small_mid_boxes_vertical_padding
s_m_fb_inner_1_fb=fb((s_m_fb_inner_1_fb_x,s_m_fb_inner_1_fb_y),smalle_c_fb_template_width,smalle_c_fb_template_hight,boxstyle="round,pad=0,rounding_size=1",linestyle='-',facecolor="white",linewidth=0.3)
ax.add_patch(s_m_fb_inner_1_fb)
s_m_fb_inner_2_fb_x=small_mid_fb.get_x()+ small_left_fb_width/2-smalle_c_fb_template_width/2
s_m_fb_inner_2_fb_y=small_left_fb_y+small_left_fb_hight-small_mid_boxes_vertical_padding-smalle_c_fb_template_hight
s_m_fb_inner_2_fb=fb((s_m_fb_inner_2_fb_x,s_m_fb_inner_2_fb_y),smalle_c_fb_template_width,smalle_c_fb_template_hight,boxstyle="round,pad=0,rounding_size=1",linestyle='-',facecolor="white",linewidth=0.3)
ax.add_patch(s_m_fb_inner_2_fb)
s_m_fb_inner_3_fb_x=small_mid_fb.get_x()+small_mid_boxes_midle_horizantal_padding
s_m_fb_inner_3_fb_y=small_left_fb_y+small_left_fb_hight/2-smalle_c_fb_template_hight/2
s_m_fb_inner_3_fb=fb((s_m_fb_inner_3_fb_x,s_m_fb_inner_3_fb_y),smalle_c_fb_template_width,smalle_c_fb_template_hight,boxstyle="round,pad=0,rounding_size=1",linestyle='-',facecolor="white",linewidth=0.3)
ax.add_patch(s_m_fb_inner_3_fb)
s_m_fb_inner_4_fb_x=small_mid_fb.get_x()+small_left_fb_width-small_mid_boxes_midle_horizantal_padding-smalle_c_fb_template_width
s_m_fb_inner_4_fb_y=small_left_fb_y+small_left_fb_hight/2-smalle_c_fb_template_hight/2
s_m_fb_inner_4_fb=fb((s_m_fb_inner_4_fb_x,s_m_fb_inner_4_fb_y),smalle_c_fb_template_width,smalle_c_fb_template_hight,boxstyle="round,pad=0,rounding_size=1",linestyle='-',facecolor="white",linewidth=0.3)
ax.add_patch(s_m_fb_inner_4_fb)
##right one
s_r_fb_inner_horizantal_fb_gap=(small_left_fb_width-2*small_mid_boxes_midle_horizantal_padding-4*smalle_c_fb_template_width)/3
s_r_fb_inner_1_fb_x=small_right_fb.get_x()+small_mid_boxes_midle_horizantal_padding
s_r_fb_inner_1_fb_y=small_left_fb_y+small_left_fb_hight/2-smalle_c_fb_template_hight/2
s_r_fb_inner_1_fb=fb((s_r_fb_inner_1_fb_x,s_r_fb_inner_1_fb_y),smalle_c_fb_template_width,smalle_c_fb_template_hight,boxstyle="round,pad=0,rounding_size=1",linestyle='-',facecolor="white",linewidth=0.3)
ax.add_patch(s_r_fb_inner_1_fb)
s_r_fb_inner_4_fb_x=small_right_fb.get_x()+small_left_fb_width-small_mid_boxes_midle_horizantal_padding-smalle_c_fb_template_width
s_r_fb_inner_4_fb_y=small_left_fb_y+small_left_fb_hight/2-smalle_c_fb_template_hight/2
s_r_fb_inner_4_fb=fb((s_r_fb_inner_4_fb_x,s_r_fb_inner_4_fb_y),smalle_c_fb_template_width,smalle_c_fb_template_hight,boxstyle="round,pad=0,rounding_size=1",linestyle='-',facecolor="white",linewidth=0.3)
ax.add_patch(s_r_fb_inner_4_fb)
s_r_fb_inner_2_fb_x=s_r_fb_inner_1_fb_x+smalle_c_fb_template_width+s_r_fb_inner_horizantal_fb_gap
s_r_fb_inner_2_fb_y=small_left_fb_y+small_left_fb_hight/2-smalle_c_fb_template_hight/2
s_r_fb_inner_2_fb=fb((s_r_fb_inner_2_fb_x,s_r_fb_inner_2_fb_y),smalle_c_fb_template_width,smalle_c_fb_template_hight,boxstyle="round,pad=0,rounding_size=1",linestyle='-',facecolor="white",linewidth=0.3)
ax.add_patch(s_r_fb_inner_2_fb)
s_r_fb_inner_3_fb_x=s_r_fb_inner_2_fb_x+smalle_c_fb_template_width+s_r_fb_inner_horizantal_fb_gap
s_r_fb_inner_3_fb_y=small_left_fb_y+small_left_fb_hight/2-smalle_c_fb_template_hight/2
s_r_fb_inner_3_fb=fb((s_r_fb_inner_3_fb_x,s_r_fb_inner_3_fb_y),smalle_c_fb_template_width,smalle_c_fb_template_hight,boxstyle="round,pad=0,rounding_size=1",linestyle='-',facecolor="white",linewidth=0.3)
ax.add_patch(s_r_fb_inner_3_fb)
##left one
s_l_fb_inner_1_fb_x=small_left_fb_x+small_mid_boxes_midle_horizantal_padding
s_l_fb_inner_1_fb_y=small_left_fb_y+small_left_fb_hight/2-smalle_c_fb_template_hight/2
s_l_fb_inner_1_fb=fb((s_l_fb_inner_1_fb_x,s_l_fb_inner_1_fb_y),smalle_c_fb_template_width,smalle_c_fb_template_hight,boxstyle="round,pad=0,rounding_size=1",linestyle='-',facecolor="white",linewidth=0.3)
ax.add_patch(s_l_fb_inner_1_fb)
s_l_fb_inner_6_fb_x=small_left_fb_x+small_left_fb_width-small_mid_boxes_midle_horizantal_padding-smalle_c_fb_template_width
s_l_fb_inner_6_fb_y=small_left_fb_y+small_left_fb_hight/2-smalle_c_fb_template_hight/2
s_l_fb_inner_6_fb=fb((s_l_fb_inner_6_fb_x,s_l_fb_inner_6_fb_y),smalle_c_fb_template_width,smalle_c_fb_template_hight,boxstyle="round,pad=0,rounding_size=1",linestyle='-',facecolor="white",linewidth=0.3)
ax.add_patch(s_l_fb_inner_6_fb)
s_l_fb_inner_2_fb_x=s_l_fb_inner_1_fb_x+smalle_c_fb_template_width+s_r_fb_inner_horizantal_fb_gap
s_l_fb_inner_2_fb_y=small_left_fb_y+small_left_fb_hight-small_mid_boxes_vertical_padding-smalle_c_fb_template_hight
s_l_fb_inner_2_fb=fb((s_l_fb_inner_2_fb_x,s_l_fb_inner_2_fb_y),smalle_c_fb_template_width,smalle_c_fb_template_hight,boxstyle="round,pad=0,rounding_size=1",linestyle='-',facecolor="white",linewidth=0.3)
ax.add_patch(s_l_fb_inner_2_fb)
s_l_fb_inner_3_fb_x=s_l_fb_inner_1_fb_x+smalle_c_fb_template_width+s_r_fb_inner_horizantal_fb_gap
s_l_fb_inner_3_fb_y=small_left_fb_y+small_mid_boxes_vertical_padding
s_l_fb_inner_3_fb=fb((s_l_fb_inner_3_fb_x,s_l_fb_inner_3_fb_y),smalle_c_fb_template_width,smalle_c_fb_template_hight,boxstyle="round,pad=0,rounding_size=1",linestyle='-',facecolor="white",linewidth=0.3)
ax.add_patch(s_l_fb_inner_3_fb)
s_l_fb_inner_4_fb_x=s_l_fb_inner_2_fb_x+smalle_c_fb_template_width+s_r_fb_inner_horizantal_fb_gap
s_l_fb_inner_4_fb_y=small_left_fb_y+small_left_fb_hight-small_mid_boxes_vertical_padding-smalle_c_fb_template_hight
s_l_fb_inner_4_fb=fb((s_l_fb_inner_4_fb_x,s_l_fb_inner_4_fb_y),smalle_c_fb_template_width,smalle_c_fb_template_hight,boxstyle="round,pad=0,rounding_size=1",linestyle='-',facecolor="white",linewidth=0.3)
ax.add_patch(s_l_fb_inner_4_fb)
s_l_fb_inner_5_fb_x=s_l_fb_inner_2_fb_x+smalle_c_fb_template_width+s_r_fb_inner_horizantal_fb_gap
s_l_fb_inner_5_fb_y=small_left_fb_y+small_mid_boxes_vertical_padding
s_l_fb_inner_5_fb=fb((s_l_fb_inner_5_fb_x,s_l_fb_inner_5_fb_y),smalle_c_fb_template_width,smalle_c_fb_template_hight,boxstyle="round,pad=0,rounding_size=1",linestyle='-',facecolor="white",linewidth=0.3)
ax.add_patch(s_l_fb_inner_5_fb)
##now arrows -->
##left_one-->
s_l_fb_inner_1_ar=Ar(s_l_fb_inner_1_fb_x+smalle_c_fb_template_width,s_l_fb_inner_1_fb_y+smalle_c_fb_template_hight/2,s_l_fb_inner_2_fb_x-s_l_fb_inner_1_fb_x-smalle_c_fb_template_width,s_l_fb_inner_2_fb_y-s_l_fb_inner_1_fb_y, width=30,facecolor="black")
ax.add_patch(s_l_fb_inner_1_ar)
s_l_fb_inner_2_ar=Ar(s_l_fb_inner_1_fb_x+smalle_c_fb_template_width,s_l_fb_inner_1_fb_y+smalle_c_fb_template_hight/2,s_l_fb_inner_2_fb_x-s_l_fb_inner_1_fb_x-smalle_c_fb_template_width,s_l_fb_inner_3_fb_y-s_l_fb_inner_1_fb_y, width=30,facecolor="black")
ax.add_patch(s_l_fb_inner_2_ar)
s_l_fb_inner_3_ar=Ar(s_l_fb_inner_2_fb_x+smalle_c_fb_template_width,s_l_fb_inner_2_fb_y+smalle_c_fb_template_hight/2,s_l_fb_inner_2_fb_x-s_l_fb_inner_1_fb_x-smalle_c_fb_template_width,0, width=30,facecolor="black")
ax.add_patch(s_l_fb_inner_3_ar)
s_l_fb_inner_4_ar=Ar(s_l_fb_inner_2_fb_x+smalle_c_fb_template_width,s_l_fb_inner_3_fb_y+smalle_c_fb_template_hight/2,s_l_fb_inner_2_fb_x-s_l_fb_inner_1_fb_x-smalle_c_fb_template_width,0, width=30,facecolor="black")
ax.add_patch(s_l_fb_inner_4_ar)
s_l_fb_inner_5_ar=Ar(s_l_fb_inner_5_fb_x+smalle_c_fb_template_width,s_l_fb_inner_4_fb_y+smalle_c_fb_template_hight/2,s_l_fb_inner_6_fb_x-s_l_fb_inner_5_fb_x-smalle_c_fb_template_width,s_l_fb_inner_5_fb_y-s_l_fb_inner_6_fb_y, width=30,facecolor="black")
ax.add_patch(s_l_fb_inner_5_ar)
s_l_fb_inner_6_ar=Ar(s_l_fb_inner_5_fb_x+smalle_c_fb_template_width,s_l_fb_inner_5_fb_y+smalle_c_fb_template_hight/2,s_l_fb_inner_6_fb_x-s_l_fb_inner_5_fb_x-smalle_c_fb_template_width,s_l_fb_inner_6_fb_y-s_l_fb_inner_5_fb_y, width=30,facecolor="black")
ax.add_patch(s_l_fb_inner_6_ar)
##mid_one-->
s_m_fb_inner_1_ar=Ar(s_m_fb_inner_3_fb_x+smalle_c_fb_template_width,s_l_fb_inner_1_fb_y+smalle_c_fb_template_hight/2,s_m_fb_inner_1_fb_x-s_m_fb_inner_3_fb_x-smalle_c_fb_template_width,s_l_fb_inner_2_fb_y-s_l_fb_inner_1_fb_y, width=30,facecolor="black")
ax.add_patch(s_m_fb_inner_1_ar)
s_m_fb_inner_2_ar=Ar(s_m_fb_inner_3_fb_x+smalle_c_fb_template_width,s_l_fb_inner_1_fb_y+smalle_c_fb_template_hight/2,s_m_fb_inner_1_fb_x-s_m_fb_inner_3_fb_x-smalle_c_fb_template_width,-(s_l_fb_inner_2_fb_y-s_l_fb_inner_1_fb_y), width=30,facecolor="black")
ax.add_patch(s_m_fb_inner_2_ar)
s_m_fb_inner_3_ar=Ar(s_m_fb_inner_1_fb_x+smalle_c_fb_template_width,s_m_fb_inner_1_fb_y+smalle_c_fb_template_hight/2,s_m_fb_inner_1_fb_x-s_m_fb_inner_3_fb_x-smalle_c_fb_template_width,s_l_fb_inner_2_fb_y-s_l_fb_inner_1_fb_y, width=30,facecolor="black")
ax.add_patch(s_m_fb_inner_3_ar)
s_m_fb_inner_4_ar=Ar(s_m_fb_inner_1_fb_x+smalle_c_fb_template_width,s_m_fb_inner_2_fb_y+smalle_c_fb_template_hight/2,s_m_fb_inner_1_fb_x-s_m_fb_inner_3_fb_x-smalle_c_fb_template_width,-(s_l_fb_inner_2_fb_y-s_l_fb_inner_1_fb_y), width=30,facecolor="black")
ax.add_patch(s_m_fb_inner_4_ar)
##right one-->
s_r_fb_inner_1_ar=Ar(s_r_fb_inner_1_fb_x+smalle_c_fb_template_width,s_l_fb_inner_1_fb_y+smalle_c_fb_template_hight/2,s_r_fb_inner_horizantal_fb_gap,0, width=30,facecolor="black")
ax.add_patch(s_r_fb_inner_1_ar)
s_r_fb_inner_2_ar=Ar(s_r_fb_inner_2_fb_x+smalle_c_fb_template_width,s_l_fb_inner_1_fb_y+smalle_c_fb_template_hight/2,s_r_fb_inner_horizantal_fb_gap,0, width=30,facecolor="black")
ax.add_patch(s_r_fb_inner_2_ar)
s_r_fb_inner_3_ar=Ar(s_r_fb_inner_3_fb_x+smalle_c_fb_template_width,s_l_fb_inner_1_fb_y+smalle_c_fb_template_hight/2,s_r_fb_inner_horizantal_fb_gap,0, width=30,facecolor="black")
ax.add_patch(s_r_fb_inner_3_ar)
### now circles
circle_vertical_margin=10
circle_radius=(smalle_c_fb_template_hight-4*circle_vertical_margin)/3
##left
##1
cr_l_1_down_x=s_l_fb_inner_1_fb_x+smalle_c_fb_template_width/2
cr_l_1_down_y=s_l_fb_inner_1_fb_y+circle_vertical_margin+circle_radius/2
cr_l_1_down=cr((cr_l_1_down_x,cr_l_1_down_y),circle_radius,facecolor='r')
ax.add_patch(cr_l_1_down)
cr_l_1_up_x=s_l_fb_inner_1_fb_x+smalle_c_fb_template_width/2
cr_l_1_up_y=s_l_fb_inner_1_fb_y+smalle_c_fb_template_hight-circle_vertical_margin-circle_radius/2
cr_l_1_up=cr((cr_l_1_up_x,cr_l_1_up_y),circle_radius,facecolor='r')
ax.add_patch(cr_l_1_up)
##2
cr_l_2_down_x=s_l_fb_inner_2_fb_x+smalle_c_fb_template_width/2
cr_l_2_down_y=s_l_fb_inner_2_fb_y+circle_vertical_margin/1.5+circle_radius/2
cr_l_2_down=cr((cr_l_2_down_x,cr_l_2_down_y),circle_radius,facecolor='y')
ax.add_patch(cr_l_2_down)
cr_l_2_up_x=s_l_fb_inner_2_fb_x+smalle_c_fb_template_width/2
cr_l_2_up_y=s_l_fb_inner_2_fb_y+smalle_c_fb_template_hight-circle_vertical_margin/1.5-circle_radius/2
cr_l_2_up=cr((cr_l_2_up_x,cr_l_2_up_y),circle_radius,facecolor='y')
ax.add_patch(cr_l_2_up)
cr_l_2_mid_x=s_l_fb_inner_2_fb_x+smalle_c_fb_template_width/2
cr_l_2_mid_y=cr_l_2_down_y+(cr_l_2_up_y-cr_l_2_down_y)/2
cr_l_2_mid=cr((cr_l_2_mid_x,cr_l_2_mid_y),circle_radius,facecolor='y')
ax.add_patch(cr_l_2_mid)
##3
cr_l_3_down_x=s_l_fb_inner_3_fb_x+smalle_c_fb_template_width/2
cr_l_3_down_y=s_l_fb_inner_3_fb_y+circle_vertical_margin/1.5+circle_radius/2
cr_l_3_down=cr((cr_l_3_down_x,cr_l_3_down_y),circle_radius,facecolor='b')
ax.add_patch(cr_l_3_down)
cr_l_3_up_x=s_l_fb_inner_3_fb_x+smalle_c_fb_template_width/2
cr_l_3_up_y=s_l_fb_inner_3_fb_y+smalle_c_fb_template_hight-circle_vertical_margin/1.5-circle_radius/2
cr_l_3_up=cr((cr_l_3_up_x,cr_l_3_up_y),circle_radius,facecolor='b')
ax.add_patch(cr_l_3_up)
cr_l_3_mid_x=s_l_fb_inner_3_fb_x+smalle_c_fb_template_width/2
cr_l_3_mid_y=cr_l_3_down_y+(cr_l_2_up_y-cr_l_2_down_y)/2
cr_l_3_mid=cr((cr_l_3_mid_x,cr_l_3_mid_y),circle_radius,facecolor='b')
ax.add_patch(cr_l_3_mid)
##4
cr_l_4_down_x=s_l_fb_inner_4_fb_x+smalle_c_fb_template_width/2
cr_l_4_down_y=s_l_fb_inner_4_fb_y+circle_vertical_margin+circle_radius/2
cr_l_4_down=cr((cr_l_4_down_x,cr_l_4_down_y),circle_radius,facecolor='g')
ax.add_patch(cr_l_4_down)
cr_l_4_up_x=s_l_fb_inner_4_fb_x+smalle_c_fb_template_width/2
cr_l_4_up_y=s_l_fb_inner_4_fb_y+smalle_c_fb_template_hight-circle_vertical_margin-circle_radius/2
cr_l_4_up=cr((cr_l_4_up_x,cr_l_4_up_y),circle_radius,facecolor='g')
ax.add_patch(cr_l_4_up)
##5
cr_l_5_down_x=s_l_fb_inner_5_fb_x+smalle_c_fb_template_width/2
cr_l_5_down_y=s_l_fb_inner_5_fb_y+circle_vertical_margin/1.5+circle_radius/2
cr_l_5_down=cr((cr_l_5_down_x,cr_l_5_down_y),circle_radius,facecolor='orange')
ax.add_patch(cr_l_5_down)
cr_l_5_up_x=s_l_fb_inner_5_fb_x+smalle_c_fb_template_width/2
cr_l_5_up_y=s_l_fb_inner_5_fb_y+smalle_c_fb_template_hight-circle_vertical_margin/1.5-circle_radius/2
cr_l_5_up=cr((cr_l_5_up_x,cr_l_5_up_y),circle_radius,facecolor='orange')
ax.add_patch(cr_l_5_up)
cr_l_5_mid_x=s_l_fb_inner_5_fb_x+smalle_c_fb_template_width/2
cr_l_5_mid_y=cr_l_5_down_y+(cr_l_2_up_y-cr_l_2_down_y)/2
cr_l_5_mid=cr((cr_l_5_mid_x,cr_l_5_mid_y),circle_radius,facecolor='orange')
ax.add_patch(cr_l_5_mid)
##6
cr_l_6_down_x=s_l_fb_inner_6_fb_x+smalle_c_fb_template_width/2
cr_l_6_down_y=s_l_fb_inner_6_fb_y+circle_vertical_margin/1.5+circle_radius/2
cr_l_6_down=cr((cr_l_6_down_x,cr_l_6_down_y),circle_radius,facecolor='purple')
ax.add_patch(cr_l_6_down)
cr_l_6_up_x=s_l_fb_inner_6_fb_x+smalle_c_fb_template_width/2
cr_l_6_up_y=s_l_fb_inner_6_fb_y+smalle_c_fb_template_hight-circle_vertical_margin/1.5-circle_radius/2
cr_l_6_up=cr((cr_l_6_up_x,cr_l_6_up_y),circle_radius,facecolor='purple')
ax.add_patch(cr_l_6_up)
cr_l_6_mid_x=s_l_fb_inner_6_fb_x+smalle_c_fb_template_width/2
cr_l_6_mid_y=cr_l_6_down_y+(cr_l_2_up_y-cr_l_2_down_y)/2
cr_l_6_mid=cr((cr_l_6_mid_x,cr_l_6_mid_y),circle_radius,facecolor='purple')
ax.add_patch(cr_l_6_mid)
##mid
##1
cr_m_1_down_x=s_m_fb_inner_1_fb_x+smalle_c_fb_template_width/2
cr_m_1_down_y=s_m_fb_inner_1_fb_y+circle_vertical_margin/1.5+circle_radius/2
cr_m_1_down=cr((cr_m_1_down_x,cr_m_1_down_y),circle_radius,facecolor='b')
ax.add_patch(cr_m_1_down)
cr_m_1_up_x=s_m_fb_inner_1_fb_x+smalle_c_fb_template_width/2
cr_m_1_up_y=s_m_fb_inner_1_fb_y+smalle_c_fb_template_hight-circle_vertical_margin/1.5-circle_radius/2
cr_m_1_up=cr((cr_m_1_up_x,cr_m_1_up_y),circle_radius,facecolor='b')
ax.add_patch(cr_m_1_up)
cr_m_1_mid_x=s_m_fb_inner_1_fb_x+smalle_c_fb_template_width/2
cr_m_1_mid_y=cr_m_1_down_y+(cr_l_2_up_y-cr_l_2_down_y)/2
cr_m_1_mid=cr((cr_m_1_mid_x,cr_m_1_mid_y),circle_radius,facecolor='b')
ax.add_patch(cr_m_1_mid)
##2
cr_m_2_down_x=s_m_fb_inner_2_fb_x+smalle_c_fb_template_width/2
cr_m_2_down_y=s_m_fb_inner_2_fb_y+circle_vertical_margin/1.5+circle_radius/2
cr_m_2_down=cr((cr_m_2_down_x,cr_m_2_down_y),circle_radius,facecolor='y')
ax.add_patch(cr_m_2_down)
cr_m_2_up_x=s_m_fb_inner_2_fb_x+smalle_c_fb_template_width/2
cr_m_2_up_y=s_m_fb_inner_2_fb_y+smalle_c_fb_template_hight-circle_vertical_margin/1.5-circle_radius/2
cr_m_2_up=cr((cr_m_2_up_x,cr_m_2_up_y),circle_radius,facecolor='y')
ax.add_patch(cr_m_2_up)
cr_m_2_mid_x=s_m_fb_inner_2_fb_x+smalle_c_fb_template_width/2
cr_m_2_mid_y=cr_m_2_down_y+(cr_m_2_up_y-cr_l_2_down_y)/2
cr_m_2_mid=cr((cr_m_2_mid_x,cr_m_2_mid_y),circle_radius,facecolor='y')
ax.add_patch(cr_m_2_mid)
##3
cr_m_3_down_x=s_m_fb_inner_3_fb_x+smalle_c_fb_template_width/2
cr_m_3_down_y=s_m_fb_inner_3_fb_y+circle_vertical_margin+circle_radius/2
cr_m_3_down=cr((cr_m_3_down_x,cr_m_3_down_y),circle_radius,facecolor='r')
ax.add_patch(cr_m_3_down)
cr_m_3_up_x=s_m_fb_inner_3_fb_x+smalle_c_fb_template_width/2
cr_m_3_up_y=s_m_fb_inner_3_fb_y+smalle_c_fb_template_hight-circle_vertical_margin-circle_radius/2
cr_m_3_up=cr((cr_m_3_up_x,cr_m_3_up_y),circle_radius,facecolor='r')
ax.add_patch(cr_m_3_up)
##4
cr_m_4_down_x=s_m_fb_inner_4_fb_x+smalle_c_fb_template_width/2
cr_m_4_down_y=s_m_fb_inner_4_fb_y+circle_vertical_margin/1.5+circle_radius/2
cr_m_4_down=cr((cr_m_4_down_x,cr_m_4_down_y),circle_radius,facecolor='purple')
ax.add_patch(cr_m_4_down)
cr_m_4_up_x=s_m_fb_inner_4_fb_x+smalle_c_fb_template_width/2
cr_m_4_up_y=s_m_fb_inner_4_fb_y+smalle_c_fb_template_hight-circle_vertical_margin/1.5-circle_radius/2
cr_m_4_up=cr((cr_m_4_up_x,cr_m_4_up_y),circle_radius,facecolor='purple')
ax.add_patch(cr_m_4_up)
cr_m_4_mid_x=s_m_fb_inner_4_fb_x+smalle_c_fb_template_width/2
cr_m_4_mid_y=cr_m_4_down_y+(cr_l_2_up_y-cr_l_2_down_y)/2
cr_m_4_mid=cr((cr_m_4_mid_x,cr_m_4_mid_y),circle_radius,facecolor='purple')
ax.add_patch(cr_m_4_mid)
#right
##1
cr_r_1_down_x=s_r_fb_inner_1_fb_x+smalle_c_fb_template_width/2
cr_r_1_down_y=s_r_fb_inner_1_fb_y+circle_vertical_margin+circle_radius/2
cr_r_1_down=cr((cr_r_1_down_x,cr_r_1_down_y),circle_radius,facecolor='r')
ax.add_patch(cr_r_1_down)
cr_r_1_up_x=s_r_fb_inner_1_fb_x+smalle_c_fb_template_width/2
cr_r_1_up_y=s_r_fb_inner_1_fb_y+smalle_c_fb_template_hight-circle_vertical_margin-circle_radius/2
cr_r_1_up=cr((cr_r_1_up_x,cr_r_1_up_y),circle_radius,facecolor='r')
ax.add_patch(cr_r_1_up)
##2
cr_r_2_down_x=s_r_fb_inner_2_fb_x+smalle_c_fb_template_width/2
cr_r_2_down_y=s_r_fb_inner_2_fb_y+circle_vertical_margin/1.5+circle_radius/2
cr_r_2_down=cr((cr_r_2_down_x,cr_r_2_down_y),circle_radius,facecolor='y')
ax.add_patch(cr_r_2_down)
cr_r_2_up_x=s_r_fb_inner_2_fb_x+smalle_c_fb_template_width/2
cr_r_2_up_y=s_r_fb_inner_2_fb_y+smalle_c_fb_template_hight-circle_vertical_margin/1.5-circle_radius/2
cr_r_2_up=cr((cr_r_2_up_x,cr_r_2_up_y),circle_radius,facecolor='y')
ax.add_patch(cr_r_2_up)
cr_r_2_mid_x=s_r_fb_inner_2_fb_x+smalle_c_fb_template_width/2
cr_r_2_mid_y=cr_r_2_down_y+(cr_l_2_up_y-cr_l_2_down_y)/2
cr_r_2_mid=cr((cr_r_2_mid_x,cr_r_2_mid_y),circle_radius,facecolor='y')
ax.add_patch(cr_r_2_mid)
##3
cr_r_3_down_x=s_r_fb_inner_3_fb_x+smalle_c_fb_template_width/2
cr_r_3_down_y=s_r_fb_inner_3_fb_y+circle_vertical_margin/1.5+circle_radius/2
cr_r_3_down=cr((cr_r_3_down_x,cr_r_3_down_y),circle_radius,facecolor='b')
ax.add_patch(cr_r_3_down)
cr_r_3_up_x=s_r_fb_inner_3_fb_x+smalle_c_fb_template_width/2
cr_r_3_up_y=s_r_fb_inner_3_fb_y+smalle_c_fb_template_hight-circle_vertical_margin/1.5-circle_radius/2
cr_r_3_up=cr((cr_r_3_up_x,cr_r_3_up_y),circle_radius,facecolor='b')
ax.add_patch(cr_r_3_up)
cr_r_3_mid_x=s_r_fb_inner_3_fb_x+smalle_c_fb_template_width/2
cr_r_3_mid_y=cr_r_3_down_y+(cr_l_2_up_y-cr_l_2_down_y)/2
cr_r_3_mid=cr((cr_r_3_mid_x,cr_r_3_mid_y),circle_radius,facecolor='b')
ax.add_patch(cr_r_3_mid)
##4
cr_r_4_down_x=s_r_fb_inner_4_fb_x+smalle_c_fb_template_width/2
cr_r_4_down_y=s_r_fb_inner_4_fb_y+circle_vertical_margin/1.5+circle_radius/2
cr_r_4_down=cr((cr_r_4_down_x,cr_r_4_down_y),circle_radius,facecolor='purple')
ax.add_patch(cr_r_4_down)
cr_r_4_up_x=s_r_fb_inner_4_fb_x+smalle_c_fb_template_width/2
cr_r_4_up_y=s_r_fb_inner_4_fb_y+smalle_c_fb_template_hight-circle_vertical_margin/1.5-circle_radius/2
cr_r_4_up=cr((cr_r_4_up_x,cr_r_4_up_y),circle_radius,facecolor='purple')
ax.add_patch(cr_r_4_up)
cr_r_4_mid_x=s_r_fb_inner_4_fb_x+smalle_c_fb_template_width/2
cr_r_4_mid_y=cr_r_4_down_y+(cr_l_2_up_y-cr_l_2_down_y)/2
cr_r_4_mid=cr((cr_r_4_mid_x,cr_r_4_mid_y),circle_radius,facecolor='purple')
ax.add_patch(cr_r_4_mid)
###two big normal boxes in left down
down_left_inner_fb_inner_vertical_text_gap=30
down_left_inner_fb_inner_padding=20
down_left_inner_fb_inner_vertical_gap=30
big_plt_box_hight=(left_down_inner_fb_hight-down_left_inner_fb_inner_padding*2-down_left_inner_fb_inner_vertical_gap-down_left_inner_fb_inner_vertical_text_gap)/2
big_plt_box_width=left_down_inner_fb_width-2*down_left_inner_fb_inner_padding
##box1
big_box_down_x=left_down_inner_fb_x+down_left_inner_fb_inner_padding
big_box_down_y=left_down_inner_fb_y+down_left_inner_fb_inner_padding
box1=fb((big_box_down_x,big_box_down_y),big_plt_box_width,big_plt_box_hight,boxstyle="round,pad=0,rounding_size=1",linestyle='-',facecolor="white",linewidth=0.3)
ax.add_patch(box1)
##box2
big_box_up_x=left_down_inner_fb_x+down_left_inner_fb_inner_padding
big_box_up_y=left_down_inner_fb_y+left_down_inner_fb_hight-down_left_inner_fb_inner_padding-big_plt_box_hight-down_left_inner_fb_inner_vertical_text_gap
box2=fb((big_box_up_x,big_box_up_y),big_plt_box_width,big_plt_box_hight,boxstyle="round,pad=0,rounding_size=1",linestyle='-',facecolor="white",linewidth=0.3)
ax.add_patch(box2)
#now middle arrow
down_inner_arrow_x=big_box_up_x+big_plt_box_width/2
down_inner_arrow_y=big_box_up_y
down_inner_arrow=Ar(down_inner_arrow_x,down_inner_arrow_y,0,-down_left_inner_fb_inner_vertical_gap, width=50,facecolor="black")
ax.add_patch(down_inner_arrow)
#now arrow axis -->
bix_box_horizantal_padding=20
ax_arrow_start_x=big_box_down_x+bix_box_horizantal_padding
ax_arrow_start_y=big_box_down_y+down_left_inner_fb_inner_vertical_gap
ax_arrow_start_vertical=Ar_f((ax_arrow_start_x, ax_arrow_start_y), (ax_arrow_start_x+big_plt_box_width-bix_box_horizantal_padding, ax_arrow_start_y), arrowstyle='->', mutation_scale=5)
ax.add_patch(ax_arrow_start_vertical)
ax_arrow_start_horizantal=Ar_f((ax_arrow_start_x, ax_arrow_start_y), (ax_arrow_start_x, ax_arrow_start_y+big_plt_box_hight-down_left_inner_fb_inner_vertical_gap), arrowstyle='->', mutation_scale=5)
ax.add_patch(ax_arrow_start_horizantal)
#lowwer big box
plt_box_hight=(big_plt_box_hight-down_left_inner_fb_inner_vertical_gap)/20
ax_boxes_parent_padding=10
#red boxes
red_box_width=plt_box_hight*4
red_b_x=ax_arrow_start_x+ax_boxes_parent_padding
red_b_1_y=ax_arrow_start_y+14*plt_box_hight
red_b_1=fb((red_b_x,red_b_1_y),red_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="r",linewidth=0.3)
ax.add_patch(red_b_1)
red_b_2_y=ax_arrow_start_y+15*plt_box_hight
red_b_2=fb((red_b_x,red_b_2_y),red_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="r",linewidth=0.3)
ax.add_patch(red_b_2)
red_b_3_y=ax_arrow_start_y+16*plt_box_hight
red_b_3=fb((red_b_x,red_b_3_y),red_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="r",linewidth=0.3)
ax.add_patch(red_b_3)
#yellow boxes
yellow_box_width=plt_box_hight*14
yellow_b_x=red_b_x+red_box_width
yellow_b_1_y=ax_arrow_start_y+11*plt_box_hight
yellow_b_1=fb((yellow_b_x,yellow_b_1_y),yellow_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="y",linewidth=0.3)
ax.add_patch(yellow_b_1)
yellow_b_2_y=ax_arrow_start_y+12*plt_box_hight
yellow_b_2=fb((yellow_b_x,yellow_b_2_y),yellow_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="y",linewidth=0.3)
ax.add_patch(yellow_b_2)
yellow_b_3_y=ax_arrow_start_y+13*plt_box_hight
yellow_b_3=fb((yellow_b_x,yellow_b_3_y),yellow_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="y",linewidth=0.3)
ax.add_patch(yellow_b_3)
#blue boxes
blue_box_width=plt_box_hight*10
blue_b_x=yellow_b_x
blue_b_1_y=ax_arrow_start_y+8*plt_box_hight
blue_b_1=fb((blue_b_x,blue_b_1_y),blue_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="b",linewidth=0.3)
ax.add_patch(blue_b_1)
blue_b_2_y=ax_arrow_start_y+9*plt_box_hight
blue_b_2=fb((blue_b_x,blue_b_2_y),blue_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="b",linewidth=0.3)
ax.add_patch(blue_b_2)
blue_b_3_y=ax_arrow_start_y+10*plt_box_hight
blue_b_3=fb((blue_b_x,blue_b_3_y),blue_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="b",linewidth=0.3)
ax.add_patch(blue_b_3)
#green boxes
green_box_width=plt_box_hight*16
green_b_x=yellow_b_x+yellow_box_width
green_b_1_y=ax_arrow_start_y+7*plt_box_hight
green_b_1=fb((green_b_x,green_b_1_y),green_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="g",linewidth=0.3)
ax.add_patch(green_b_1)
green_b_2_y=ax_arrow_start_y+6*plt_box_hight
green_b_2=fb((green_b_x,green_b_2_y),green_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="g",linewidth=0.3)
ax.add_patch(green_b_2)
#orange boxes
orange_box_width=plt_box_hight*20
orange_b_x=yellow_b_x+yellow_box_width
orange_b_1_y=ax_arrow_start_y+5*plt_box_hight
orange_b_1=fb((orange_b_x,orange_b_1_y),orange_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="orange",linewidth=0.3)
ax.add_patch(orange_b_1)
orange_b_2_y=ax_arrow_start_y+4*plt_box_hight
orange_b_2=fb((orange_b_x,orange_b_2_y),orange_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="orange",linewidth=0.3)
ax.add_patch(orange_b_2)
orange_b_3_y=ax_arrow_start_y+3*plt_box_hight
orange_b_3=fb((orange_b_x,orange_b_3_y),orange_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="orange",linewidth=0.3)
ax.add_patch(orange_b_3)
#purple boxes
purple_box_width=plt_box_hight*8
purple_b_x=orange_b_x+orange_box_width
purple_b_1_y=ax_arrow_start_y+2*plt_box_hight
purple_b_1=fb((purple_b_x,purple_b_1_y),purple_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="purple",linewidth=0.3)
ax.add_patch(purple_b_1)
purple_b_2_y=ax_arrow_start_y+plt_box_hight
purple_b_2=fb((purple_b_x,purple_b_2_y),purple_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="purple",linewidth=0.3)
ax.add_patch(purple_b_2)
purple_b_3_y=ax_arrow_start_y
purple_b_3=fb((purple_b_x,purple_b_3_y),purple_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="purple",linewidth=0.3)
ax.add_patch(purple_b_3)
#upper big box
upper_big_box_offset=big_plt_box_hight+down_left_inner_fb_inner_vertical_gap
ax_boxes_parent_padding=10
#red boxes
red_box_width=plt_box_hight*4
red_b_x=ax_arrow_start_x+ax_boxes_parent_padding
red_b_1_y=ax_arrow_start_y+14*plt_box_hight+upper_big_box_offset
red_b_1=fb((red_b_x,red_b_1_y),red_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="r",linewidth=0.3)
ax.add_patch(red_b_1)
red_b_2_y=ax_arrow_start_y+15*plt_box_hight+upper_big_box_offset
red_b_2=fb((red_b_x,red_b_2_y),red_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="r",linewidth=0.3)
ax.add_patch(red_b_2)
red_b_3_y=ax_arrow_start_y+16*plt_box_hight+upper_big_box_offset
red_b_3=fb((red_b_x,red_b_3_y),red_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="r",linewidth=0.3)
ax.add_patch(red_b_3)
#yellow boxes
yellow_box_width=plt_box_hight*14
yellow_b_x=red_b_x+red_box_width
yellow_b_1_y=ax_arrow_start_y+11*plt_box_hight+upper_big_box_offset
yellow_b_1=fb((yellow_b_x,yellow_b_1_y),yellow_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="y",linewidth=0.3)
ax.add_patch(yellow_b_1)
yellow_b_2_y=ax_arrow_start_y+12*plt_box_hight+upper_big_box_offset
yellow_b_2=fb((yellow_b_x,yellow_b_2_y),yellow_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="y",linewidth=0.3)
ax.add_patch(yellow_b_2)
yellow_b_3_y=ax_arrow_start_y+13*plt_box_hight+upper_big_box_offset
yellow_b_3=fb((yellow_b_x,yellow_b_3_y),yellow_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="y",linewidth=0.3)
ax.add_patch(yellow_b_3)
#blue boxes
blue_box_width=plt_box_hight*10
blue_b_x=yellow_b_x
blue_b_1_y=ax_arrow_start_y+8*plt_box_hight+upper_big_box_offset
blue_b_1=fb((blue_b_x,blue_b_1_y),blue_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="b",linewidth=0.3)
ax.add_patch(blue_b_1)
blue_b_2_y=ax_arrow_start_y+9*plt_box_hight+upper_big_box_offset
blue_b_2=fb((blue_b_x,blue_b_2_y),blue_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="b",linewidth=0.3)
ax.add_patch(blue_b_2)
blue_b_3_y=ax_arrow_start_y+10*plt_box_hight+upper_big_box_offset
blue_b_3=fb((blue_b_x,blue_b_3_y),blue_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="b",linewidth=0.3)
ax.add_patch(blue_b_3)
#green boxes
green_box_width=plt_box_hight*16
green_b_x=yellow_b_x+yellow_box_width
green_b_1_y=ax_arrow_start_y+7*plt_box_hight+upper_big_box_offset
green_b_1=fb((green_b_x,green_b_1_y),green_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="g",linewidth=0.3)
ax.add_patch(green_b_1)
green_b_2_y=ax_arrow_start_y+6*plt_box_hight+upper_big_box_offset
green_b_2=fb((green_b_x,green_b_2_y),green_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="g",linewidth=0.3)
ax.add_patch(green_b_2)
#orange boxes
orange_box_width=plt_box_hight*20
orange_b_x=yellow_b_x+yellow_box_width
orange_b_1_y=ax_arrow_start_y+5*plt_box_hight+upper_big_box_offset
orange_b_1=fb((orange_b_x,orange_b_1_y),orange_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="orange",linewidth=0.3)
ax.add_patch(orange_b_1)
orange_b_2_y=ax_arrow_start_y+4*plt_box_hight+upper_big_box_offset
orange_b_2=fb((orange_b_x,orange_b_2_y),orange_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="orange",linewidth=0.3)
ax.add_patch(orange_b_2)
orange_b_3_y=ax_arrow_start_y+3*plt_box_hight+upper_big_box_offset
orange_b_3=fb((orange_b_x,orange_b_3_y),orange_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="orange",linewidth=0.3)
ax.add_patch(orange_b_3)
#purple boxes
purple_box_width=plt_box_hight*8
purple_b_x=orange_b_x+orange_box_width
purple_b_1_y=ax_arrow_start_y+2*plt_box_hight+upper_big_box_offset
purple_b_1=fb((purple_b_x,purple_b_1_y),purple_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="purple",linewidth=0.3)
ax.add_patch(purple_b_1)
purple_b_2_y=ax_arrow_start_y+1*plt_box_hight+upper_big_box_offset
purple_b_2=fb((purple_b_x,purple_b_2_y),purple_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="purple",linewidth=0.3)
ax.add_patch(purple_b_2)
purple_b_3_y=ax_arrow_start_y+upper_big_box_offset
purple_b_3=fb((purple_b_x,purple_b_3_y),purple_box_width,plt_box_hight,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="purple",linewidth=0.3)
ax.add_patch(purple_b_3)
##now lines
#orange line
orange_line_x=orange_b_x+orange_box_width
orange_line_y=orange_b_2_y+plt_box_hight/2
purple_line_width=big_box_down_x+big_plt_box_width-orange_line_x
orange_line=fb((orange_line_x,orange_line_y),purple_line_width,0,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="black",linewidth=0.3)
ax.add_patch(orange_line)
#purple line
purple_line_x=purple_b_x+purple_box_width
purple_line_y=purple_b_2_y+plt_box_hight/2
purple_line_width=big_box_down_x+big_plt_box_width-purple_line_x
purple_line=fb((purple_line_x,purple_line_y),purple_line_width,0,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="black",linewidth=0.3)
ax.add_patch(purple_line)
#green line
green_line_x=green_b_x+green_box_width
green_line_y=green_b_1_y
green_line_width=big_box_down_x+big_plt_box_width-green_line_x
green_line=fb((green_line_x,green_line_y),green_line_width,0,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="black",linewidth=0.3)
ax.add_patch(green_line)
#blue line
blue_line_x=blue_b_x+blue_box_width
blue_line_y=blue_b_2_y+plt_box_hight/2
blue_line_width=big_box_down_x+big_plt_box_width-blue_line_x
blue_line=fb((blue_line_x,blue_line_y),blue_line_width,0,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="black",linewidth=0.3)
ax.add_patch(blue_line)
#yellow line
yellow_line_x=yellow_b_x+yellow_box_width
yellow_line_y=yellow_b_2_y+plt_box_hight/2
yellow_line_width=big_box_down_x+big_plt_box_width-yellow_line_x
yellow_line=fb((yellow_line_x,yellow_line_y),yellow_line_width,0,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="black",linewidth=0.3)
ax.add_patch(yellow_line)
#red line
red_line_x=red_b_x+red_box_width
red_line_y=red_b_2_y+plt_box_hight/2
red_line_width=big_box_down_x+big_plt_box_width-red_line_x
red_line=fb((red_line_x,red_line_y),red_line_width,0,boxstyle="round,pad=0,rounding_size=0",linestyle='-',facecolor="black",linewidth=0.3)
###-->
down_mid_Arrow_lower_y=left_down_inner_fb_right_inner_lower_fb_y+left_down_inner_fb_right_inner_upper_fb_hight/2
down_mid_Arrow_lower=Ar(big_box_down_x+big_plt_box_width,down_mid_Arrow_lower_y,-(big_box_down_x+big_plt_box_width-left_down_inner_fb_right_x),0, width=50,facecolor="black")
ax.add_patch(down_mid_Arrow_lower)
#now path patches
Path = mpath.Path
path_data = [
    (Path.MOVETO, (extent_r_4[0]-ducker_image_horizantal_gap,extent_r_4[2])),
    (Path.CURVE4, (extent_r_4[0]+whale_icon_size/2,extent_r_4[2]-whale_icon_size)),
    (Path.CURVE4, (extent_r_4[1],extent_r_4[2]+whale_icon_size/2)),
    (Path.CURVE4, (extent_r_5_2[1]+ducker_image_horizantal_gap/2,extent_r_5_2[2]+ducker_image_vertical_gap/2)),
    (Path.CURVE4, (extent_r_6_2[1]+whale_icon_size/1.5,extent_r_6_2[2]+whale_icon_size)),
    (Path.CURVE4, (extent_r_6_2[1]-ducker_image_horizantal_gap,extent_r_6_2[2]+whale_icon_size)),    
    (Path.CURVE3, (extent_r_6_2[0]-ducker_image_horizantal_gap+10,extent_r_6_2[2]+whale_icon_size/2)),
    (Path.CURVE3, (extent_r_5_2[0]+ducker_image_horizantal_gap+10,extent_r_5_2[2]-whale_icon_size/3)),    
    (Path.CURVE3, (extent_r_4[0],extent_r_5[2]-whale_icon_size/2.5)),  
          
    (Path.CLOSEPOLY,  (extent_r_4[0]-ducker_image_horizantal_gap,extent_r_4[2])),
    ]
codes, verts = zip(*path_data)
path = mpath.Path(verts, codes)
patch = mpatches.PathPatch(path, facecolor="none",linestyle='--',zorder=3)
ax.add_patch(patch)
path_data = [
    (Path.MOVETO, (extent_r_4_2[0]-ducker_image_horizantal_gap,extent_r_4[2])),
    (Path.CURVE4, (extent_r_4_2[0]+whale_icon_size/2,extent_r_4[2]-whale_icon_size)),
    (Path.CURVE4, (extent_r_4_2[1]+ducker_image_horizantal_gap,extent_r_4[2]+whale_icon_size/2)),
    (Path.CURVE4, (extent_r_5_3[1]+ducker_image_horizantal_gap/2,extent_r_5_2[2]+ducker_image_vertical_gap/2)),
    (Path.CURVE4, (extent_r_6_3[1]+ducker_image_horizantal_gap,extent_r_6_2[2]+whale_icon_size/2)),
    (Path.CURVE4, (extent_r_6_3[1]+ducker_image_horizantal_gap,extent_r_6_2[2]+whale_icon_size)),
    
    (Path.CURVE4, (extent_r_6_3[0]-ducker_image_horizantal_gap+10,extent_r_6_2[2]+whale_icon_size/2)),
    (Path.CURVE3, (extent_r_5_3[0]+ducker_image_horizantal_gap+10,extent_r_5_3[2]-whale_icon_size/2)),    
    (Path.CURVE4, (extent_r_5_3[0]-whale_icon_size,extent_r_4_2[2]+whale_icon_size/2)),
    (Path.CLOSEPOLY,  (extent_r_4[0]-ducker_image_horizantal_gap,extent_r_4[2]+whale_icon_size/3)),
    ]
codes, verts = zip(*path_data)
path = mpath.Path(verts, codes)
patch = mpatches.PathPatch(path, facecolor="none",linestyle='--',zorder=3)
ax.add_patch(patch)    
ax.add_patch(red_line)
##-->

mid_to_upper_big_box_ar=Ar(small_left_fb_x+small_left_fb_width/2,small_left_fb_y,0,big_box_up_y+big_plt_box_hight-small_left_fb_y, width=35,facecolor="black")
ax.add_patch(mid_to_upper_big_box_ar)
##text
plt.text(red_line_x+40,red_line_y+10,"Order of Relationship of Task Istance",fontsize="xx-small")
plt.text(red_line_x+50,big_box_up_y+big_plt_box_hight+10,"Task scheduler",fontsize="xx-small")
plt.text(big_box_down_x+big_plt_box_width/2,big_box_down_y+big_plt_box_hight-25,"Task scheduling",ha="center",fontsize="xx-small")
plt.text(big_box_down_x+30,big_box_down_y+big_plt_box_hight-25,"containers",fontsize="xx-small")
plt.text(big_box_down_x+big_plt_box_width/1.1,ax_arrow_start_y-22,"Time",ha='right',fontsize="xx-small")
plt.text(right_inner_upper_fb_x+right_inner_upper_fb_width/1.8,(right_inner_lower_fb_y+right_inner_upper_fb_y+right_inner_lower_fb_hight)/2-15 ,"transion time"+'\n'+"in diffrent clouds",zorder=4,fontsize=4)
path_data = [
    (Path.MOVETO, (extent_r_4_2[1],extent_r_4_2[2]-ducker_image_vertical_gap)),
    (Path.LINETO, (right_inner_upper_fb_x+right_inner_upper_fb_width/1.8,(right_inner_lower_fb_y+right_inner_upper_fb_y+right_inner_lower_fb_hight)/2-15)),
    (Path.LINETO,(extent_r_3[1]+ducker_image_horizantal_gap,extent_r_3[2]+ducker_image_vertical_gap))
    ]
codes, verts = zip(*path_data)
path = mpath.Path(verts, codes)
patch = mpatches.PathPatch(path, facecolor="none",linestyle='-',zorder=3,linewidth=0.3)
ax.add_patch(patch)    
plt.text(extent_r_5_3[0]+ducker_image_horizantal_gap,(extent_r_6_3[2]+extent_r_5_3[2])/2 ,"transion time"+'\n'+"in same clouds",zorder=4,fontsize=4)
path_data = [
    (Path.MOVETO, (extent_r_5_3[0]-ducker_image_horizantal_gap,(extent_r_6_3[2]+extent_r_5_3[2])/2)),
    (Path.LINETO, (extent_r_5_3[0]+ducker_image_horizantal_gap,(extent_r_6_3[2]+extent_r_5_3[2])/2)),
    (Path.LINETO,(extent_r_5[0]+whale_icon_size-10,extent_r_5[2]+whale_icon_size/2))
    ]
codes, verts = zip(*path_data)
path = mpath.Path(verts, codes)
patch = mpatches.PathPatch(path, facecolor="none",linestyle='-',zorder=3,linewidth=0.3)
ax.add_patch(patch)    
plt.text(-70,-90,"Fig. 1.    Scheduling frameWork in cloud",zorder=4)
fig.savefig("fig 1")
plt.show()

