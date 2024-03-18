class Solution:
    def reformatDate(self, date: str) -> str:
        answer = []
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        date = date.split(' ')

        answer.append(date[2])
        
        for i,month in enumerate(months):
            if month == date[1]:
                if i < 9:
                    answer.append('0'+str(i+1))
                else:
                    answer.append(str(i+1))
        
        if len(date[0][:-2]) < 2:
            answer.append('0'+date[0][:-2])
        else:
            answer.append(date[0][:-2])
        
        return '-'.join(answer)