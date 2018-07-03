str1 = raw_input()
p1_x = float(str1.split(" ")[0])
p1_y = float(str1.split(" ")[1])

str1 = raw_input()
p2_x = float(str1.split(" ")[0])
p2_y = float(str1.split(" ")[1])

str1 = raw_input()
p3_x = float(str1.split(" ")[0])
p3_y = float(str1.split(" ")[1])

import math
diff1 = (p2_x - p1_x)**2 + (p2_y - p1_y)**2
edge1 = math.sqrt(diff1)

diff2 = (p3_x - p1_x)**2 + (p3_y - p1_y)**2
edge2 = math.sqrt(diff2)

diff3 = (p3_x - p2_x)**2 + (p3_y - p2_y)**2
edge3 = math.sqrt(diff3)

if(edge1 == edge2 and edge2 == edge3):
    area = math.sqrt(3)/4 * (edge1**2)
    print area
elif((edge1/edge2) == math.sqrt(2) or edge1/edge3 == math.sqrt(2)):
    area = edge2**2
    print area

