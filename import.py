import ModulesForImport # 직접 정의한 module 을 import
import sys
import matplotlib.pyplot as plt

# 현재 디렉토리에서 모듈이나 패키지를 검색하도록 경로 추가
sys.path.append("./") 
ModulesForImport.piFunc("모듈 import")

fig = plt.figure(figsize=(10, 7))
plt.boxplot(([100, 23, 50, 93, 40], [19, 39, 29, 81, 10]))
plt.grid()
plt.show()