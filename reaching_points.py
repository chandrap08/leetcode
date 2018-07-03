class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """

        while sx < tx and sy < ty: tx, ty = tx % ty, ty % tx
        return sx == tx and (ty - sy) % sx == 0 or sy == ty and (tx - sx) % sy == 0