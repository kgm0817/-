import stockyard
import sys
#inital value
#epoch = 10, params = [[20, 20, 3, 7, 0, 100, 100]], flag = [True,True,True,True], methods = ['random']

# 여러 파라미터 확인
'''params = [[20, 30, 3, 4, 0, 30, 30], [20, 30, 3, 4, 15, 30, 30],[20, 30, 3, 7, 0, 30, 30],[20, 30, 3, 7, 0, 100, 100]]'''

# 여러 메소드 확인
flag = [[True,False,False,False]]
methods = ['random', 'depth', 'quad2', 'quad4']
# methods = ['random']
# sys.stdout = open("test.txt", "a")

# params = [[40, 40, 3, 7, 10, 50, 60], [40, 40, 3, 7, 10, 100, 110], [40, 40, 3, 7, 10, 150, 160]]
params = [[20, 20, 3, 4, 10, 50, 50]]
# params = [[30, 30, 3, 4, 0, 250, 250]]
stockyard.sota(epoch=50, params=params, flag=flag, methods=methods)
# stockyard.sota(epoch=50, params=xzcv, flag=None, methods=['quad4'])
# stockyard.sota(epoch=10, params=[[30, 30, 3, 6, 10, 100, 100]], flag=None, methods=['quad4'])

# sys.stdout.close()