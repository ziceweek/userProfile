# coding:utf-8
import re

pat = re.compile(r'"(.*)"')

# just word without weight,different from the fun_2
def get_topic_words_in_str_1(topic_str):
    dict_of_a_topic = []
    items = topic_str.split('+')
    for word in items:
        result = pat.search(word)
        dict_of_a_topic.append(result.group(1))
    return dict_of_a_topic


# argue: a str describe a topic,generated by Gensim module.Like 1.000*"博" + 0.004*"图书馆" + 0.003*"大家" + 0.002*"话筒"
# return: a dict which take words as key,and list as value
def get_topic_words_in_str_2(topic_str):
    dict_of_a_topic = dict()
    items = topic_str.split('+')
    for word in items:
        print word
        result = pat.search(word)
        dict_of_a_topic[result.group(1)] = []

    return dict_of_a_topic


# sentence = '''
#     1.000*"博" + 0.004*"图书馆" + 0.003*"大家" + 0.002*"话筒" + 0.001*"书海" + 0.001*"宣传部" + 0.001*"官方" + 0.001*"黑龙江" + 0.001*"青青" + 0.001*"新浪"
#     -0.835*"图书馆" + -0.154*"读者" + -0.149*"网页" + -0.149*"链接" + -0.129*"讲座" + -0.126*"时间" + -0.126*"北校区" + -0.116*"南校区" + -0.115*"报告厅" + -0.107*"部门"
#     -0.476*"讲座" + 0.408*"图书馆" + -0.249*"资源" + -0.236*"数据库" + -0.227*"链接" + -0.226*"网页" + -0.200*"文献" + -0.137*"北校区" + -0.122*"老师" + -0.112*"论文"
#     -0.379*"女性" + -0.338*"沙龙" + -0.279*"世界" + -0.264*"嘉宾" + 0.261*"讲座" + -0.242*"水" + -0.171*"文化节" + -0.155*"主题" + -0.151*"罗茜" + -0.145*"教授"
#     -0.442*"读者" + -0.392*"部门" + -0.305*"学校" + 0.295*"讲座" + 0.205*"北校区" + -0.187*"图书" + 0.184*"图书馆" + -0.171*"时间" + 0.157*"报告厅" + -0.153*"法定"
#     -0.345*"女性" + -0.289*"讲座" + -0.278*"北校区" + 0.241*"链接" + 0.240*"网页" + 0.238*"数据库" + -0.173*"教授" + 0.157*"世界" + -0.151*"报告厅" + 0.146*"文化节"
#     '''
# dic = get_topic_words_in_str(sentence)
# for k in dic:
#    print k


