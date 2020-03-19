class Solution:
    def isRectangleOverlap(self, rec1, rec2) -> bool:
        return not (rec1[2] <= rec2[0] or
                    rec1[3] <= rec2[1] or
                    rec1[0] >= rec2[2] or
                    rec1[1] >= rec2[3])

class Solution2:
    def isRectangleOverlap(self, rec1, rec2) -> bool:
        rec1x_side = (rec1[2] - rec1[0]) / 2
        rec2x_side = (rec2[2] - rec2[0]) / 2

        rec1x_center_point = rec1x_side + rec1[0]
        rec2x_center_point = rec2x_side + rec2[0]
        x_distance = abs(rec1x_center_point - rec2x_center_point)  # x轴中心点的距离

        rec1y_side = (rec1[3] - rec1[1]) / 2
        rec2y_side = (rec2[3] - rec2[1]) / 2

        rec1y_center_point = rec1y_side + rec1[1]
        rec2y_center_point = rec2y_side + rec2[1]
        y_distance = abs(rec1y_center_point - rec2y_center_point)  # x轴中心点的距离

        if x_distance < rec1x_side + rec2x_side and y_distance < rec1y_side + rec2y_side:
            return True
        else:
            return False

s = Solution2()
rec1 = [11,12,13,13]
rec2 = [17,1,17,19]
print(s.isRectangleOverlap(rec1, rec2))
rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
print(s.isRectangleOverlap(rec1, rec2))
rec1 = [0,0,1,1]
rec2 = [1,0,2,1]
print(s.isRectangleOverlap(rec1, rec2))