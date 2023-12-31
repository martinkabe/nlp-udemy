inputs = [1, 2, 3, 4]
targets = [2, 4, 6, 8]
w = 0.1
learning_rate = 0.1


def predict(i):
    return w*i


if __name__ == '__main__':
    # train the network
    for _ in range(25):
        preds = [predict(i) for i in inputs]
        errors = [t - p for p, t in zip(preds, targets)]
        cost = sum(errors)/len(targets)
        print(f'Weight: {w:.2f}, Cost: {cost:.2f}')
        w += learning_rate * cost

    # test the network
    test_inputs = [5, 6]
    test_targets = [10, 12]
    pred = [predict(i) for i in test_inputs]
    for i, p, t in zip(test_inputs, pred, test_targets):
        print(f'input: {i}, target: {t}, pred: {p:.4f}')
