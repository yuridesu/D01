#20微巴斯卡=0分貝，定義為v0；此式代表多少微巴斯卡=多少分貝
import numpy as np
print(20*np.log10(20000/20))
#分貝=20log10(微巴斯卡/20)
print((10**(30/20+np.log10(20)))/(10**(50/20+np.log10(20))))
