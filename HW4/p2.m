% we consider only the first 2 records for now, to solve for m and b

x = [0 1];
y = [0.0434 1.0343];
e = [0.1 0.1];
% model matrix
A = [x.^0; x.^1];
% solve analytically for m and b (notes)
betahat = [0.9909, 0.566];

% we can find the other 3 errors by solving for e?
x = [2 3 4];
y = [-0.2588 3.68622 4.3188];
A = [x.^0; x.^1];
e345 = A'*betahat' - y';

% print out b, m, sigma
str = ['b = ', num2str(betahat(2)), ', m = ', num2str(betahat(1)), ', e3 through e5 = ', num2str(e345(1)), ', ', num2str(e345(2)), ', ', num2str(e345(3))];
disp(str)

% find the sigma of e

sigma = var([e12; e345]);

b_range = -10:1:10; % Range of a values
m_range = -10:1:10; % Range of b values

% an array for unnormalized posterior
posterior_unnorm = zeros(length(m_range), length(b_range));

for i = 1:length(m_range)
    for j = 1:length(b_range)
		% Likelihood
		likelihood = sum((y' - (A' * [m_range(i); b_range(j)])).^2) / (2 * sigma^2) - 5 * log(sigma);
		% Prior (assuming uniform prior for simplicity)
		prior = 1/sigma; % Uniform prior
		% Unnormalized posterior
		posterior_unnorm(i, j) = likelihood * prior;
       
    end
end

% proportionality constant
Z = trapz(b_range, trapz(m_range, posterior_unnorm, 1), 2);

% normalized posterior distribution
posterior = posterior_unnorm / Z;

% PDFs
pdf_b = trapz(m_range, posterior, 1);
pdf_m = trapz(b_range, posterior, 1);

mean_b = trapz(b_range, b_range .* pdf_b);
var_b = trapz(b_range, (b_range - mean_b).^2 .* pdf_b);
mean_m = trapz(m_range, m_range .* pdf_m);
var_m = trapz(m_range, (m_range - mean_m).^2 .* pdf_m);

% print out results
disp(['Mean of b: ', num2str(mean_b)]);
disp(['Variance of b: ', num2str(var_b)]);
disp(['Mean of m: ', num2str(mean_m)]);
disp(['Variance of m: ', num2str(var_m)]);
