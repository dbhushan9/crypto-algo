def eucledian(a,b):
	if b == 0:
		return a
	return eucledian(b,a%b)

def extended_eucledian(a,b):
    if b==0:
        return (a,1,0)
    g,s,t = extended_eucledian(b,a%b)
    return (g,t,s-(a//b)*t)

def m_inverse(a,m):
    g,s,t = extended_eucledian(a,m)
    print(g,s,t)
    if g!=1:
        return None
    else:
        return ((s%m+m)%m)