"""extraction of suitable objects at a time .....in left, right, and front direction""" 

left_box = (50,200,720,400) #(top,left,bottom,right)
front_box = (50,400,720,880)
right_box = (50,880,720,1080)


def iou_cal(box1, box2):
    """Implement the intersection over union (IoU) between box1 and box2
    
    Arguments:
    box1 -- first box, list object with coordinates (y1, x1, y2, x2)
    box2 -- second box, list object with coordinates (y1, x1, y2, x2)
    """
   
    yi1 = max(box1[0], box2[0])
    xi1 = max(box1[1], box2[1])
    yi2 = min(box1[2], box2[2])
    xi2 = min(box1[3], box2[3])
    inter_area = max(0,(xi2 - xi1))*max(0,(yi2 - yi1))
   
    box1_area = (box1[3] - box1[1])*(box1[2]- box1[0])
    box2_area = (box2[3] - box2[1])*(box2[2]- box2[0])
    union_area = (box1_area + box2_area) - inter_area
   
    iou = inter_area / union_area
    

    return iou

def extract_suitable_object_info(out_scores,out_boxes,out_classes,objects):
    
    lowest_left,lowest_right,lowest_front  = 0,0,0
    right_obj,left_obj ,front_obj= "",'',''
    
    for ind,box in enumerate(out_boxes):
        
#         centre_x = int((box[1]+box[3])/2)
        # centre_y = int((box[0]+box[2])/2)
        if box[2] >=500:
        
        
#             if (centre_x <=250 or box[3]<=400) and lowest_left < box[2]:
#                 lowest_left = box[2]
#                 left_obj = objects[out_classes[ind]][:-1]
                
#             elif (centre_x >=1000 or box[1] >= 800) and lowest_right < box[2]:
#                 lowest_right = box[2]
#                 right_obj = objects[out_classes[ind]][:-1]
                
#             elif lowest_front < box[2]:
#                 lowest_front = box[2]
#                 front_obj = objects[out_classes[ind]][:-1]
            iou_with_left = iou_cal(box,left_box)
            iou_with_right = iou_cal(box,right_box)
            iou_with_front = iou_cal(box,front_box)
            
            max_iou = max(iou_with_left,iou_with_right,iou_with_front)
            
            if(max_iou>0 and max_iou==iou_with_left and lowest_left < box[2]):
                lowest_left = box[2]
                left_obj = objects[out_classes[ind]][:-1]
            
            elif(max_iou>0 and max_iou==iou_with_right and lowest_right < box[2]):
                lowest_right = box[2]
                right_obj = objects[out_classes[ind]][:-1]
            
            elif(max_iou>0 and max_iou==iou_with_front and lowest_front < box[2]):
                lowest_front = box[2]
                front_obj = objects[out_classes[ind]][:-1]

    msg = ''
    if(len(front_obj)>0):
        msg = msg + 'front '+ front_obj+' '
    if(len(left_obj)>0):
        msg = msg + 'left '+ left_obj +' '
    if(len(right_obj)>0):
        msg = msg + 'right '+ right_obj
                
    return msg
                