y = [[3.75 0.36 0.58 2.06]; [0.93 0.32 0.67 1.01]; [0.38 0.11 0.12 0.60]; [0.05 0.15 0.05 0.11]; [0.04 0.03 0.08 0.06]];
t = [1 2 3 4 5];

A = [[t t t t].^0; [t t t t].^1];
A = A';
betahat = (A' * A) \ (A' * (reshape(y,1,[]))'); 

% e = y / exp(-bt)
% log e = bt + log(y), adheres to the Abeta - y format) 
% calculate log(e)
elog = A*betahat + log(reshape(y,1,[]))';
% to get the value of e, we can just get the exponent of elog
e = exp(elog);
% the formula of the posterior probability: 1/sigma^11 exp (- (e'e)/(2*sigma^2))
% same logarithm as in problem 1, then?
sigma = sqrt((0.25 * (e' * e))/11);
% it's around 4.96, seems reasonable?

% print out b, m, sigma
str = ['b = ', num2str(betahat(2)), ', m = ', num2str(betahat(1)), ', sigma = ', num2str(sigma)];
disp(str)

% 3D mesh
b_range = -10:1:10; % Range of a values
m_range = -10:1:10; % Range of b values
sigma_range = 1:1:10; % Range of sigma values

% an array for unnormalized posterior
posterior_unnorm = zeros(length(m_range), length(b_range), length(sigma_range));

for i = 1:length(m_range)
    for j = 1:length(b_range)
		for k = 1:length(sigma_range)
			% Likelihood
			% likelihood = exp(-0.5 * sum((y - (A * [1; a_range(i); b_range(j)])).^2) / sigma_range(k)^2);
			likelihood = sum(((reshape(y,1,[]))' - (A * [m_range(i); b_range(j)])).^2) / (2 * sigma_range(k)^2) - 10 * log(sigma_range(k));
			% Prior (assuming uniform prior for simplicity)
			prior = 1/sigma; % Uniform prior
			% Unnormalized posterior
			posterior_unnorm(i, j, k) = likelihood * prior;
		end
       
    end
end

% proportionality constant
Z = trapz(sigma_range, trapz(b_range, trapz(m_range, posterior_unnorm, 1), 2), 3);

% normalized posterior distribution
posterior = posterior_unnorm / Z;

% PDFs
pdf_b = trapz(sigma_range, trapz(m_range, posterior, 1), 3);
pdf_m = trapz(sigma_range, trapz(b_range, posterior, 2), 3);
pdf_m = pdf_m';
pdf_sigma = trapz(m_range, trapz(b_range, posterior, 1), 2);
pdf_sigma = (squeeze(pdf_sigma))';

mean_b = trapz(b_range, b_range .* pdf_b);
var_b = trapz(b_range, (b_range - mean_b).^2 .* pdf_b);
mean_m = trapz(m_range, m_range .* pdf_m);
var_m = trapz(m_range, (m_range - mean_m).^2 .* pdf_m);
mean_sigma = trapz(sigma_range, sigma_range .* pdf_sigma);
var_sigma = trapz(sigma_range, (sigma_range - mean_sigma).^2 .* pdf_sigma);
std_dev_sigma = sqrt(var_sigma);

% print out results
disp(['Mean of b: ', num2str(mean_b)]);
disp(['Variance of b: ', num2str(var_b)]);
disp(['Mean of m: ', num2str(mean_m)]);
disp(['Variance of m: ', num2str(var_m)]);
disp(['Mean of sigma: ', num2str(mean_sigma)]);
disp(['Standard deviation of sigma: ', num2str(std_dev_sigma)]);