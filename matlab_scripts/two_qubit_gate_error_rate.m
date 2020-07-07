data = readtable('two_qubit_gate_error_rate.csv');
data = data(randperm(size(data, 1)), :);
data.TwoQubitGateErrorRate = round(data.TwoQubitGateErrorRate, 1);

trainData = data(1:1661,:);
testData = data(1662:1846,:);

cost = unique(trainData.TwoQubitGateErrorRate);
cost = cost' - cost;
cost = abs(cost);