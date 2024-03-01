class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        answer = []
        for i in emails:
            local,domain = i.split('@')
            local = local.replace('.','')
            for index,j in enumerate(local):
                if j == '+':
                    local = local[:index]
                    break
            email = local + '@' + domain
            answer.append(email)
        return len(set(answer))