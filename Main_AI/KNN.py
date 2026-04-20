import random

data = []

for i in range(10000):
    if random.random() < 0.5:
        # class 0 centered around (25, 5.5, 2)
        x1 = random.gauss(25, 20)   # mean, std dev
        x2 = random.gauss(5.5, 3)
        x3 = random.gauss(2, 2)
        label = 0
    else:
        # class 1 centered around (75, 11.5, 8)
        x1 = random.gauss(75, 20)
        x2 = random.gauss(11.5, 3)
        x3 = random.gauss(8, 2)
        label = 1

    # add label noise (flip ~10% randomly)
    if random.random() < 0.1:
        label = 1 - label

    data.append((x1, x2, x3, label))
class KNN:
    def __init__(self,data,k):
        self.training_data=data[0:int(0.8*len(data))]
        self.testing_data=data[int(0.8*len(data)):len(data)]
        self.k=k
    def distance(self,point1,point2):
        return (point1[0]-point2[0])**2+(point1[1]-point2[1])**2+(point1[2]-point2[2])**2
    def predict(self,point2):
        distances=[]
        for point1 in self.training_data:
            distances.append((self.distance(point1,point2),point1))
        distances.sort(key=lambda x:x[0])
        lowest_points=distances[:self.k]
        c1=0
        c0=0
        for point in lowest_points:
            cor=point[1]
            cl=cor[3]
            if cl==0:
                c0+=1
            elif cl==1:
                c1+=1
        if c1>c0:
            return 1
        else:
            return 0
    def testing(self):
        self.prediction=[]
        for point in self.testing_data:
            self.prediction.append(self.predict(point))
    def confusion_matrix(self):
        self.tp=0
        self.tn=0
        self.fp=0
        self.fn=0
        actual_result=[]
        for point in self.testing_data:
            actual_result.append(point[3])
        for i in range(int(0.2*len(data))):
            x=actual_result[i] 
            y=self.prediction[i]
            if x==1 and y==1:
                self.tp+=1
            elif x==0 and y==0:
                self.tn+=1
            elif x==0 and y==1:
                self.fp+=1
            elif x==1 and y==0:
                self.fn+=1
        print(f"{self.tp} {self.fp}")
        print(f"{self.fn} {self.tn}")
    def accuracy(self):
        print((self.tp+self.tn)/len(self.testing_data))
    def precision(self):
        print(self.tp/(self.tp+self.fp))
    def recall(self):
        print(self.tp/(self.tp+self.fn))

model=KNN(data,3)
model.testing()
model.confusion_matrix()
model.accuracy()
model.precision()
model.recall()
