y = [-2.73; -2.71; -2.65; -0.87; -3.10; -1.03; 0.63; 1.46; 5.90; 8.38];
t = (1:10)';

A = [t.^0, t.^1, t.^2];

% least squares estimate of c, b and a
betahat = (A' * A) \ (A' * y); 
e = A * betahat - y; 

% just calculate sigma from the derivative with respect to sigma of a logarithm of a posterior 
sigma = sqrt((0.25 * (e' * e)) / 11);

% print out initial guess
str = ['a = ', num2str(betahat(3)), ', b = ', num2str(betahat(2)), ', c = ', num2str(betahat(1)), ', sigma = ', num2str(sigma)];
disp(str)

% 4D mesh
a_range = -10:1:10; % Range of a values
b_range = -10:1:10; % Range of b values
c_range = -10:1:10; % Range of c values
sigma_range = 1:1:10; % Range of sigma values

% an array for unnormalized posterior
posterior_unnorm = zeros(length(c_range), length(b_range), length(a_range), length(sigma_range));

for i = 1:length(c_range)
    for j = 1:length(b_range)
        for k = 1:length(a_range)
			for l = 1:length(sigma_range)
				% Likelihood
				% likelihood = exp(-0.5 * sum((y - (A * [1; a_range(i); b_range(j)])).^2) / sigma_range(k)^2);
				likelihood = sum((y - (A * [c_range(i); b_range(j); a_range(k)])).^2) / (2 * sigma_range(l)^2) - 10 * log(sigma_range(l));
				% Prior (assuming uniform prior for simplicity)
				prior = 1/sigma; % Uniform prior
				% Unnormalized posterior
				posterior_unnorm(i, j, k, l) = likelihood * prior;
			end
       end
    end
end

% proportionality constant
Z = trapz(sigma_range, trapz(a_range, trapz(b_range, trapz(c_range, posterior_unnorm, 1), 2), 3), 4);

% normalized posterior distribution
posterior = posterior_unnorm / Z;

% PDFs
pdf_a = trapz(sigma_range, trapz(b_range, trapz(c_range, posterior, 1), 2), 4);
pdf_a = (squeeze(pdf_a))';
pdf_b = trapz(sigma_range, trapz(a_range, trapz(c_range, posterior, 1), 3), 4);
pdf_c = trapz(sigma_range, trapz(a_range, trapz(b_range, posterior, 2), 3), 4);
pdf_c = pdf_c';
pdf_sigma = trapz(a_range, trapz(b_range, trapz(c_range, posterior, 1), 2), 3);


% means and variances
mean_a = trapz(a_range, a_range .* pdf_a);
var_a = trapz(a_range, (a_range - mean_a).^2 .* pdf_a);
mean_b = trapz(b_range, b_range .* pdf_b);
var_b = trapz(b_range, (b_range - mean_b).^2 .* pdf_b);
mean_c = trapz(c_range, c_range .* pdf_c);
var_c = trapz(c_range, (c_range - mean_c).^2 .* pdf_c);
mean_sigma = trapz(sigma_range, sigma_range .* pdf_sigma);
var_sigma = trapz(sigma_range, (sigma_range - mean_sigma).^2 .* pdf_sigma);
std_dev_sigma = sqrt(var_sigma);

% print out results
disp(['Mean of c: ', num2str(mean_c)]);
disp(['Variance of c: ', num2str(var_c)]);
disp(['Mean of b: ', num2str(mean_b)]);
disp(['Variance of b: ', num2str(var_b)]);
disp(['Mean of a: ', num2str(mean_a)]);
disp(['Variance of a: ', num2str(var_a)]);
disp(['Mean of sigma: ', num2str(mean_sigma)]);
disp(['Standard deviation of sigma: ', num2str(std_dev_sigma)]);