import os
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector
from get_xml import write_xml


#global variables
img = None

#coordinates of mouse click
#tl =  top left mouse click coordinate
#br = bottom right mouse c
tl_list = []
br_list = []

object_list = []

#Path of dataset folder that is to be annotated
image_folder = 'NFPA Dataset'
#Directory where you want to save the annotations
savedir = 'annotation_folder'
#Tag you want to give to the object detected
obj = 'NFPA'


def line_select_callback(clk, rls):
    global tl_list
    global br_list
    tl_list.append((int(clk.xdata), int(clk.ydata)))
    br_list.append((int(rls.xdata), int(rls.ydata)))
    object_list.append(obj)
    

def onkeypress(event):
    global tl_list
    global br_list
    global object_list
    global img

    if event.key == 'q':
        write_xml(image_folder, img, object_list, tl_list, br_list, savedir)
        tl_list = []
        br_list = []
        object_list = []
        img = None
        plt.close()


def toggle_selector(event):
    #sets the toggle selector active
    toggle_selector.RS.set_active(True)

if __name__ == '__main__':
    for n, image_file in enumerate(os.scandir(image_folder)):
        img = image_file
        fig, ax = plt.subplots(1)
        image = cv2.imread(image_file.path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ax.imshow(image)

        #button[1] = left mouse click
        toggle_selector.RS = RectangleSelector(ax, line_select_callback,
                                               drawtype='box', useblit=True,
                                               button=[1], minspanx=5, minspany=5,
                                               spancoords='pixels', interactive=True)

        bbox =  bbox = plt.connect('key_press_event', toggle_selector)
        key = plt.connect('key_press_event', onkeypress)
        plt.show()

        
        
        
        
