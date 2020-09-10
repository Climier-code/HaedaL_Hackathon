#-*- coding:utf-8 -*-

import pandas as pd



#create dataframe
df_marks = pd.DataFrame[{'교과번호-분반': 'CLTR011001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '중국어1', '구분': '교양', '수강정원': '50', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '대학원동301', '개설대학': '인문대학', '개설\n학과': '중어중문학과', '개설\n전공': 'nan', '담당교수': '정영지', '팀티칭\n여부': 'Y', '스마트러닝\n강좌 여부': 'nan', '직급': '강사', '교수소속\n대학': '인문대학', '교수소속\n학과': '중어중문학과', '강의\n언어': 'nan', '교과목명\n(영문)': 'Freshman Chinese1', '학년': 'nan', '비고': 'nan', '수용정원': '50.0', '실시간정원': '43.0'}, {'교과번호-분반': 'CLTR017001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '실용한자', '구분': '기본소양', '수강정원': '100', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '인문한국진흥관102', '개설대학': '인문대학', '개설\n학과': '한문학과', '개설\n전공': 'nan', '담당교수': '박영호', '팀티칭\n여부': 'Y', '스마트러닝\n강좌 여부': 'nan', '직급': '교수', '교수소속\n대학': '인문대학', '교수소속\n학과': '한문학과', '강의\n언어': 'nan', '교과목명\n(영문)': 'Practical Classical Chinese', '학년': 'nan', '비고': 'nan', '수용정원': '100.0', '실시간정원': '30.0'}, {'교과번호-분반': 'CLTR032002', '학점': '3', '강의': '3', '실습': '0', '교과목명': '일어 I', '구분': '교양', '수강정원': '70', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '인문한국진흥관105', '개설대학': '인문대학', '개설\n학과': '일어일문학과', '개설\n전공': 'nan', '담당교수': '이자호', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '교수', '교수소속\n대학': '인문대학', '교수소속\n학과': '일어일문학과', '강의\n언어': 'nan', '교과목명\n(영문)': 'Japanese Language I', '학년': 'nan', '비고': 'nan', '수용정원': '70.0', '실시간정원': '23.0'}, {'교과번호-분반': 'CLTR044001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '철학의이해', '구분': '교양', '수강정원': '55', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '인문대학422', '개설대학': '인문대학', '개설\n학과': '철학과', '개설\n전공': 'nan', '담당교수': '김윤동', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '교수', '교수소속\n대학': '인문대학', '교수소속\n학과': '철학과', '강의\n언어': 'nan', '교과목명\n(영문)': 'Understanding of Philosophy', '학년': 'nan', '비고': 'nan', '수용정원': '55.0', '실시간정원': '30.0'}, {'교과번호-분반': 'CLTR045001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '논리와 비판적 사고', '구분': '기본소양', '수강정원': '120', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '인문대학101', '개설대학': '인문대학', '개설\n학과': '철학과', '개설\n전공': 'nan', '담당교수': '권홍우', '팀티칭\n여부': 'Y', '스마트러닝\n강좌 여부': 'nan', '직급': '조교수', '교수소속\n대학': '인문대학', '교수소속\n학과': '철학과', '강의\n언어': 'nan', '교과목명\n(영문)': 'Logic and Critical Thinking', '학년': 'nan', '비고': 'nan', '수용정원': '120.0', '실시간정원': '96.0'}, {'교과번호-분반': 'CLTR074001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '결혼과 가족관계', '구분': '교양', '수강정원': '120', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '생활과학대학401', '개설대학': '생활과학대학', '개설\n학과': '아동학부', '개설\n전공': 'nan', '담당교수': '백경숙', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '교수', '교수소속\n대학': '생활과학대학', '교수소속\n학과': '아동학부', '강의\n언어': 'nan', '교과목명\n(영문)': 'Marriage & Family Relationships', '학년': 'nan', '비고': 'nan', '수용정원': '120.0', '실시간정원': '85.0'}, {'교과번호-분반': 'CLTR083001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '경제의이해', '구분': '기본소양', '수강정원': '130', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '경상대학311', '개설대학': '경상대학', '개설\n학과': '경제통상학부', '개설\n전공': 'nan', '담당교수': '이상락', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '강의초빙교수', '교수소속\n대학': '경상대학', '교수소속\n학과': '경제통상학부', '강의\n언어': 'nan', '교과목명\n(영문)': 'Understanding of Economy', '학년': 'nan', '비고': 'nan', '수용정원': '130.0', '실시간정원': '32.0'}, {'교과번호-분반': 'CLTR085001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '경영의이해', '구분': '기본소양', '수강정원': '120', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '경상대학201', '개설대학': '경상대학', '개설\n학과': '경영학부', '개설\n전공': 'nan', '담당교수': '김상현', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '교수', '교수소속\n대학': '경상대학', '교수소속\n학과': '경영학부', '강의\n언어': 'nan', '교과목명\n(영문)': 'Introduction to Management', '학년': 'nan', '비고': 'nan', '수용정원': '120.0', '실시간정원': '93.0'}, {'교과번호-분반': 'CLTR096001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '영상으로보는독일문화', '구분': '교양', '수강정원': '140', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '인문대학110', '개설대학': '인문대학', '개설\n학과': '독어독문학과', '개설\n전공': 'nan', '담당교수': '이덕형', '팀티칭\n여부': 'Y', '스마트러닝\n강좌 여부': 'nan', '직급': '교수', '교수소속\n대학': '인문대학', '교수소속\n학과': '독어독문학과', '강의\n언어': 'nan', '교과목명\n(영문)': 'German Culture in the Film', '학년': 'nan', '비고': 'nan', '수용정원': '140.0', '실시간정원': '111.0'}, {'교과번호-분반': 'CLTR112001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '생활속의통계', '구분': '기본소양', '수강정원': '80', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '자연과학대학401', '개설대학': '자연과학대학', '개설\n학과': '통계학과', '개설\n전공': 'nan', '담당교수': '조교영', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '교수', '교수소속\n대학': '자연과학대학', '교수소속\n학과': '통계학과', '강의\n언어': 'nan', '교과목명\n(영문)': 'Statistics in Real Life', '학년': 'nan', '비고': 'nan', '수용정원': '80.0', '실시간정원': '77.0'}, {'교과번호-분반': 'CLTR133001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '국악의 이해', '구분': '교양', '수강정원': '70', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '조형관(제3합동강의동)104', '개설대학': '예술대학', '개설\n학과': '국악학과', '개설\n전공': 'nan', '담당교수': '주영위', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '교수', '교수소속\n대학': '예술대학', '교수소속\n학과': '국악학과', '강의\n언어': 'nan', '교과목명\n(영문)': 'Understanding of Korean Music', '학년': 'nan', '비고': 'nan', '수용정원': '120.0', '실시간정원': '56.0'}, {'교과번호-분반': 'CLTR134002', '학점': '3', '강의': '3', '실습': '0', '교과목명': '음악의 이해', '구분': '교양', '수강정원': '70', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '조형관(제3합동강의동)101', '개설대학': '예술대학', '개설\n학과': '음악학과', '개설\n전공': 'nan', '담당교수': '김정아', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '부교수', '교수소속\n대학': '예술대학', '교수소속\n학과': '음악학과', '강의\n언어': 'nan', '교과목명\n(영문)': 'Understanding of Music', '학년': 'nan', '비고': 'nan', '수용정원': '70.0', '실시간정원': '68.0'}, {'교과번호-분반': 'CLTR135001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '한국가곡의 이해', '구분': '교양', '수강정원': '70', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '예술대학106', '개설대학': '예술대학', '개설\n학과': '음악학과', '개설\n전공': 'nan', '담당교수': '유소영', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '교수', '교수소속\n대학': '예술대학', '교수소속\n학과': '음악학과', '강의\n언어': 'nan', '교과목명\n(영문)': 'Understanding of Korean Art Songs', '학년': 'nan', '비고': 'nan', '수용정원': '0.0', '실시간정원': '0.0'}, {'교과번호-분반': 'CLTR188001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '현대인과 패션', '구분': '교양', '수강정원': '70', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '생활과학대학402', '개설대학': '생활과학대학', '개설\n학과': '의류학과', '개설\n전공': 'nan', '담당교수': '구양숙', '팀티칭\n여부': 'Y', '스마트러닝\n강좌 여부': 'nan', '직급': '교수', '교수소속\n대학': '생활과학대학', '교수소속\n학과': '의류학과', '강의\n언어': 'nan', '교과목명\n(영문)': 'Modern Life and Fashion', '학년': 'nan', '비고': 'nan', '수용정원': '70.0', '실시간정원': '46.0'}, {'교과번호-분반': 'CLTR205001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '대학글쓰기', '구분': '기본소양', '수강정원': '30', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': 'KNU글로벌프라자402', '개설대학': '교육개발본부', '개설\n학과': '교양교육센터', '개설\n전공': 'nan', '담당교수': '김도경', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '강의초빙교수', '교수소속\n대학': '교육개발본부', '교수소속\n학과': '교양교육센터', '강의\n언어': 'nan', '교과목명\n(영문)': 'Basic Writing', '학년': 'nan', '비고': 'nan', '수용정원': '30.0', '실시간정원': '31.0'}, {'교과번호-분반': 'CLTR211001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '수학 I', '구분': '전공기반', '수강정원': '65', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '자연과학대학219', '개설대학': '자연과학대학', '개설\n학과': '수학과', '개설\n전공': 'nan', '담당교수': '임정욱', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '부교수', '교수소속\n대학': '자연과학대학', '교수소속\n학과': '수학과', '강의\n언어': 'nan', '교과목명\n(영문)': 'Calculus I', '학년': 'nan', '비고': 'nan', '수용정원': '0.0', '실시간정원': '0.0'}, {'교과번호-분반': 'CLTR211002', '학점': '3', '강의': '3', '실습': '0', '교과목명': '수학 I', '구분': '전공기반', '수강정원': '65', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': 'KNU글로벌프라자510', '개설대학': '자연과학대학', '개설\n학과': '수학과', '개설\n전공': 'nan', '담당교수': '최선미', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '강의초빙교수', '교수소속\n대학': '교육개발본부', '교수소속\n학과': '교양교육센터', '강의\n언어': 'nan', '교과목명\n(영문)': 'Calculus I', '학년': 'nan', '비고': 'nan', '수용정원': '65.0', '실시간정원': '57.0'}, {'교과번호-분반': 'CLTR212001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '수학 II', '구분': '전공기반', '수강정원': '65', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': 'KNU글로벌프라자502', '개설대학': '자연과학대학', '개설\n학과': '수학과', '개설\n전공': 'nan', '담당교수': '서명수', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '강의초빙교수', '교수소속\n대학': '교육개발본부', '교수소속\n학과': '교양교육센터', '강의\n언어': 'nan', '교과목명\n(영문)': 'Calculus II', '학년': 'nan', '비고': 'nan', '수용정원': '65.0', '실시간정원': '33.0'}, {'교과번호-분반': 'CLTR214001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '물리학 II', '구분': '전공기반', '수강정원': '130', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '제1과학관120', '개설대학': '자연과학대학', '개설\n학과': '물리학과', '개설\n전공': 'nan', '담당교수': '김도형', '팀티칭\n여부': 'Y', '스마트러닝\n강좌 여부': 'nan', '직급': '부교수', '교수소속\n대학': '자연과학대학', '교수소속\n학과': '물리학과', '강의\n언어': 'nan', '교과목명\n(영문)': 'Physics II', '학년': 'nan', '비고': 'nan', '수용정원': '130.0', '실시간정원': '70.0'}, {'교과번호-분반': 'CLTR215001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '화학 I', '구분': '전공기반', '수강정원': '120', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '화학관217', '개설대학': '자연과학대학', '개설\n학과': '화학과', '개설\n전공': 'nan', '담당교수': '이효선', '팀티칭\n여부': 'Y', '스마트러닝\n강좌 여부': 'nan', '직급': '교수', '교수소속\n대학': '자연과학대학', '교수소속\n학과': '화학과', '강의\n언어': 'nan', '교과목명\n(영문)': 'Chemistry I', '학년': 'nan', '비고': 'nan', '수용정원': '120.0', '실시간정원': '92.0'}, {'교과번호-분반': 'CLTR246001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '일반생명과학Ⅰ', '구분': '전공기반', '수강정원': '80', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '생명공학관(교양과정동)209', '개설대학': '자연과학대학', '개설\n학과': '생명과학부', '개설\n전공': '생물학전공', '담당교수': '최재신', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '강의초빙교수', '교수소속\n대학': '자연과학대학', '교수소속\n학과': '생명과학부', '강의\n언어': 'nan', '교과목명\n(영문)': 'Biological ScienceⅠ', '학년': 'nan', '비고': 'nan', '수용정원': '80.0', '실시간정원': '50.0'}, {'교과번호-분반': 'CLTR372001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '인공지능의 이해', '구분': '교양', '수강정원': '70', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': 'IT융복합관(IT융복합공학관)351', '개설대학': '교육개발본부', '개설\n학과': '소프트웨어교육센터', '개설\n전공': 'nan', '담당교수': '조규철', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '계약교수', '교수소속\n대학': '소프트웨어교육센터', '교수소속\n학과': 'nan', '강의\n언어': 'nan', '교과목명\n(영문)': 'Understanding of Artificial Intelligence', '학년': 'nan', '비고': 'nan', '수용정원': '70.0', '실시간정원': '64.0'}, {'교과번호-분반': 'CLTR504001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '동화의 세계', '구분': '교양', '수강정원': '450', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '정보전산원(전자계산소)117', '개설대학': '인문대학', '개설\n학과': '독어독문학과', '개설\n전공': 'nan', '담당교수': '김정철', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '교수', '교수소속\n대학': '인문대학', '교수소속\n학과': '독어독문학과', '강의\n언어': 'nan', '교과목명\n(영문)': 'World of Fairy Tales', '학년': 'nan', '비고': 'nan', '수용정원': '450.0', '실시간정원': '350.0'}, {'교과번호-분반': 'CLTR585001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '과학과 문화', '구분': '교양', '수강정원': '70', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '생명공학관(교양과정동)319', '개설대학': '자연과학대학', '개설\n학과': '생명과학부', '개설\n전공': '생명공학전공', '담당교수': '이원하', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '교수', '교수소속\n대학': '자연과학대학', '교수소속\n학과': '생명과학부', '강의\n언어': 'nan', '교과목명\n(영문)': 'The Science and Culture', '학년': 'nan', '비고': 'nan', '수용정원': '70.0', '실시간정원': '55.0'}, {'교과번호-분반': 'CLTR608001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '결혼준비 교육', '구분': '교양', '수강정원': '80', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '생활과학대학403', '개설대학': '생활과학대학', '개설\n학과': '아동학부', '개설\n전공': 'nan', '담당교수': '전귀연', '팀티칭\n여부': 'Y', '스마트러닝\n강좌 여부': 'nan', '직급': '교수', '교수소속\n대학': '생활과학대학', '교수소속\n학과': '아동학부', '강의\n언어': 'nan', '교과목명\n(영문)': 'Premarital Preparation Education', '학년': 'nan', '비고': 'nan', '수용정원': '80.0', '실시간정원': '32.0'}, {'교과번호-분반': 'CLTR635002', '학점': '3', '강의': '3', '실습': '0', '교과목명': '미술의 감상과 이해', '구분': '기본소양', '수강정원': '70', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '조형관(제3합동강의동)103', '개설대학': '예술대학', '개설\n학과': '미술학과', '개설\n전공': 'nan', '담당교수': '신영호', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '부교수', '교수소속\n대학': '예술대학', '교수소속\n학과': '미술학과', '강의\n언어': 'nan', '교과목명\n(영문)': 'The Appreciation and Comprehension of Art', '학년': 'nan', '비고': 'nan', '수용정원': '0.0', '실시간정원': '0.0'}, {'교과번호-분반': 'CLTR680001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '영화로 만나는 러시아와 동유럽 문화', '구분': '교양', '수강정원': '90', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '인문한국진흥관104', '개설대학': '인문대학', '개설\n학과': '노어노문학과', '개설\n전공': 'nan', '담당교수': '윤영순', '팀티칭\n여부': 'Y', '스마트러닝\n강좌 여부': 'nan', '직급': '부교수', '교수소속\n대학': '인문대학', '교수소속\n학과': '노어노문학과', '강의\n언어': 'nan', '교과목명\n(영문)': 'Russian & East European Culture in Films', '학년': 'nan', '비고': 'nan', '수용정원': '90.0', '실시간정원': '84.0'}, {'교과번호-분반': 'COME331001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '자료구조', '구분': '공학전공', '수강정원': '90', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': 'IT대학1호관(공대10호관)209', '개설대학': 'IT대학', '개설\n학과': '전자공학부', '개설\n전공': 'nan', '담당교수': '김종화', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '강의초빙교수', '교수소속\n대학': 'IT대학', '교수소속\n학과': '전자공학부', '강의\n언어': 'nan', '교과목명\n(영문)': 'Data Structure', '학년': 'nan', '비고': 'nan', '수용정원': '90.0', '실시간정원': '52.0'}, {'교과번호-분반': 'COMM323001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '인간커뮤니케이션', '구분': '전공', '수강정원': '300', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '사회과학대학101', '개설대학': '사회과학대학', '개설\n학과': '신문방송학과', '개설\n전공': 'nan', '담당교수': '정정주', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'Y', '직급': '부교수', '교수소속\n대학': '사회과학대학', '교수소속\n학과': '신문방송학과', '강의\n언어': 'nan', '교과목명\n(영문)': 'Human Communication', '학년': 'nan', '비고': 'nan', '수용정원': '300.0', '실시간정원': '67.0'}, {'교과번호-분반': 'COMP311001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '논리회로설계', '구분': '공학전공', '수강정원': '30', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': 'IT대학2호관(공대5호관)214', '개설대학': 'IT대학', '개설\n학과': '전자공학부', '개설\n전공': 'nan', '담당교수': '김찬용', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '강의초빙교수', '교수소속\n대학': 'IT대학', '교수소속\n학과': '전자공학부', '강의\n언어': 'nan', '교과목명\n(영문)': 'Logic Circuit Design', '학년': 'nan', '비고': 'nan', '수용정원': '45.0', '실시간정원': '42.0'}, {'교과번호-분반': 'COMP411001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '컴퓨터구조', '구분': '공학전공', '수강정원': '90', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': 'IT대학1호관(공대10호관)315', '개설대학': 'IT대학', '개설\n학과': '전자공학부', '개설\n전공': 'nan', '담당교수': '김지훈', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '강의초빙교수', '교수소속\n대학': 'IT대학', '교수소속\n학과': '전자공학부', '강의\n언어': 'nan', '교과목명\n(영문)': 'Computer Architectures', '학년': 'nan', '비고': 'nan', '수용정원': '90.0', '실시간정원': '41.0'}, {'교과번호-분반': 'ECON204001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '무역학원론', '구분': '전공', '수강정원': '200', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '경상대학319', '개설대학': '경상대학', '개설\n학과': '경제통상학부', '개설\n전공': 'nan', '담당교수': '김성룡', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'Y', '직급': '조교수', '교수소속\n대학': '경상대학', '교수소속\n학과': '경제통상학부', '강의\n언어': 'nan', '교과목명\n(영문)': 'Principle of International Trade', '학년': 'nan', '비고': 'nan', '수용정원': '200.0', '실시간정원': '59.0'}, {'교과번호-분반': 'ECON471001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '국제경제학', '구분': '전공필수', '수강정원': '80', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '경상대학315', '개설대학': '경상대학', '개설\n학과': '경제통상학부', '개설\n전공': 'nan', '담당교수': '김성민', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '강의초빙교수', '교수소속\n대학': '경상대학', '교수소속\n학과': '경제통상학부', '강의\n언어': 'nan', '교과목명\n(영문)': 'International Economics', '학년': 'nan', '비고': 'nan', '수용정원': '80.0', '실시간정원': '80.0'}, {'교과번호-분반': 'ECON645001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '경제통상통계학', '구분': '전공필수', '수강정원': '100', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '경상대학323', '개설대학': '경상대학', '개설\n학과': '경제통상학부', '개설\n전공': 'nan', '담당교수': '정기호', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'Y', '직급': '교수', '교수소속\n대학': '경상대학', '교수소속\n학과': '경제통상학부', '강의\n언어': 'nan', '교과목명\n(영문)': 'Statistics for Economics and Commercial Trade', '학년': 'nan', '비고': 'nan', '수용정원': '100.0', '실시간정원': '29.0'}, {'교과번호-분반': 'ELEC247001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '논리회로', '구분': '공학전공', '수강정원': '90', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': 'IT대학3호관(공대11호관)106', '개설대학': 'IT대학', '개설\n학과': '전자공학부', '개설\n전공': 'nan', '담당교수': '최두현', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '교수', '교수소속\n대학': 'IT대학', '교수소속\n학과': '전자공학부', '강의\n언어': 'nan', '교과목명\n(영문)': 'Logic Circuits', '학년': 'nan', '비고': 'nan', '수용정원': '90.0', '실시간정원': '72.0'}, {'교과번호-분반': 'ELEC311001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '물리전자', '구분': '공학전공', '수강정원': '90', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': 'IT대학3호관(공대11호관)111', '개설대학': 'IT대학', '개설\n학과': '전자공학부', '개설\n전공': 'nan', '담당교수': '신장규', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '교수', '교수소속\n대학': 'IT대학', '교수소속\n학과': '전자공학부', '강의\n언어': 'nan', '교과목명\n(영문)': 'Physical Electronics', '학년': 'nan', '비고': 'nan', '수용정원': '90.0', '실시간정원': '82.0'}, {'교과번호-분반': 'ENGL396001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '미국문학개관 1', '구분': '전공', '수강정원': '70', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '대학원동101', '개설대학': '인문대학', '개설\n학과': '영어영문학과', '개설\n전공': 'nan', '담당교수': '박연옥', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '교수', '교수소속\n대학': '인문대학', '교수소속\n학과': '영어영문학과', '강의\n언어': 'nan', '교과목명\n(영문)': 'Introduction to American Literature 1', '학년': 'nan', '비고': 'nan', '수용정원': '70.0', '실시간정원': '36.0'}, {'교과번호-분반': 'ITEC201001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '컴퓨터학개론', '구분': '공학전공', '수강정원': '80', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': 'IT대학4호관(제2학생회관)104', '개설대학': 'IT대학', '개설\n학과': '컴퓨터학부', '개설\n전공': 'nan', '담당교수': '김상욱', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '교수', '교수소속\n대학': 'IT대학', '교수소속\n학과': '컴퓨터학부', '강의\n언어': 'nan', '교과목명\n(영문)': 'Introduction to Computer Science and Engineering', '학년': 'nan', '비고': 'nan', '수용정원': '110.0', '실시간정원': '101.0'}, {'교과번호-분반': 'MGMT209001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '경영수학', '구분': '전공', '수강정원': '70', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '경상대학223', '개설대학': '경상대학', '개설\n학과': '경영학부', '개설\n전공': 'nan', '담당교수': '권준엽', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '조교수', '교수소속\n대학': '경상대학', '교수소속\n학과': '경영학부', '강의\n언어': 'nan', '교과목명\n(영문)': 'Mathematics for Business', '학년': 'nan', '비고': 'nan', '수용정원': '90.0', '실시간정원': '63.0'}, {'교과번호-분반': 'MGMT231001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '경영통계', '구분': '전공필수', '수강정원': '100', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '경상대학227', '개설대학': '경상대학', '개설\n학과': '경영학부', '개설\n전공': 'nan', '담당교수': '김성수', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'Y', '직급': '부교수', '교수소속\n대학': '경상대학', '교수소속\n학과': '경영학부', '강의\n언어': 'nan', '교과목명\n(영문)': 'Business Statistics', '학년': 'nan', '비고': 'nan', '수용정원': '140.0', '실시간정원': '122.0'}, {'교과번호-분반': 'PUAD251001', '학점': '3', '강의': '3', '실습': '0', '교과목명': '정책학', '구분': '전공필수', '수강정원': '70', '강의시간(요일,교시)': '월1A1B2A\n월2B3A3B\n화1A1B2A\n화2B3A3B\n수1A1B2A\n수2B3A3B\n금1A1B2A\n금2B3A3B', '강의실': '법과대학(법학전문대학원)101', '개설대학': '행정학부', '개설\n학과': '행정학부', '개설\n전공': 'nan', '담당교수': '진상현', '팀티칭\n여부': 'nan', '스마트러닝\n강좌 여부': 'nan', '직급': '부교수', '교수소속\n대학': '행정학부', '교수소속\n학과': 'nan', '강의\n언어': 'nan', '교과목명\n(영문)': 'Policy Sciences', '학년': 'nan', '비고': 'nan', '수용정원': '0.0', '실시간정원': '0.0'}]

#render dataframe as html
html = df_marks.to_html()

#write html to file
text_file = open("/Users/jawoos/SynologyDrive/Python_Projects/KNUS_HTML/startbootstrap-blog-post-gh-pages/table.html", "w", encoding="UTF8")
text_file.write(html)
text_file.close()
