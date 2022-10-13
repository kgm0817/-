x_axis, y_axis = order.order(df)
x_index = x_axis.index(num)  # x 축 인덱스 번호
y_index = y_axis[x_index]  # y 축 값q
consider_list_4 = y_axis[x_index + 1:]  # 고려해야하는 Y축 리스트