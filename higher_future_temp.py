def higher_future_temp( temperatures ) :
	#Insert your code here
	n = len(temperatures)
	daysOFwait = [0] * n
	s = []

	for i in range(0, n):
		while(len(s) != 0 and temperatures[s[-1]] < temperatures[i]):
			daysOFwait[s[-1]] = i - s[-1]
			s.pop(-1)
		s.append(i)

	# for i in range(n):
		# print(daysOFwait[i], end = "")

	return daysOFwait