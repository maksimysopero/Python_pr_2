                                      # Кодирование меток

import numpy as np
from sklearn import preprocessing

input_labels = ['red','black','red','green','black','yellow','white'] #Этикетки  напечатаны следующим образом

encoder = preprocessing.LabelEncoder() 

print(encoder.fit(input_labels)) 

test_labels = ['green','red','black'] #Этот шаг можно использовать для проверки производительности путем кодирования
# случайного упорядоченного списка.
encoded_values = encoder.transform(test_labels) 
print("\nLabels =", test_labels)

print("Encoded values =", list(encoded_values))


encoded_values = [3,0,4,1]#Проверка производительности путем декодирования случайного набора
#чисел 
decoded_list = encoder.inverse_transform(encoded_values) 
print("\nEncoded values =", encoded_values)

print("Decoded labels =", list(decoded_list))
