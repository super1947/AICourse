# touristResource.py
# 공공 기관 데이터 : 관광 자원 통계 서비스
'''
처리 순서
1. end_point 문자열을 생성
2. 일반 인증 키를 발급 받는다
3. 요청을 하기 위한 url 변수를 만든다.
'''
import requests
import urllib.parse, urllib.request, json, math, datetime
now = datetime.datetime.now()

def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            # print(f'URL 정보 : {url}')
            return response.read().decode('utf-8')
    except Exception as err:
        # print(err)
        print(f'오류 발생! 시각 : {now}, URL : {url}')
        return None

access_key = 'm%2FCdRL8aDJq%2Bj32H2FXkLhi5JoN5nqx5wo6y7Co9kRfVcjND8yNLqpl9ENJ7DJlcYK8luwaKiK4MjTvC9BYUwA%3D%3D'
access_key_decode = requests.utils.unquote(access_key)
print(access_key_decode)

def getTourData(yyyymm, sido, gungu, nPageNum, maxRecords):
    # end_point와 params를 이용하여 url을 생성
    # getRequestUrl() 함수를 이용하여 url 추출
    end_point = 'http://openapi.tour.go.kr/openapi/service'
    end_point += '/TourismResourceStatsService'
    end_point += '/getPchrgTrrsrtVisitorList'
    params = '?'
    params += '_type=json'
    params += '&serviceKey=' + access_key_decode
    params += '&YM=' + yyyymm
    params += '&SIDO=' + urllib.parse.quote(sido)
    params += '&GUNGU=' + urllib.parse.quote(gungu)
    params += '&RES_NM=' + ''
    params += '&pageNo=' + str(nPageNum)
    params += '&numOfRows=' + str(maxRecords)
    url = end_point + params
    result = getRequestUrl(url)

    if result == None:
        return None
    else:
        return json.loads(result)

def tourPointCorrection(item, yyyymm, jsonResult):
    # 전처리 : 해당 키가 존재하지 않는 경우, 기본 값으로 대체 데이터를 만들어 주는 함수
    addrCd = 0 if 'addrCd' not in item.keys() else item['addrCd']
    gungu = 0 if 'gungu' not in item.keys() else item['gungu']
    sido = 0 if 'sido' not in item.keys() else item['sido']
    resNm = 0 if 'resNm' not in item.keys() else item['resNm']
    rnum = 0 if 'rnum' not in item.keys() else item['rnum']
    ForNum = 0 if 'csForCnt' not in item.keys() else item['csForCnt']
    NatNum = 0 if 'csNatCnt' not in item.keys() else item['csNatCnt']

    jsonResult.append({'yyyymm': yyyymm, 'addrCd': addrCd, 'gungu':gungu, 'sido': sido, 'resNm': resNm, 'rnum': rnum, 'ForNum': ForNum, 'NatNum': NatNum})

def main():
    jsonResult = []
    sido = ''
    gungu = ''
    nStartYear = 2015 # 검색 시작 연도
    nEndYear = 2019 # 검색 종료 연도
    nPageNum = 1 # 페이지 번호
    maxRecords = 100 # 조회될 행의 최대 수

    for year in range(nStartYear, nEndYear+1):
        for month in range(1, 13):
            yyyymm = f'{str(year)}{str(month).zfill(2)}'

            while(True):
                jsonData = getTourData(yyyymm, sido, gungu, nPageNum, maxRecords)
                print(jsonData)

                # 응답 결과가 'ok'이면
                if jsonData['response']['header']['resultMsg'] == 'OK':
                    nTotal = jsonData['response']['body']['totalCount']
                    if nTotal == 0:
                        break
                    for item in jsonData['response']['body']['items']['item']:
                        tourPointCorrection(item, yyyymm, jsonResult)

                    nPage = math.ceil(nTotal / 100)
                    if(nPageNum == nPage):
                        break
                    nPageNum += 1
                else:
                    break
    # 파일 저장하기
    savedFilename = 'touristResource(%s %d~%d).json'
    with open(savedFilename % (sido, nStartYear, nEndYear), mode='w', encoding='utf-8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

if __name__ == '__main__':
    main()






