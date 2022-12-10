def tallest_stack(boxes):
    """
    This function returns the height of tallest stack
    formed by the given boxes.
    """
    boxes.sort(key=lambda x: x[0])
    heights = {box:box[2] for box in boxes}
    for i in range(1, len(boxes)):
        box = boxes[i]
        stack = [boxes[j] for j in range(i) if can_be_stacked(boxes[j], box)]
        heights[box] = box[2] + max([heights[box] for box in stack], default=0)
    
    return max(heights.values(), default=0)

def can_be_stacked(top, bottom):
    """
    This function returns a boolean value if a box 
    can be stacked on the other one.
    """
    return top[0]<bottom[0] and top[1]<bottom[1]


if __name__ == "__main__":
    #boxes_array = [(4,1,5), (2,1,2), (4,1,2), (5,2,1), (2,2,4), (5,3,3), (3,4,1), (2,5,3), (4,5,1)]
    boxes_array = [(1,2,2), (1,5,4), (2,3,2), (2,4,1), (3,6,2), (4,5,3)]
    result = tallest_stack(boxes_array)
    print(result)
