class Solution(object):
    def largestAltitude(self, gain):
        highest=0;
        altitute=0;
        for gain in gain:
            altitute+=gain
            highest=max(altitute,highest);
        return highest
            
        