# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 16:24:07 2025

@author: DELL
"""

#gọi thư viện pandas và numpy
import pandas as pd
import numpy as np

#Viết chương trình Pandas để tạo và hiển thị DataFrame từ dữ liệu từ điển được chỉ định có nhãn chỉ mục.

#Dữ liệu cho sẵn
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

#List labels thay thành index cho từng dòng → thay vì mặc định là 0,1,2,...
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#Tạo dataframe 
df = pd.DataFrame(exam_data,index=labels)

#output
#Viết chương trình Pandas tìm các giá trị rỗng. sử dụng hàm .isnull()
print(" attemps lớn hơn 2 trong DataFrame ")
print(df[df['score'].isnull()])