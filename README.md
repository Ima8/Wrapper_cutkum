# Wrapper class of  Cutkum ['คัดคำ']
Cutkum ('คัดคำ') is a python code for Thai Word-Segmentation using Recurrent Neural Network (RNN) based on Tensorflow library. 

Cutkum is trained on BEST2010, a 5 Millions Thai words corpus by NECTEC (https://www.nectec.or.th/). It also comes with an already trained model, and can be used right out of the box. Cutkum is still a work-in-progress project. Evaluated on the 10% hold-out data from BEST2010 corpus (~600,000 words), the included trained model currently performs at 0.93 recall, 0.92 precision and 0.93 F-measure. 

# Requirements
* python >= 3.0
* tensorflow >= 1.1

# Usages
`main.py`
```
from cutkum2 import segment_text
segment_text('สวัสดีครับ')
```

For example, `main.py`


# Citations
Pucktada Treeratpituk. Thai Word-Segmentation with Deep Learning in Tensorflow.
https://github.com/pucktada/cutkum.
Accessed: [Insert date here]
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
