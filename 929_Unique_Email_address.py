class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        UniqueEmails = set()
        for email in emails:
            (cleanedLocalName, domain) = email.split('@')
            cleanedLocalName = (cleanedLocalName.split('+')[0]).replace('.', '')
            UniqueEmails.add(cleanedLocalName + '@' + domain)
        
        return len(UniqueEmails)