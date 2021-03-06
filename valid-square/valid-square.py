class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2 or p1 == p3 or p1 == p4 or p2 == p3 or p2 == p4 or p3 == p4: 
                return False
        else:
            p1,p2,p3,p4 = sorted([p1,p2,p3,p4])
            n1 = ((p1[0]-p4[0])**2)+((p1[1]-p4[1])**2)
            
            n2 = ((p2[0]-p3[0])**2)+((p2[1]-p3[1])**2)
            if n1 == n2 :
                print(p1,p2,p3,p4)
                l1 = ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) 
                l2 = ((p2[0]-p4[0])**2)+((p2[1]-p4[1])**2) 
                l3 = ((p4[0]-p3[0])**2)+((p4[1]-p3[1])**2) 
                l4 = ((p3[0]-p1[0])**2)+((p3[1]-p1[1])**2) 

                print(l1)
                print(l2)
                print(l3)
                print(l4)

                if l1 == l2 and l2 == l3 and l3 == l4 and l4 == l1 :
                    print('true')
                    return True
                else:
                    print('false')
                    return False
            else:
                print('false')
                return False  