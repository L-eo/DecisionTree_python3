# the list0's title: RID, age, income, student, credit_rating, Class: buys_computer
title = ['RID',' age', 'income', 'student', 'credit_rating', 'Class: buys_computer']
list0 = [title,
         [1,'youth','high','no','fair','no'],
         [2,'youth','high','no','excellent','no'],
         [3,'middle_aged','high','no','fair','yes'],
         [4,'senior','medium','no','fair','yes'],
         [5,'senior','low','yes','fair','yes'],
         [6,'senior','low','yes','excellent','no'],
         [7,'middle_aged','low','yes','excellent','yes'],
         [8,'youth','medium','no','fair','no'],
         [9,'youth','low','yes','fair','yes'],
         [10,'senior','medium','yes','fair','yes'],
         [11,'youth','medium','yes','excellent','yes'],
         [12,'middle_aged','medium','no','excellent','yes'],
         [13,'middle_aged','high','yes','fair','yes'],
         [14,'senior','medium','no','excellent','no'],]

import DecisionTree as D
D.DeciTree(list0)