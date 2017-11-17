import math, copy

def Info_D(InfoList0):  # solve Info(D)  IN PAGE 217 of the book
    InfoList = copy.deepcopy(InfoList0)
    ResultDic = {}
    NumSample = len(InfoList) 
    result = 0
    for i in range(1,NumSample):
        if InfoList[i][-1] not in ResultDic:
            ResultDic[InfoList[i][-1]] = 0
        ResultDic[InfoList[i][-1]] += 1
    for key in ResultDic:
        result += -ResultDic[key]/(NumSample-1) * math.log(ResultDic[key]/(NumSample-1),2)
    return result
def Info_A_D(InfoList0, column):  # solve Info_A(D)  IN PAGE 218 of the book
    InfoList = copy.deepcopy(InfoList0)
    ColumnDic = {}
    ListPart = {}
    NumSample = len(InfoList)
    result = 0
    for i in range(1,NumSample):
        if InfoList[i][column] not in ColumnDic:
            ColumnDic[InfoList[i][column]] = 0
            ListPart[InfoList[i][column]] = [InfoList[0]]
        ColumnDic[InfoList[i][column]] += 1
        ListPart[InfoList[i][column]].append(InfoList[i])
    for key in ColumnDic:
        result += ColumnDic[key]/(NumSample-1) * Info_D(ListPart[key])
    return result

def Split(InfoDict1):  # one matrix splits to two accroding to information gain
    InfoDict0 = copy.deepcopy(InfoDict1)
    keys = list(InfoDict0)
    InfoList0 = InfoDict0[keys[0]]
    NumInfo = len(InfoList0[0]) - 2
    OtherInfoDic = {}
    for i in range(1, NumInfo+1):
        OtherInfoDic[i] = Info_A_D(InfoList0, i)
    minValueInOtherInfo = OtherInfoDic[1]
    minCol = 1
    for key in OtherInfoDic:
        if(OtherInfoDic[key] < minValueInOtherInfo):
            minValueInOtherInfo = OtherInfoDic[key]
            minCol = key
    ReturnDic = {}
    Title = InfoList0[0][minCol]
    InfoList0[0].remove(Title)
    for i in range(1,len(InfoList0)):
        valuep = InfoList0[i][minCol]
        if Title + ':' + valuep not in ReturnDic:
            ReturnDic[Title + ':' + valuep] = [InfoList0[0]]
        InfoList0[i].remove(valuep)
        ReturnDic[Title + ':' + valuep].append(InfoList0[i])
    return ReturnDic

def Split_recursion(InfoList0):  # use recursion method to bulid decision tree
    judgeDic = Split(InfoList0)
    InfoListRe = judgeDic
    for key in judgeDic:
        result = judgeDic[key][1][-1]
        for i in range(1,len(judgeDic[key])):
            if(judgeDic[key][i][-1] != result):
                RecurDic = {key:judgeDic[key]}
                InfoListRe[key] = Split_recursion(RecurDic)
                break
        if(i == len(judgeDic[key])-1):
            InfoListRe[key] = [result]
    return InfoListRe

def DeciTree(InfoList1):
    Root = {'Root':InfoList1}
    print(Split_recursion(Root))