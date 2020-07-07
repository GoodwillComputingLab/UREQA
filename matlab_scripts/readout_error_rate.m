data = readtable('readout_error_rate.csv');
data = data(randperm(size(data, 1)), :);
data.ReadoutErrorRate = round(data.ReadoutErrorRate, 1);

trainData = data(1:4049,:);
testData = data(4050:4499,:);

cost = unique(trainData.ReadoutErrorRate);
cost = cost' - cost;
cost = abs(cost);