import math


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
M=1
C=1
def loss(y_pred):
    Total=0
    count=0
    for point in data:
        y=point[1]
        total+=(y_pred[count]-y)**2
        count+=1
    loss=total/len(data)
    return loss

def f(X):
    return M*X+C



