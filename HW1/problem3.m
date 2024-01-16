% Unit tests

disp("Testing the functions provided in the Homework 1 PDF for calculating S1.")
disp("Recursive function, for n = 5: S = " + S1_rec(5))
disp("Iterative function, for n = 5: S = " + S1_iter(5))

disp("The iterative function adds the value of n at each step instead of adding values in a sequence.")
disp("Testing the fixed iterative function for calculating S1.")
disp("Iterative function, for n = 5: S = " + S1_iter_fixed(5))


disp("Testing the recursive function for calculating O1.")
disp("For n = 5: O = " + O1_rec(5))
disp("For n = 8: O = " + O1_rec(8))


disp("Testing the recursive function for calculating S2.")
disp("For n = 5: S = " + S2_rec(5))
disp("For n = 8: S = " + S2_rec(8))


% Functions
function S = S1_rec(n)
	if n > 1
		S = n + S1_rec(n-1);
	else
		S = 1;
	end
end

function S = S1_iter(n)
	S = 0;
	for i = 1:n
		S = S+n;
	end
end

function S = S1_iter_fixed(n)
	S = 0;
	for i = 1:n
		S = S+i;
	end
end

function O = O1_rec(n)
	if n > 1
		O = (2*n-1) + O1_rec(n-1);
	else
		O = 1;
	end
end

function S = S2_rec(n)
	if n > 1
		S = n^2 + S2_rec(n-1);
	else
		S = 1;
	end
end
