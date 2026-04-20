data = [
    (0, 12),
    (2, 15),
    (4, 25),
    (5, 24),
    (7, 32),
    (9, 36),
    (10, 41),
    (12, 45),
    (13, 49),
    (15, 55),
    (16, 52),   # slightly low
    (18, 65),
    (20, 68),
    (21, 74),
    (23, 78),
    (25, 90),   # outlier (high)
    (27, 92),
    (28, 94),
    (30, 101),
    (32, 105),
    (35, 113),
    (37, 120),
    (38, 121),
    (40, 130),  # outlier (high)
    (42, 132),
    (45, 146),
    (47, 148),
    (50, 160)
]
class Model:
    def __init__(self, data, m, c, lr):
        self.data = data
        self.m = m
        self.c = c
        self.lr = lr
    def loss(self, y_pred):
        total=0
        count=0
        for point in self.data:
            y=point[1]
            total+=(y_pred[count]-y)**2
            count+=1
        loss=total/count
        return loss
    def f(self, X):
        return self.m*X+self.c
    def grad_m(self):
        error=0
        for point in self.data:
            error+=2*point[0]*(self.f(point[0])-point[1])
        return error/len(data)
    def grad_c(self):
        error=0
        for point in self.data:
            error+=2*(self.f(point[0])-point[1])
        return error/len(self.data)
    def train(self):
        y_pred=[]
        for point in self.data:
            y_pred.append(self.f(point[0]))
        for i in range(100000):
            y_pred=[]
            for point in self.data:
                y_pred.append(self.f(point[0]))
            self.m-=self.lr*self.grad_m()
            self.c-=self.lr*self.grad_c()
            print(self.loss(y_pred))
    def result(self):
        print(f"The Line is {self.m}X+{self.c}")
        print(f"The Average loss is:{self.loss}")
m1=Model(data,1,1,0.00005)
m1.train()
m1.result()
