# 实验设计课程3.21课堂作业
# 18数据科学 孙易泽
# Stratified 抽样选取 Gender&Race & Workclass_result
# Systematic 抽样选取 Age&Edu_Level&Race_result

import matplotlib.pyplot as plt
import t_test

# 单样本均值假设检验
# 红线为p = 0.05 ，可以看出所有抽样方法大于0.05
p_srs = t_test.Model('./RESULT/srs_result.csv', '').ttest1()
p_cs = t_test.Model('./RESULT/cluster_result.csv', '').ttest1()
p_ss = t_test.Model('./RESULT/stratified_Gender&Race&Workclass_result.csv', '').ttest1()
p_uss = t_test.Model('./RESULT/systematic_Age&Edu_Level&Race_result.csv', '').ttest1()
p_oss = t_test.Model('./RESULT/systematic_None_result.csv', '').ttest1()
data1 = [p_srs, p_cs, p_ss, p_uss, p_oss]
data1_name = ['SRS', 'Cluster', 'Stratified', 'Systematic', 'Ordered']
plt.bar(range(len(data1)), data1, tick_label=data1_name, width=0.8)
plt.axhline(y=0.05, c="r", ls="--")
plt.xlabel('Sampling Methods')
plt.ylabel('p value')
plt.title('t-test of single sample')
plt.show()
print('单样本t检验 p值结果(保留5位小数)')
for i in range(5):
    print(data1_name[i], '=', data1[i])


# 双样本均值假设检验
# 红线为p = 0.05 ，可以看出均大于0.05， 为相同分布
srs_cs = t_test.Model('./RESULT/srs_result.csv', './RESULT/cluster_result.csv').ttest2()
srs_ss = t_test.Model('./RESULT/srs_result.csv', './RESULT/stratified_Gender&Race&Workclass_result.csv').ttest2()
srs_uss = t_test.Model('./RESULT/srs_result.csv', './RESULT/systematic_Age&Edu_Level&Race_result.csv').ttest2()
srs_oss = t_test.Model('./RESULT/srs_result.csv', './RESULT/systematic_None_result.csv').ttest2()
data2 = [srs_cs, srs_ss, srs_uss, srs_oss]
data2_name = ['SRS VS Cluster', 'SRS VS Stratified', 'SRS VS Systematic', 'SRS VS Ordered Systematic']
plt.bar(range(len(data2)), data2, tick_label=data2_name, width=0.8)
plt.axhline(y=0.05, c="r", ls="--")
plt.ylim(0.0, 0.8)
plt.xlabel('Comparison of Sampling Methods')
plt.ylabel('p value')
plt.xticks(rotation=10)
plt.title('t-test of double sample')
plt.show()
print('\n样本对比t检验 p值结果(保留5位小数)')
for i in range(4):
    print(data2_name[i], '=', data2[i])
