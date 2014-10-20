score1=float(input('please input your first score\n'))
score2=float(input('please input your second score\n'))
score3=float(input('please input your third score\n'))
x=[score1,score2,score3]
x.sort()
finalscore=x[0]*0.2+x[1]*0.3+x[2]*0.5
print('your score\n')
print(finalscore)
