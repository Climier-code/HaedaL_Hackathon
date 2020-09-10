import getGTML
import excel

#Get_same_lec(code,ex_df) #ex_df는 데이터프레임. 정규학기 디비에 대해서 하는 것
test1 = getGTML.Get_same_lec(code,sw_df) #계절학기 디비에 대해 하는 것

#Get_same_time(code,ex_df) 정규학기 디비에 대해 하는 것
test = Get_same_time(code,sw_df) #계절학기 디비에 대해 하는 것

test = test.applymap(str)
test1 = test1.applymap(str)