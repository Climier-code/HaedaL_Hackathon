import urllib.request           # 웹크롤링 모듈
import bs4                      # 웹크롤링 모듈
import time

def Current_enrollment_num(code): # 실시간 수강신청 인원
    code = code.upper()        #과목코드의 영문부분을 모두 대문자로 표기

    ## URL에 들어갈 정보
    # '학기(semester) ex.20192',
    # '과목분반정보(subClass) ex. 001',
    # '과목정보(maincode) ex. ENGR211,
    # '모든코드(code) ex. ENGR211001,

    ####################'학기(Year_semester)'#########################
    ## 월 추출(정수)
    Month_int = int(time.strftime("%m", time.localtime(time.time())))

    ## 년 추출(문자)
    Year_int = str(time.strftime("%Y", time.localtime(time.time())))

    ##학기 추출
    if Month_int <= 3:  # 1, 2, 3월이면
        semester = "1"  # 1학기 수강신청
    elif 4 <= Month_int <= 6:  # 4, 5, 6월이면
        semester = "S"  # 여름학기 수강신청
    elif 7 <= Month_int <= 9:  # 7, 8, 9월이면
        semester = "2"  # 2학기 수강신청
    elif 10 <= Month_int <= 12:  # 10, 11, 12월이면
        semester = "W"  # 겨울학기 수강신청
    Year_semester = Year_int + semester  # ex. Year_semester는 "20192"

    subClass = code[7:]     # '과목분반정보(subClass) ex. 001'
    maincode = code[:7]     # '과목분반정보(subClass) ex. ENGR211'

    url ="http://my.knu.ac.kr/stpo/stpo/cour/lectReqCntEnq/list.action?&lectReqCntEnq.search_open_yr_trm="+Year_semester+"&lectReqCntEnq.search_sub_class_cde="+subClass+"&lectReqCntEnq.search_subj_cde="+maincode+"&searchValue="+code
    html = urllib.request.urlopen(url)      # html 코드 받기
    bsObj = bs4.BeautifulSoup(html, "html.parser")  #bs4에 html 코드 넣기

    # 현 과목코드에 대한 정보가 없을시에 0값을 도출합니다
    try:
        current_num = int(bsObj.find("td", {"class": "lect_req_cnt"}).text)     # 실시간 정원
        limit_num = int(bsObj.find("td", {"class": "lect_quota"}).text)         # 수용정원
    except:
        return [0, 0]

    return [limit_num, current_num]     # [수용정원, 실시간 정원]


def Get_same_lec(code,df):  #code 입력 과목과 같은 과목 다른 시간
    return_df = df.loc[df.loc[:,'교과번호-분반'].str.contains(code[:7]),:]
    return_df.loc[:,'수용정원'] = 'no'
    return_df.loc[:,'실시간정원'] = 'no'
    for index, row in return_df.iterrows():
        return_list = Current_enrollment_num(row['교과번호-분반'])
        print(return_list)
        return_df.loc[index,'수용정원'] = return_list[0]
        return_df.loc[index,'실시간정원'] = return_list[1]
    #return_df['잔여정원'] = return_df['수용정원'].map(int) - return_df['실시간정원'].map(int)
    return return_df


def Get_same_time(code,df): #code 입력과목과 다른 과목 같은 시간
    for index, value in df.loc[df['교과번호-분반'] == code,'강의시간(요일,교시)'].iteritems(): #더 좋은 방법이 있다면. 이렇게.
        return_df = df.loc[df['강의시간(요일,교시)'] == value,:]
    for index, row in return_df.iterrows():
        return_list = Current_enrollment_num(row['교과번호-분반'])
        print(return_list)
        return_df.loc[index,'수용정원'] = return_list[0]
        return_df.loc[index,'실시간정원'] = return_list[1]
    return return_df



