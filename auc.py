def auc_py(labels, preds):
    # 提取正负例的索引
    pos_idx = [i for i in range(len(labels)) if labels[i] == 1]
    neg_idx = [i for i in range(len(labels)) if labels[i] == 0]
    auc_sum = 0
    for i in pos_idx:
        for j in neg_idx:
            if preds[i] > preds[j]:
                auc_sum += 0.5
            elif preds[i] == preds[j]:
                auc_sum += 0.5
    return auc_sum / len(preds)

if __name__ == '__main__':
    label = [1,0,0,0,1,0,1,0]
    pre = [0.9, 0.8, 0.3, 0.1, 0.4, 0.9, 0.66, 0.7]
    from sklearn.metrics import roc_curve, auc
    fpr, tpr, th = roc_curve(label, pre , pos_label=1)

    print('auc_py', auc_py(label, pre))
    print('sklearn', auc(fpr, tpr))
    '''
    auc_py 0.5625
    sklearn 0.5666666666666667
    '''