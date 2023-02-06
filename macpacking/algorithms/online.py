from math import remainder
from re import L
from .. import Solution, WeightStream
from ..model import Online


class NextFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        bin_index = 0
        solution = [[]]
        remaining = capacity
        for w in stream:
            if remaining >= w:
                solution[bin_index].append(w)
                remaining = remaining - w
            else:
                bin_index += 1
                solution.append([w])
                remaining = capacity - w
        return solution


class TerribleFit(Online):
    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        solution = []
        for w in stream:
            solution.append([w])  #append a list of individual elements 
        
        return solution


'''
Informal Understanding: 
Look at weight, loop over bins, first bin it fits, add it, break;
Go to next weight, loop over bins, if fit, add it, break; 
go to next weight, loop over bins, not fit? -> make new bin, add it; 
'''
class FirstFit(Online):
    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        bin_index=0
        solution = [[]] #stores the solution
        bin_rem=[]
        #for every weight 
        for w in stream: 
            j=0

            while (j < bin_index): #finds the first bin with space
                if (bin_rem[j]>=w):
                    bin_rem[j]=bin_rem[j]-w
                    solution[j].append(w)
                    break 
                j+=1
            
            if (j==bin_index): #if new bin needs to be created 
                bin_rem.append(capacity-w)
                solution.append([w])
                bin_index+=1

        return solution
                
            

class BestFit(Online):
    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        bin_index = 0   #number of bins
        solution = [[]] #stores the solution
        bin_rem=[]  #stores the remaining weight in the bins 
        for w in stream:  #range(len(stream)) right? 
            j=0 
            remaining=capacity+1 
            best_index=0 #best bin for the weight
            for j in range(bin_index):
                if (bin_rem[j]>w and bin_rem[j]-w < remaining): 
                    #if remaining capacity of bin is greater than weight and space left after is less than previous best bin 
                    best_index=j
                    remaining=bin_rem[j]-w
            
            if (remaining == capacity+1): #if no best bin found, create a new one
                bin_rem.append(capacity-w) 
                solution.append([w]) #new bin created with w as first element
                bin_index+=1 #updated with every bin creation
            else:
                bin_rem[best_index] -= w
                solution[best_index].append(w) #item added to the best bin
        return solution

class WorstFit(Online):
    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        bin_index = 0   #number of bins
        solution = [[]] #stores the solution
        bin_rem=[]  #stores the remaining weight in the bins 
        for w in stream: #range(len(stream)) right? 
            j=0 
            remaining=-1 
            worst_index=0 #worst bin for the weight
            for j in range(bin_index):
                if (bin_rem[j]>=w and bin_rem[j]-w > remaining): 
                    #if remaining capacity of bin is greater than weight and space left after is greater than previous worst bin 
                    worst_index=j
                    remaining=bin_rem[j]-w
            
            if (remaining == -1): #if no worst bin found, create a new one
                bin_rem.append(capacity-w) 
                solution.append([w]) #new bin created with w as first element
                bin_index+=1 #updated with every bin creation
            else:
                bin_rem[worst_index] -= w
                solution[worst_index].append(w) #item added to the worst bin
        return solution


class RefinedFirstFit(Online):
    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        solution = [[]]

        C1FF, C2FF, C3FF, C4FF = FirstFit(), FirstFit(), FirstFit(), FirstFit()
        C1, C2, C3, C4 = [],[],[],[]
 
        m = 9 # a fixed integer ([6,9]) described in the paper 

        #Split the Weights into Classes 
        counter = 0
        for w in stream: 
            #classify 
            ratio = w/capacity

            if ratio <= 1 and ratio > 1/2:
                C1.append(w)
            elif ratio <= 1/2 and ratio > 2/5:
                C2.append(w)
            elif ratio <= 2/5 and ratio > 1/3:
                counter+= 1
                if counter > m:
                    C1.append(w)
                else: 
                    C3.append(w)
            else: 
                C4.append(w) 
            

        #Sort the Weights using FirstFit
        C1FF = FirstFit(capacity, C1)
        C2FF = FirstFit(capacity, C2)
        C3FF = FirstFit(capacity, C3)
        C4FF = FirstFit(capacity, C4)

        #Return List of Lists 
        return [C1FF, C2FF, C3FF, C4FF]
        