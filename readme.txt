403410062 郭晏誌 HW2
On Mac OS Sierra 10.12.3 / Docker (Caffe image)

I got some problems on this homework so I turn to my Friend 黃鈺程 for some technical support.

Below is how I finish this task.

1. Use Create_lmdb.py to create dataset.

2. Use Create_train_test_prototext.py to create Train_test.prototxt and I duplicate it for 3 copies and change the number of num_output in FullConnect Layer as 1 / 10 / 50.

3.Create 3 solver.prototxt for Train_test.prototext 1 / 10 / 50.

4.In 3 Learning_Curve.ipnb I will implement all 3 types of setting and draw their own ACC/LOSS Graph.

*** To see the Curve and result or my whole work ***
https://github.com/macaca50507/ML/blob/master/Learning_Curve1.ipynb
https://github.com/macaca50507/ML/blob/master/Learning_Curve2.ipynb
https://github.com/macaca50507/ML/blob/master/Learning_Curve3.ipynb
