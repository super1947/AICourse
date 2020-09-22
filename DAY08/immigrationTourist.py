# immigrationTourist.py
# 출입국 관광 통계 서비스
import urllib.parse, urllib.request, json
# import matplotlib.pyplot as plt
#
# plt.rc('font', family='Malgun Gothic')

def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            return response.read().decode('utf-8')
    except Exception as err:
        print(err)
        print(f'오류 발생! URL : {url}')
        return None

access_key = 'la0oJ36Ys9xVH5HrvdWF4NGxbtE%2FJx08%2F6aALNmroSOk%2BHsxlk3EH9qkY5pGRngEaryWrlXLGkZLU%2B1r6Mp0dg%3D%3D'
def getNatVisitor(ym, nat_cd, ed_cd):
    end_point = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService'
    end_point += '/getEdrcntTourismStatsList'

    params = '?_type=json&serviceKey=' + access_key
    params += '&YM=' + ym
    params += '&NAT_CD=' + nat_cd
    params += '&ED_CD=' + ed_cd

    url = end_point + params
    # print(url)
    retData = getRequestUrl(url)
    if retData == None:
        return None
    else:
        return json.loads(retData)

def main():
    jsonResult = []
    nation = '중국'
    nat_cd = '112'
    ed_cd = 'E'

    nStartYear = 2015  # 검색 시작 연도
    nEndYear = 2019  # 검색 종료 연도

    for year in range(nStartYear, nEndYear+1):
        for month in range(1, 13):
            ym = f'{str(year)}{str(month).zfill(2)}'
            jsonData = getNatVisitor(ym, nat_cd, ed_cd)
            print(jsonData)
            if jsonData['response']['header']['resultMsg'] == 'OK':
                krname = jsonData['response']['body']['items']['item']['natKorNm'].replace(' ', '')
                iTotalVisit = jsonData['response']['body']['items']['item']['num']
                # print('%s_%s : %s' % (krname, ym, iTotalVisit))
                jsonResult.append({'nat_name': krname, 'nat_cd': nat_cd, 'yyyymm': ym, 'visit_cnt': iTotalVisit})

    savedFilename = f'immigrationTourist {nation}({nat_cd})_({nStartYear}~{nEndYear}).json'
    with open(savedFilename, mode='w', encoding='utf-8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

        # # 그래프 그리기
        # cnVisit = []  # 방문자 수
        # visitYM = []  # 방문한 년월
        # index = []
        # i = 0
        #
        # for item in jsonResult:
        #     index.append(i)
        #     cnVisit.append(item['visit_cnt'])
        #     visitYM.append(item['yyyymm'])
        #     i = i + 1
        #
        # plt.xticks(index, visitYM)
        # plt.plot(index, cnVisit)
        # plt.xlabel('방문월')
        # plt.ylabel('방문객수')
        # plt.show()

if __name__ == '__main__':
    main()