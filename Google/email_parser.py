class Solution(object):

    def cleanEmail(self, email):
        """Convert the email address into its
           cleanest version. (i.e.: no '.' or '+')
        Args:
          email: The original email string.
        Returns:
          Clean email string.
        """

        # Check if email string is empty
        if not email:
            return email

        # Divide email string into 'local' and 'domain'
        i = len(email) - 1
        while i >= 0:
            if email[i] == '@':
                break
            i -= 1
        local = email[:i]
        domain = email[i:]

        # Clean the local part
        local_clean = ""
        for char in local:
            if char == '+':
                break
            elif char != '.':
                local_clean += char

        # Concatenate and return the result
        return local_clean + domain


    def emailParser(self, emails):
        """Return the number of unique email strings
           in the given list that occurs more than once.
        Args:
          emails: A list of email strings.
        Returns:
          Number of unique email strings that occurs more than once.
        """

        # Use a hashmap to record the number of
        # occurrence of each unique email string
        memo = dict()
        for email in emails:
            email = self.cleanEmail(email)
            print(email)
            if email not in memo:
                memo[email] = 1
            else:
                memo[email] += 1

        # Count the number of occurrence for each
        # unique email string and return the result
        ans = 0
        for key, value in memo.items():
            if value > 1:
                ans += 1
        return ans



input = ['ab_1@example.com',
         'x@example.com',
         'x@exa.mple.com',
         'ab+1@example.com',
         'y@example.com',
         'y@example.com',
         'y@example.com']
mySolution = Solution()
ans = mySolution.emailParser(input)
print(ans)
