"""extraction of suitable objects at a time .....in left, right, and front direction""" 

def extract_suitable_object_info(out_scores,out_boxes,out_classes,objects):
    
    lowest_left,lowest_right,lowest_front  = 0,0,0
    right_obj,left_obj ,front_obj= "",'',''
    
    for ind,box in enumerate(out_boxes):
        centre_x = int((box[1]+box[3])/2)
        centre_y = int((box[0]+box[2])/2)
        if centre_y >=450:
            
            if (centre_x <=250 or box[3]<=400) and lowest_left < box[2]:
                lowest_left = box[2]
                left_obj = objects[out_classes[ind]]
                
            elif (centre_x >=1000 or box[1] >= 800) and lowest_right < box[2]:
                lowest_right = box[2]
                right_obj = objects[out_classes[ind]]
                
            elif lowest_front < box[2]:
                lowest_front = box[2]
                front_obj = objects[out_classes[ind]]
    msg = ''
    if(len(front_obj)>0):
        msg = msg + 'front '+ front_obj+'\n'
    if(len(left_obj)>0):
        msg = msg + 'left '+ left_obj +'\n'
    if(len(right_obj)>0):
        msg = msg + 'right '+ right_obj
                
    return msg
                