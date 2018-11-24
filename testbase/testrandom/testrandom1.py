'''
@Author: Baiy
@Date: 2018-11-16 20:46:57
@LastEditors: Baiy
@LastEditTime: 2018-11-16 20:49:11
@Email: yang01.bai@horizon.ai
@Company: Horizon Hobot
@Description: 
'''
"""
例子：地理老师为了考核班里的20个学生，中国34个省的省会城市是什么。
但为了防止学生作弊，每份试卷的题目顺序不一样，答案也不一样。
因此需要写一个程序创建20份试卷，每份试卷创建34个多重选择题，次序随机。
为每个题提供一个正确答案和3个随机的错误答案。试卷写进20个文本文件，每份试卷的答案也写进20个文本文件。
"""

import random
capital_city_string = "北京市--北京 ；上海市 --上海 ；天津市 --天津 ；重庆市 --重庆 ；" \
                    "黑龙江省 --哈尔滨 ；吉林省 --长春； 辽宁省 --沈阳 ；内蒙古自治区--呼和浩特 ；" \
                     "河北省 --石家庄 ；新疆维吾尔自治区--乌鲁木齐 ；甘肃省-- 兰州 ；青海省--西宁 ；" \
                     "陕西省 --西安 ；宁夏回族自治区--银川 ；河南省-- 郑州 ；山东省--济南 ；" \
                    "山西省--太原 ；安徽省--合肥 ；湖南省--长沙；湖北省--武汉 ；江苏省--南京 ；" \
                     "四川省--成都； 贵州省--贵阳 ；云南省--昆明 ；广西壮族自治区--南宁 ；" \
                    "西藏自治区-- 拉萨 ；浙江省--杭州； 江西省--南昌 ；广东省--广州 ；福建省--福州 ；" \
                    "台湾省--台北 ；海南省 --海口 ；香港特别行政区-- 香港； 澳门特别行政区-- 澳门"

grade = {0: "A", 1: "B", 2: "C", 3: "D"}  # 设置答案等级



def get_dict(city_string):  # 将省会和省会城市的字符串转变成一个字典格式
    province_and_capital_dict = {}
    city_list = city_string.split("；")
    for city_index in city_list:
        province_and_capital_list = city_index.split("--")
        province_and_capital_dict[province_and_capital_list[0]] = province_and_capital_list[1]
    return province_and_capital_dict


def make_test_paper(province_and_capital_dict):
    for i in range(20):
        f_test = open("E:\\test" + str(i + 1) + ".txt", "w+")  # 创建试卷文件
        f_answer = open("E:\\answer" + str(i + 1) + ".txt", "w+")  # 创建试卷答案文件
        f_test.write("Name:\n")  # 试卷前需要学生填写自己的姓名
        f_test.write("Score:\n\n")  # 试卷的得分
        province_and_capital_dictkeys = list(province_and_capital_dict.keys())  # 获得34省列表
        random.shuffle(province_and_capital_dictkeys)  # 随机打乱34省列表的顺序
        for i in range(34):  # 循环创建34个题目
            # 将问题写入文件
            f_test.write(str(i+1)+","+"what's the capital of " + province_and_capital_dictkeys[i]+"?\n")
            correct_answer = province_and_capital_dict[province_and_capital_dictkeys[i]]  # 问题的正确答案
            error_answer = list(province_and_capital_dict.values())  # 所有的答案
            error_answer.remove(correct_answer)  # 在所有答案中移除正确的那个答案，得到错误答案的列表
            random.shuffle(error_answer)  # 随机打乱错误答案
            answer = random.sample(error_answer, 3)  # 在错误答案列表中随机选择3个错误答案
            answer.append(correct_answer)  # 将正确答案添加到答案列表中
            random.shuffle(answer)  # 再打乱4个答案的顺序
            f_test.write("\n"+grade[0]+answer[0]+"\n"+grade[1]+answer[1]+"\n"+grade[2]+answer[2]+"\n"+grade[3] +
                         answer[3] + "\n\n")  # 得到A、B、C、D四个答案，并写入到文件中
            answer_grade = ""
            for answer_index in answer:
                if answer_index == correct_answer:
                    index = answer.index(answer_index)
                    answer_grade = grade[index]  # 得到正确答案的等级（A、B、C、D）
            f_answer.write(str(i+1)+","+answer_grade+correct_answer)  # 最后将答案写入试卷答案文件
        f_test.close()
        f_answer.close()

#调用两个方法
if __name__ == "__main__":
    province_and_capital_dict = get_dict(capital_city_string)
    print(province_and_capital_dict)
    make_test_paper(province_and_capital_dict)