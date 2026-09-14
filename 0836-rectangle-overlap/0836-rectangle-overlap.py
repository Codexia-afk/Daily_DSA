class Solution(object):

    def isRectangleOverlap(self, rec1, rec2):
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2

        
        overlap_x = min(x2, x4) > max(x1, x3)
        overlap_y = min(y2, y4) > max(y1, y3)

        return overlap_x and overlap_y