import pandas as pd
import os 

# data = {
#     'apples': [3, 2, 1, 5],
#     'oranges': [2, 4, 1, 7]
# }

# basket_df = pd.DataFrame(data, index = ['바구니1', '바구니2', '바구니3', '바구니4'])

# print(basket_df)
# current_directory = os.getcwd()
# print(f"현재 작업 디렉토리: {current_directory}")


df = pd.read_csv("방통대_데이터/grade.csv", index_col=0)

print(df)