# Cantonese Word Segmentation Comparison
We use the segeval library to calculate Precision, Recall, F1, and Accuracy of various Cantonese segmenters on the HKCanCor and CityU word segmentation corpora.

## Results
### HKCanCor (16,162 sentences / 153,992 characters)
|Segmenter   | Precision | Recall | F1    | Accuracy |
|------------|-----------|--------|-------|----------|
|Pycantonese | 93.04     | 87.48  | 90.18 |  94.77   |
|Cantoseg    | 92.63     | 86.81  | 89.63 |  94.53   |
|CyberCan-LTR| 83.14     | 76.26  | 79.55 |  89.14   |
|CyberCan-RTL| 83.06     | 76.19  | 79.48 |  89.09   |

### CityU (53,019 sentences / 1,456,208 characters)
|Segmenter   | Precision | Recall | F1    | Accuracy |
|------------|-----------|--------|-------|----------|
|Pycantonese | 79.44     | 83.42  | 81.38 |  90.75   |
|Cantoseg    | 85.58     | 82.24  | 83.88 |  92.78   |
|CyberCan-LTR| 79.64     | 81.46  | 80.54 |  90.43   |
|CyberCan-RTL| 79.97     | 81.78  | 80.87 |  90.67   |

## Raw Results

```
Pycantonese
=== data/finetune_hkcancor.json performance ===
{'_': {'precision': 0.930427875815865, 'recall': 0.8747986908410826, 'f1': 0.9017561592759819, 'number': 153992}, 'overall_precision': 0.930427875815865, 'overall_recall': 0.8747986908410826, 'overall_f1': 0.9017561592759819, 'overall_accuracy': 0.9476581289826684}
=== data/finetune_cityu.json performance ===
{'_': {'precision': 0.7944436742039783, 'recall': 0.8342125575467241, 'f1': 0.813842573238576, 'number': 1456208}, 'overall_precision': 0.7944436742039783, 'overall_recall': 0.8342125575467241, 'overall_f1': 0.813842573238576, 'overall_accuracy': 0.9074799890512801}

Cantoseg
=== data/finetune_hkcancor.json performance ===
{'_': {'precision': 0.9263396414687723, 'recall': 0.8681035378461219, 'f1': 0.8962766046603622, 'number': 153992}, 'overall_precision': 0.9263396414687723, 'overall_recall': 0.8681035378461219, 'overall_f1': 0.8962766046603622, 'overall_accuracy': 0.9453274156356153}
=== data/finetune_cityu.json performance ===
{'_': {'precision': 0.8558331862318752, 'recall': 0.8223646621911156, 'f1': 0.8387651905869052, 'number': 1456208}, 'overall_precision': 0.8558331862318752, 'overall_recall': 0.8223646621911156, 'overall_f1': 0.8387651905869052, 'overall_accuracy': 0.9277729754643846}

CyberCan-LTR
=== data/finetune_hkcancor.json performance ===
{'_': {'precision': 0.831404034182225, 'recall': 0.7625720816665801, 'f1': 0.7955018883262486, 'number': 153992}, 'overall_precision': 0.831404034182225, 'overall_recall': 0.7625720816665801, 'overall_f1': 0.7955018883262486, 'overall_accuracy': 0.8913639632044829}
=== data/finetune_cityu.json performance ===
{'_': {'precision': 0.7963653549354226, 'recall': 0.8146315636227791, 'f1': 0.8053949040283223, 'number': 1456208}, 'overall_precision': 0.7963653549354226, 'overall_recall': 0.8146315636227791, 'overall_f1': 0.8053949040283223, 'overall_accuracy': 0.9042656745151905}

CyberCan-RTL
=== data/finetune_hkcancor.json performance ===
{'_': {'precision': 0.8305877855570265, 'recall': 0.7619097095953037, 'f1': 0.7947678415991818, 'number': 153992}, 'overall_precision': 0.8305877855570265, 'overall_recall': 0.7619097095953037, 'overall_f1': 0.7947678415991818, 'overall_accuracy': 0.8908779846767995}
=== data/finetune_cityu.json performance ===
{'_': {'precision': 0.7997499199193082, 'recall': 0.8178268489116939, 'f1': 0.8086873767328697, 'number': 1456208}, 'overall_precision': 0.7997499199193082, 'overall_recall': 0.8178268489116939, 'overall_f1': 0.8086873767328697, 'overall_accuracy': 0.9067382881559977}
```