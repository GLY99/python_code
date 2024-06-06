class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        my_set = set()
        for email in emails:
            i = email.index('@')
            local = email[:i].split('+', 1)[0]
            local = local.replace('.', '')
            my_set.add(local + email[i:])
        return len(my_set)