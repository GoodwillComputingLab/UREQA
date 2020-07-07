data = readtable('one_qubit_gate_error_rate.csv');
data = data(randperm(size(data, 1)), :);
data.OneQubitGateErrorRate = round(data.OneQubitGateErrorRate, 2);

trainData = data(1:6285,:);
testData = data(6286:6983,:);

cost = unique(trainData.OneQubitGateErrorRate);
cost = cost' - cost;
cost = abs(cost);