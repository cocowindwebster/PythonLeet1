class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        if secret == None or guess == None:
            return ""
        countA = 0
        countB = 0
        dict = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                countA += 1
            #ERROR1
            # dict[secret[i]] +=1
            dict[secret[i]] = dict.get(secret[i], 0) + 1

        for i in range(len(guess)):
           # ERRRO1
           #  if dict[guess[i]] > 0:
           if dict.get(guess[i], 0) > 0:
                countB += 1
                dict[guess[i]] -= 1
        countB -= countA
        return str(countA) + "A" + str(countB) + "B"