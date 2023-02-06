import json 
import matplotlib.pyplot as plt

class jsonReader:
    def __init__(self, fileName:str) -> None:
        self.fileName = fileName
        self.data: list
    
    def extractData(self):
        f = open(self.fileName) #Open provided file 
        data = json.load(f) #returns JSON object as a dictionary
    
        times = []
        executionTimes = []
        for i in data['benchmarks']:
            #We ignore the first element in runs since it is the only file that does not have the values element
            for j in range(1, len(i['runs'])): 
                times.append(i['runs'][j]['metadata']['load_avg_1min'])

            #Append [file_name, average of load_avg_1min] to list
            executionTimes.append([i['metadata']['name'], sum(times)/len(i['runs'])])
        
            #Clear our times list for next set of values 
            times = []
            
        f.close() #Close .json file 
        self.data = executionTimes
        return executionTimes



class jsonDataPlotter():
    def __init__(self, data:jsonReader) -> None:
        self.data = data

    def plotData(self):

        xAxis = [i[0] for i in self.data] #file names
        print(xAxis)

        #For the binpp and binpp-hard altogrithms  
        xAxis = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
        yAxis = [i[1] for i in self.data]
        
        #Customize this section
        plt.scatter(xAxis,yAxis)
        plt.xlabel('File Name - N4C2W2_<Letter>')
        plt.ylabel('Execution Times')
        plt.title("Exeution Time on RefinedFirstFit")
        plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
        
        plt.show()

class jsonDataPlotterMuliple():
    def __init__(self, data:list, algos:list) -> None:
        self.data = data #list of lists 
        self.algos = algos #list of names for legend 

    def plotData(self):

        #For the binpp and binpp-hard altogrithms  
        xAxis = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
        
        count = 0
        for j in self.data:
            yAxis = [i[1] for i in j.data]
            plt.plot(xAxis,yAxis,label=self.algos[count])
            plt.legend()
            count +=1 


        #Customize this section
        plt.xlabel('File Name - N4C2W2_<Letter>')
        plt.ylabel('Execution Times')
        plt.title("Exeution Time on Online Algorithms")
        plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

        plt.show()

