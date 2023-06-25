# Graduation-project
Different components forming the grad project


#1 getting sensor data folder contains the src code of an android studio application developed with java to gather the required accelerometer and gyroscope data





#2 drag me custome hook folder contains the source code of a react typescript interface containing draggable components





#3 the rest of the files are the some different components used such as variety of different deep neural network mdoels.





Deep Neural Networks for Human Activity Recognition (HAR)
Introduction
Human Activity Recognition (HAR) is a field of study that aims to automatically identify and classify human activities based on sensor data, such as accelerometer and gyroscope readings. Deep Neural Networks (DNNs) have emerged as powerful tools for HAR, offering the ability to extract intricate patterns and representations from sensor data. In this README file, we will explore the usage of various DNN architectures, including CNN+LSTM, LSTM, GRU, and CNN+GRU, for HAR applications.

CNN+LSTM
The CNN+LSTM architecture combines Convolutional Neural Networks (CNNs) with Long Short-Term Memory (LSTM) networks. The CNN component extracts spatial features from input sensor data, such as time-series accelerometer readings. These features are then fed into the LSTM network, which captures temporal dependencies and learns sequential patterns. This architecture has shown excellent performance in HAR tasks by effectively learning both spatial and temporal representations.

LSTM
Long Short-Term Memory (LSTM) networks are a type of recurrent neural network (RNN) that excel at modeling sequential data. LSTM networks are designed to overcome the vanishing gradient problem and can capture long-term dependencies in time-series data. In HAR applications, LSTM networks can effectively learn temporal patterns from sensor data and make accurate predictions based on the historical context.

GRU
Gated Recurrent Units (GRUs) are another type of recurrent neural network that shares similarities with LSTM networks. GRUs have gating mechanisms that regulate the flow of information through the network, enabling them to capture dependencies over long sequences. GRUs are computationally efficient and can be used in HAR applications to capture temporal patterns and classify human activities.

CNN+GRU
The CNN+GRU architecture combines the power of CNNs in capturing spatial features with the GRU's ability to model sequential dependencies. The CNN component extracts meaningful spatial representations from sensor data, and the GRU network processes these representations in a sequential manner, capturing temporal patterns. This architecture has demonstrated strong performance in HAR tasks by effectively leveraging both spatial and temporal information.

BiLSTM
Bidirectional LSTM (BiLSTM) networks are an extension of LSTM networks that process input sequences in both forward and backward directions. By considering the past and future context of each time step, BiLSTMs capture a more comprehensive understanding of temporal dependencies. In HAR applications, BiLSTMs can effectively model the sequential nature of sensor data and make accurate activity predictions.

Conclusion
Deep Neural Networks have revolutionized the field of Human Activity Recognition by enabling accurate and robust activity classification based on sensor data. In this README file, we have explored several DNN architectures commonly used in HAR applications, including CNN+LSTM, LSTM, GRU, CNN+GRU, and BiLSTM. These architectures leverage the power of neural networks to learn spatial and temporal representations from sensor data, leading to improved activity recognition performance. Researchers and practitioners can experiment with these architectures to build robust HAR systems and contribute to advancements in this exciting field.
