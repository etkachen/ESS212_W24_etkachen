y = [-2.73 -2.71 -2.65 -0.87 -3.10 -1.03 0.63 1.46 5.90 8.38];
t = [1:10];

A = [t.^0; t.^1; t.^2];
% least squares estimate of c, b and a
betahat = A/y; 
A = A';
%calculate the error
e = A*betahat - y';

% just calculate sigma from the derivative with respect to sigma of a logarithm of a posterior 
sigma = sqrt((0.25 * (e' * e))/11);
% huge sigma, is that right?

str = ['a = ', num2str(betahat(3)), ', b = ', num2str(betahat(2)), ', c = ', num2str(betahat(1)), ', sigma = ', num2str(sigma)];
disp(str)