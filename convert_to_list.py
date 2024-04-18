# 定义点的列表，每个点的坐标以字典形式给出
points = [
    {'longitude': 116.35679745678053, 'latitude': 39.96491016630655},
    {'longitude': 116.357072, 'latitude': 39.964884},
    {'longitude': 116.35665038188299, 'latitude': 39.96392340071386},
    {'longitude': 116.357173, 'latitude': 39.963754},
    {'longitude': 116.35803138097535, 'latitude': 39.96361283073395},
    {'longitude': 116.358623, 'latitude': 39.963862},
    {'longitude': 116.35905951553204, 'latitude': 39.963434022680914},
    {'longitude': 116.358688, 'latitude': 39.963305},
    {'longitude': 116.357179, 'latitude': 39.96327},
    {'longitude': 116.35668923965758, 'latitude': 39.962485317018285},
    {'longitude': 116.3564751101895, 'latitude': 39.96191848662335},
    {'longitude': 116.357228, 'latitude': 39.962273},
    {'longitude': 116.358729, 'latitude': 39.962336},
    {'longitude': 116.358778, 'latitude': 39.961195},
    {'longitude': 116.35840523256256, 'latitude': 39.96119784480619},
    {'longitude': 116.357278, 'latitude': 39.961194},
    {'longitude': 116.3567692984475, 'latitude': 39.960475447846505},
    {'longitude': 116.357316, 'latitude': 39.960427},
    {'longitude': 116.35809193723807, 'latitude': 39.960490904153794},
    {'longitude': 116.35864, 'latitude': 39.960466}
]

# 创建边的列表
edges = []

# 连接每个点到下一个点，构成边
for i in range(len(points) - 1):  # 遍历除最后一个点外的所有点
    edge = [points[i], points[i+1]]
    edges.append(edge)

# 最后一个点与第一个点连接（如果需要形成闭环）
# 如果不需要形成闭环，注释掉下面这行代码
# edges.append([points[-1], points[0]])

# 输出结果
print(edges)
