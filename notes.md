Some links to SOTA results in text classification: https://paperswithcode.com/task/text-classification

Word embeddings can be done using:
1.	Word2vec: https://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf 
a.	Continuous Bag-of-Words model - learn a word’s vector using its context (other words) as input
b.	the Skip-Gram model- learn word’s vector by trying to predict its context
2.	Glove: https://nlp.stanford.edu/pubs/glove.pdf
Count-based model, i.e. uses co-occurrence matrix 

ULMFiT: https://arxiv.org/pdf/1801.06146.pdf
1.	Pretrained AWD-LSTM model
2.	Fune-tuning

Bots and Gender Profiling problem can be framed as a multi-task classification problem: learn to predict both bot/not_bot and male/female classes at the same time.
http://ruder.io/multi-task/
Benefits on multi-task learning are: better predictive performance due to better regularization + lower cost of training (because only one model is trained)
The basic idea is that multiple tasks can share some fundamental features about instances of different classes in early layers of the neural network, and then learn task specific features in the later layers of the network.

Some ideas to try:
1.	Use https://fasttext.cc/  to establish baseline performance because it is simple a fast to train
2.	Find pretrained ULMFiT model and fune-tune it
3.	Try training a multi-task model


# Educational resources:
- Stanford's NLP course:
https://www.youtube.com/watch?v=OQQ-W_63UgQ&list=PL3FW7Lu3i5Jsnh1rnUwq_TcylNr7EkRe6