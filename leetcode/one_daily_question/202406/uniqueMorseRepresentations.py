class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
            "....", "..", ".---", "-.-", ".-..", "--", "-.",
            "---", ".--.", "--.-", ".-.", "...", "-", "..-",
            "...-", ".--", "-..-", "-.--", "--..",
        ]
        morse_set = set()
        for word in words:
            trans = ""
            for c in word:
                trans += morse[ord(c) - ord('a')]
            morse_set.add(trans)
        return len(morse_set)