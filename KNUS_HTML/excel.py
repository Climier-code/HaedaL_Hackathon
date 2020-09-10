from dateutil.parser import parse
import csv
import pickle
import json
import time
import random
from urllib.request import urlopen
from urllib.parse   import quote
from datetime import datetime, timedelta
import re
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os
from selenium import webdriver
from random import randint
from urllib.request import Request
import requests
import random
import sqlite3
from IPython.display import display #이거 써봐라..
from xlrd import open_workbook  #정규학기 불러오기  엑셀 -> df


def elim_bar(x): #텍스트에서 바 없애는 함수
    return x.replace('-','')

pd.options.display.max_columns = None
pd.options.display.max_rows = 300

workbookName = r"D:\해달\knu_major.xlsx" #엑셀파일 불러오기
sheet = open_workbook(workbookName).sheets()[0] #시트 불러오기

flag = 0  # 엑셀 파일 시트에서 데이터프레임으로 만드는 부분
out_list = []
개설대학 = ''

for rowidx in range(sheet.nrows):

    empty_dict = {}

    row = sheet.row(rowidx)
    key = row[3].value  # 맨 왼쪽에서 4번째 줄을 구분자로 활용, 숫자가 들어가 있으면 해당 로우 값을 다 저장, 직전의 개설대학 값과 함께

    if row[5].value == '수  업  시  간  표':
        flag = 1
        continue

    if flag == 1:
        개설대학 = row[1].value
        flag = 0
        continue

    try:
        num = int(key[-1])
    except:
        continue

    empty_dict['학년'] = row[1].value
    empty_dict['구분'] = row[2].value
    empty_dict['교과번호-분반'] = row[3].value
    empty_dict['교과목명'] = row[4].value
    empty_dict['학점'] = row[6].value
    empty_dict['강의'] = row[7].value
    empty_dict['실습'] = row[8].value
    empty_dict['담당교수'] = row[9].value
    empty_dict['강의시간(요일,교시)'] = row[10].value
    empty_dict['강의실'] = row[13].value
    empty_dict['비고'] = row[14].value
    empty_dict['개설대학'] = 개설대학
    out_list.append(empty_dict)  # 추가되는 줄, 가장 최근의 개설대학 값을 바탕으로



ex_df = pd.DataFrame(out_list) #데이터 프레임으로 변형
ex_df['교과번호-분반'] = ex_df['교과번호-분반'].map(elim_bar) #학기
column_list = ['교과번호-분반', '학점', '강의', '실습', '교과목명', '구분', '수강정원', '강의시간(요일,교시)', '강의실',
       '개설대학', '개설\n학과', '개설\n전공', '담당교수', '팀티칭\n여부', '스마트러닝\n강좌 여부', '직급',
       '교수소속\n대학', '교수소속\n학과', '강의\n언어', '교과목명\n(영문)','학년', '비고']
ex_df = ex_df.loc[:,column_list]

#계절학기 불러오기 엑셀 -> df
sw_df = pd.read_excel (r'D:\해달\2019겨울계절수업 개설강좌 수업시간표.xls', header = [2]) #for an earlier version of Excel, you may need to use the file extension of 'xls'

sw_df.columns = ['교과번호-분반', '학점', '강의', '실습', '교과목명', '구분', '수강정원', '강의시간(요일,교시)', '강의실',
       '개설대학', '개설\n학과', '개설\n전공', '담당교수', '팀티칭\n여부', '스마트러닝\n강좌 여부', '직급',
       '교수소속\n대학', '교수소속\n학과', '강의\n언어', '교과목명\n(영문)', '비고'] #학년칼럼이 없어서추가.
sw_df= sw_df.loc[:,column_list]
sw_df['교과번호-분반'] = sw_df['교과번호-분반'].map(elim_bar)