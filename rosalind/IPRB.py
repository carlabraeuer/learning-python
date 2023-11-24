k = 2
m = 2
n = 2
pop = k + m + n

kk = (k/pop) * (k-1)/(pop-1)
km = (k/pop) * m/(pop-1)
kn = (k/pop) * n/(pop-1)
mk = (m/pop) * k/(pop-1)
mm = (m/pop) * (m-1)/(pop-1) * 0.75
mn = (m/pop) * n/(pop-1) * 0.5
nk = (n/pop) * k/(pop-1)
nm = (n/pop) * m/(pop-1) * 0.5

dom = round(kk + km + kn + mk + mm + mn + nk + nm, 5)
print(dom)
