% n is resolution (number of points along a given axis)
% p is number of iterations
function mandelbrot(n, p)

%Set limits
x0 = -2;   
x1 = 1;
y0 = -1.5; 
y1 = 1.5;

% Set an array of complex numbers
x = linspace(x0, x1, n);
y = linspace(y0, y1, n);
% [x,y] = meshgrid(linspace(x0, x1, n), linspace(y0, y1, n));
c = x + 1i * y;

% Set a matrix of intermittent results
z = zeros(size(c));
% Set a matrix to store information if the number is not in the Mandelbrot set
k = zeros(size(c));

for i = 1:p
	% perform the calculation for every complex number
    z = z.^2 + c;
	% if (abs(z) > 2, the value is not in the Mandelbrot set 
    k(abs(z) > 2 & k == 0) = p - i;
end

%If the points were not confirmed to be outside of the Mandelbrot set, they are treated as inside

k(k ~= 0) = 1;

figure,
imagesc(x(1,:), y(:,1), k),
colormap hot
axis square

end

function problem7()

mandelbrot(800,40)

end