class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        for i in range(len(customers)):
            if i == 0:
                ctt = customers[i][0] + customers[i][1]
                cttw = customers[i][1]
            else: 
                if ctt < customers[i][0] :
                    ctt = customers[i][0] + customers[i][1]
                    cttw = (ctt - customers[i][0]) + cttw
                else:
                    ctt = ctt + customers[i][1]
                    cttw = (ctt - customers[i][0]) + cttw
            print(ctt,cttw)                               
        avgt = cttw/len(customers) 
        return avgt

    
#   3    2
#   11   8
#   14   4
  
    
    
    
    
    
 #   7    2
 #   11   8
 #   14   11
 #   20   12                  
    
    
    
    