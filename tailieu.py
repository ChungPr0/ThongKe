import pandas as pd
import scipy.stats as st
import statsmodels
import statsmodels.api
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.stats.proportion import proportion_confint, proportions_ztest
from scipy.stats import ttest_1samp, ttest_ind, ttest_rel

data = pd.read_csv('D:/Code/A48030/nnlt/python/XSTT/Hostel.csv')


print(data.head())

# Lập bảng tần số cho biến giới tính
print(sv['GioiTinh'].value_counts())
sv.TheThao.value_counts(normalize = True)
# đặt normalize = True để tính tần suất

# Lập bảng tần số chéo
pd.crosstab(sv.GioiTinh,sv.TheThao)
pd.crosstab(sv.TheThao,sv.GioiTinh,margins=True)
# đặt margins=True để tính tổng cột và tổng hàng

ptTuoi=pd.cut(sl.Tuoi,bins=[20, 30, 40, 50, 60, 70, 80],
              include_lowest=True)
# bins: các điểm chia
# include_lowest = True: làm cận dưới của tổ đầu tiên giảm đi
# một ít (để chứa cả giá trị 20)
# tính tỉ lệ những người được điều tra có độ tuổi không vượt quá 50.
ptTuoi.value_counts(sort = False, normalize = True).cumsum()
# sort = False để xếp các tổ theo chiều tăng của dữ liệu,
# ngược lại theo chiều giảm của tần số (tần suất)
# cumsum để tính tần suất tích lũy

dthi['DiemThi'].mean() # Tính mean (trung bình cộng)
dthi['DiemThi'].median() # tính trung vị
dthi['DiemThi'].quantile([0.25, 0.5, 0.75])   #Tính các tứ phân vị
dthi['DiemThi'].quantile([0.1, 0.6, 0.9]) # tính phân vị thứ 10, 60 và 90
max(dthi.DiemThi)-min(dthi.DiemThi) # tính khoảng biến thiên
dthi['DiemThi'].var() # tính phương sai
dthi['DiemThi'].std() # tính độ lệch chuẩn

plt.boxplot(DT['DiemThi']) # Vẽ biểu đồ hộp và râu dạng đứng
plt.boxplot(DT['DiemThi'],vert=False) # Vẽ biểu đồ hộp và râu dạng nằm ngang
plt.show()

# nhãn của các thanh
TL=np.array(['R&B','Rock','Rap','Country','Classical','Latin']) 
# cao độ của các thanh (tần số của các biểu hiện)
SL=np.array([146.4, 102.6, 73.7,64.5, 14.8, 14.5])
# màu của các thanh, có thể 1 hoặc nhiều màu tùy ý
col=['blue', 'yellow']
# lệnh vẽ biểu đồ thanh
plt.bar(TL,SL,color = col)
plt.show()
# Biểu đồ tròn
plt.pie(SL, labels=TL) # SL và TL được nhập số liệu ở bên trên
plt.show()

# Đưa ra khoảng tin cậy 80% trọng lượng của các con chuột
mau=np.array([21, 23, 27, 19, 17, 18, 20, 15, 17, 22]) # nhập dữ liệu
kiemdinh = st.ttest_1samp(mau, popmean=0) #Lệnh thực hiện bài toán kiểm định (sẽ học chi tiết sau)
kiemdinh.confidence_interval(confidence_level=0.8) #dùng method confidence_interval
# để tìm ước lượng khoảng cho trung bình từ kết quả của bài toán kiểm định

# Tìm khoảng ước lượng 99% cho tỷ lệ sinh con trai của Việt Nam năm 2020
statsmodels.stats.proportion.proportion_confint(count=625,
                   nobs = 1200, alpha=0.01)
# count: số quan sát thành công (trong trường hợp này là số con trai)
# nobs: cỡ mẫu
# alpha = 1 - độ tin cậy (trong trường hợp này là 1 - 0.99 = 0.01)


#kiểm định 1 trung bình
print(ttest_1samp(data[data.City == 'Tokyo']['summary.score'], popmean=1.78, alternative='two-sided')) #less, greater, nan_policy = 'omit'

#kiểm định 1 tỷ lệ
print(proportions_ztest(count=100, nobs= 250, value=0.06, alternative='two-sided')) #smaler, larger

#kiểm định 2 trung bình
print(ttest_ind(vtm.DungC, vtm.KhongC, nan_policy='omit', alternative='less', equal_var=False )) # equal_var=False phương sai khác nhau

#kiểm định 2 tỷ lệ
print(proportions_ztest(count=[26, 10], nobs=[42, 20], alternative='larger'))

