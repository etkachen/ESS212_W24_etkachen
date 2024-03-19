y = [[3.75 0.36 0.58 2.06]; [0.93 0.32 0.67 1.01]; [0.38 0.11 0.12 0.60]; [0.05 0.15 0.05 0.11]; [0.04 0.03 0.08 0.06]];
t = [1 2 3 4 5];

A = [[t t t t].^0; [t t t t].^1];
betahat = A/reshape(y,1,[]);

% e = y / exp(-bt)
% log e = bt + log(y), adheres to the Abeta - y format) 
% calculate log(e)
elog = A'*betahat + log(reshape(y,1,[]))';
% to get the value of e, we can just get the exponent of elog
e = exp(elog);
% the formula of the posterior probability: 1/sigma^11 exp (- (e'e)/(2*sigma^2))
% same logarithm as in problem 1, then?
sigma = sqrt((0.25 * (e' * e))/11);
% it's around 4.96, seems reasonable?

% print out b, m, sigma

