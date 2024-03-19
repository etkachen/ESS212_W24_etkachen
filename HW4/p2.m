% we consider only the first 2 records for now, to solve for m and b

x = [0 1];
y = [0.0434 1.0343];
e = [0.1 0.1];
% model matrix
A = [x.^0; x.^1];
betahat = A/y; 
% does it adhere to the given errors?
e12 = A'*betahat - y';
% it does!

% we can find the other 3 errors by solving for e?
x = [2 3 4];
y = [-0.2588 3.68622 4.3188];
A = [x.^0; x.^1];
e345 = A'*betahat - y';

% print out b, m, sigma
str = ['b = ', num2str(betahat(2)), ', m = ', num2str(betahat(1)), ', e3 through e5 = ', num2str(e345(1)), ', ', num2str(e345(2)), ', ', num2str(e345(3))];
disp(str)