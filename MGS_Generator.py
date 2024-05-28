# %%
dict = {'g0':'21',
        'f5':'20',
        'f4':'19',
        'f3':'18',
        'f2':'16',
        'f1':'17',
        'e1':'15',
        'a1':'13',
        'd1':'12',
        'c1':'14',
        'b1':'11',
        'e2':'10',
        'd2':'7',
        'a2':'8',
        'c2':'9',
        'b2':'6',
        'e3':'5',
        'd3':'1',
        'a3':'4',
        'c3':'3',
        'b3':'2',
        }
puntures=3
torus=3

def generate_alpha(j):
    if j == 0:
        return ['g0']
    elif j == 1:
        return ['g13','g12','g11','g13','g0']
    elif j == 2:
        return ['g23','g22','g12','g11','g21','g23','g12','g13','g0']
    elif j >=3 :
        alpha_sequence = []
        i=j
        while i > 3:
            alpha_sequence.extend([f'g{i}3',f'g{i}2',f'g{i-2}1',f'g{i-1}1',f'g{i}1',f'g{i}3',f'g{i-2}1',f'g{i-1}3',f'g{i-3}1',f'g{i-2}3'])
            i-=1
        alpha_sequence.extend([f'g33',f'g32',f'g11',f'g21',f'g31',f'g33',f'g11',f'g23',f'g11',f'g23','g12','g13','g0'])
        return alpha_sequence
def generate_sigma(i):
    return [f'e{i}',f'd{i}',f'b{i}',f'c{i}',f'a{i}',f'b{i}',f'd{i}',f'e{i}',f'c{i}',f'a{i}',f'b{i}']
def generate_beta(j):
    if j == 0:
        return None
    elif j == 1:
        return ['g11','g12','g13']
    elif j == 2:
        return ['g11','g21','g11','g23','g12','g13']
    elif j >= 3:
        beta_sequence = []
        i = j
        t = torus
        while i > 3 and t > 3:
            beta_sequence.extend([f'g{t-1}1',f'g{i}1',f'g{t-1}1',f'g{t}3',f'g{t-2}1',f'g{t-1}3',f'g{t-3}1'])
            i=i-1
            t=t-1
        beta_sequence.extend([f'g{t-1}1',f'g{3}1',f'g{t-1}1',f'g{t}3',f'g{t-2}1',f'g{t-1}3',f'g{t-3}1','g33','g11','g23','g12','g13'])
        return beta_sequence
def generate_tau(i):
    return [f'e{i}',f'b{i}',f'a{i}',f'c{i}',f'e{i}',f'd{i}',f'b{i}',f'a{i}',f'e{i}']
def generate_gamma(n):
    gamma_sequence = []
    for i in range(n):
        l = n-i
        gamma_sequence.append(f'f{l}')
    for i in range(n+1):
        if i>=3:
            gamma_sequence.append(f'f{i}')
    return gamma_sequence


def mapping(dict, key):
    return dict.get(key, "Key not found in the dictionary")

# %%
full_sequence = []
for f in generate_gamma(torus+2):
    full_sequence.append(mapping(dict,f))
for n in range(torus):
    i = torus - n
    for h in generate_sigma(i):
        full_sequence.append(mapping(dict,h))
full_sequence.append(mapping(dict, generate_alpha(0)[0]))
for p in range(puntures-3):
    for id in generate_alpha(p+1):
        full_sequence.append(mapping(dict, p))
for f in generate_gamma(torus+2):
    full_sequence.append(mapping(dict,f))
full_sequence.append(mapping(dict,f'f{torus+1}'))
try:
    for id in generate_beta(puntures-3):
        full_sequence.appned(mapping(dict,id))
except:
    pass

for n in range(torus):
    for id in generate_tau(n+1):
        full_sequence.append(mapping(dict,id))


# %%
print(full_sequence)


