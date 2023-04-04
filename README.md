函数运行主入口为：**main.py**

由于平台对文件大小的限制，所以一次只能运行一个数据集。

需要跑那个数据集的话就把数据上传到**数据集**文件夹下。

同时修改main.py中**start**的值。比如要跑data_2776.csv文件，就设置**start=2776**。

在main.py的第625行writer_toExcel_qian50(final_sequences, start)，把当前结果保存到**result/文件夹下的result.xlsx**中，写入的sheet名为**data_start的值**。因此如果有同名sheet会报错，最好保证result.xlsx为空的excel。