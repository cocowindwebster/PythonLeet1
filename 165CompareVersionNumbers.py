class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        #ERROR1: "01", "1" , Output : -1 , Expected : 0
        #ERROR1: "1.0", "1" , Output : 1 , Expected : 0
        if version1 == None and version2 == None:
            return 0
        elif version1 == None:
            return -1
        elif version2 == None:
            return 1
        list1 = version1.split(".")
        list2 = version2.split(".")
        list1 = [int(x) for x in list1]
        list2 = [int(x) for x in list2]
        print list1
        print list2
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                return -1
            elif list1[i] > list2[j]:
                return 1
            else:
                i += 1
                j += 1
        while i < len(list1):
            if list1[i] > 0:
                return 1
            i += 1
        while j < len(list2):
            if list2[j] > 0:
                return -1
            j += 1
        return 0

