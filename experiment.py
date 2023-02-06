from macpacking import Solution
from macpacking.algorithms import baseline, offline, online
from macpacking.reader import DatasetReader, BinppReader, JburkardtReader
import matplotlib.pyplot as plt


class experiment():
    def __init__(self, dataset, dataset_capacity = None):
        self.dataset = dataset
        self.dataset_capacity = dataset_capacity  #only used ofr jburkardt


    def get_optimal_solution(self, search, filename):  #finds the optimal solution in oracle and returns it 
        with open(search, 'r') as reader:
            lines = reader.readlines()
        
        for line in lines:
            file, solution = line.split(',')
            if file == filename:
                return int(solution)


    def get_optimal_file(self):  #finds the data type, the file destination and the data file and returns 
        data_split = self.dataset.split('/')
        data_type = data_split[1]


        if (data_type == "binpp"):
            search = "_datasets/Solutions/binpp_solution.csv"
            filename = data_split[3].split('.')
            filename = filename[0]
        elif (data_type == "binpp-hard"):
            search = "_datasets/Solutions/binpp_hard_solution.csv"
            filename = data_split[2].split('.')
            filename = filename[0]
        else:
            search = "_datasets/Solutions/jburkardt_sol.csv"
            filename = data_split[2].split('.')
            filename = filename[0]
            filename = filename.strip('_w')
            filename = filename.replace('0','_0')
            
        return data_type, search, filename

    def get_data(self, data_type): #given the data type, uses the readers to read the data 
        if (data_type == 'jburkardt'):
            reader: DatasetReader=JburkardtReader(self.dataset_capacity, self.dataset)
            capacity = reader.offline()[0]
            weights = reader.offline()[1]
            return capacity, weights
        else:
            reader: DatasetReader=BinppReader(self.dataset)
            capacity=reader.offline()[0]
            weights=reader.offline()[1]
            return capacity,weights

    def get_baseline(self, capacity, weights): #runs baseline algo
        solution=baseline.BenMaier
        num=solution._process(solution, capacity, weights)
        #print (num)
        return len(num)

    def get_first_fit_online(self, capacity, weights): #runs first fit online algorithm 
        solution=online.FirstFit
        num=solution._process(solution, capacity, weights)
        #print (num)
        return len(num)

    def get_terrible_fit_online(self, capacity, weights):
        solution=online.TerribleFit
        num=solution._process(solution, capacity, weights)
        #print (num)
        return len(num)

    def get_next_fit_online(self, capacity, weights):
        solution=online.NextFit
        num=solution._process(solution, capacity, weights)
        #print (num)
        return len(num)

    def get_best_fit_online(self, capacity, weights):
        solution=online.BestFit
        num=solution._process(solution, capacity, weights)
        #print (num)
        return len(num)

    def get_worst_fit_online(self, capacity, weights):
        solution=online.WorstFit
        num=solution._process(solution, capacity, weights)
        #print (num)
        return len(num)

    def get_next_fit_offline(self, capacity, weights):
        solution=offline.NextFit
        num=solution._process(solution, capacity, weights)
        #print (num)
        return len(num)

    def get_first_fit_offline(self, capacity, weights):
        solution=offline.FirstFitDecreasing
        num=solution._process(solution, capacity, weights)
        #print (num)
        return len(num)

    def get_best_fit_offline(self, capacity, weights):
        solution=offline.BestFitDecreasing
        num=solution._process(solution, capacity, weights)
        #print (num)
        return len(num)

    def get_worst_fit_offline(self, capacity, weights):
        solution=offline.WorstFitDecreasing
        num=solution._process(solution, capacity, weights)
        #print (num)
        return len(num)

    def get_array(self): #runs all algorithms and returns the optimal solution, a array of bins and y values for the graph 
        y_values=[]
        bins=[]
        data_type,search,filename=self.get_optimal_file()
        solution=self.get_optimal_solution(search,filename)
        capacity,weights=self.get_data(data_type)

        bins.append(self.get_baseline(capacity, weights))
        bins.append(self.get_next_fit_online(capacity, weights))
        bins.append(self.get_terrible_fit_online(capacity, weights))
        bins.append(self.get_first_fit_online(capacity, weights))
        bins.append(self.get_best_fit_online(capacity, weights))
        bins.append(self.get_worst_fit_online(capacity, weights))
        bins.append(self.get_next_fit_offline(capacity, weights))
        bins.append(self.get_first_fit_offline(capacity, weights))
        bins.append(self.get_best_fit_offline(capacity, weights))
        bins.append(self.get_worst_fit_offline(capacity, weights))

        for i in range(len(bins)):
            y_values.append(bins[i]-solution)
        
        return solution, y_values, bins

    def plot_graph(self, optimal, y): #graphs the results 
        x=["B","NFON","TF","FFON","BFON","WFON","NFOff","FFOff","BFOff","WFOff"]
        plt.scatter(x, y)
        plt.xlabel('Algorithms')
        plt.ylabel('Additional Bins')
        plt.title('Optimal Bins = '+str(optimal))
        for i, text in enumerate(y):
            plt.annotate(text, (x[i],y[i]))
        plt.show()

#examples below
temp1=experiment('_datasets/binpp/N1C1W1/N1C1W1_B.BPP.txt')
solution,y,b=temp1.get_array()
print (y)
print (b)
temp1.plot_graph(solution,y)

dataset="_datasets/jburkardt/p01_w.txt"
dataset2='_datasets/jburkardt/p01_c.txt'
temp2=experiment(dataset,dataset2)
solution,y,b=temp2.get_array()
print (y)
print (b)
temp2.plot_graph(solution,y)

temp3=experiment("_datasets/binpp-hard/HARD3.BPP.txt")
solution,y,b=temp3.get_array()
temp3.plot_graph(solution,y)
