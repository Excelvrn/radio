import pandas, os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy
import math

path = '/home/excelvrn/Pr/UHF/mes_2'

for el in os.listdir(path):
    if el.count('s2p'):
        print(el)

df = pandas.read_csv(path+'/1.s2p', sep = ' ')
print(df.shape, df.columns, df.iloc[1, ])

df2 = pandas.read_csv(path+'/2.s2p', sep = ' ')
#print(df2.shape, df2.columns, df2.iloc[1, ])

df3 = pandas.read_csv(path+'/3.s2p', sep = ' ')
#print(df3.shape, df3.columns, df3.iloc[1, ])

r1 = pandas.read_csv(path+'/4.s2p', sep = ' ')
#print(df3.shape, df3.columns, df3.iloc[1, ])

r2 = pandas.read_csv(path+'/5.s2p', sep = ' ')
#print(df3.shape, df3.columns, df3.iloc[1, ])

r3 = pandas.read_csv(path+'/6.s2p', sep = ' ')
#print(df3.shape, df3.columns, df3.iloc[1, ])

r4 = pandas.read_csv(path+'/7.s2p', sep = ' ')
#print(df3.shape, df3.columns, df3.iloc[1, ])

r21 = pandas.read_csv(path+'/8.s2p', sep = ' ')
#print(df3.shape, df3.columns, df3.iloc[1, ])

r22 = pandas.read_csv(path+'/9.s2p', sep = ' ')
#print(df3.shape, df3.columns, df3.iloc[1, ])

r23 = pandas.read_csv(path+'/10.s2p', sep = ' ')
#print(df3.shape, df3.columns, df3.iloc[1, ])

r24 = pandas.read_csv(path+'/11.s2p', sep = ' ')
#print(df3.shape, df3.columns, df3.iloc[1, ])

def cmp(a, b, a1, b2):
    if a==b:
        return str(a1)+'='+str(b2)
    elif a>b:
        return str(a1)+'>'+str(b2)
    else:
        return str(a1)+'<'+str(b2)

#print(cmp(1,2, 4,5))

dfl = [df, df2, df3, df2, df3]
#print(dfl)
def g(l:list):
    gg = []
    for i in range(0, len(l)):
        if i>0:
            gg+=[l[i]]
            #if len(l)>1:
                #cmp(l[0], l[i], 0, i)
    if len(gg)>1:
        print(f'---{len(gg)}')
        g(gg)
    else:
        print(f'---')
            
#g(dfl)
gl_tgfa =df['S21'] - df2['S21'] 
gl_tol = df['S21'] - df3['S21']
tgfa_tol = df2['S21'] - df3['S21']
gl_r1 = df3['S21'] - r1['S21'] 
r1_r2 = r1['S21'] - r2['S21'] 
r2_r3 = r2['S21'] - r3['S21'] 
r3_r4 = r3['S21'] - r4['S21'] 
gl_r4 = df['S21'] - r4['S21'] 
gl_r2 = df['S21'] - r2['S21'] 
gl_r4 = df['S21'] - r4['S21'] 

ind = 0
more = 0
less = 0
equ = 0
for el in gl_r4:
    if el<0:
        less+=1
        #print(f'{round(df["Hz"].iloc[ind]/1e6)} - {el}')
    elif el==0:
        equ+=1
        #print(f'{round(df["Hz"].iloc[ind]/1e6)} - {el}')
    else:
        more+=1
        #print(f'{round(df["Hz"].iloc[ind]/1e6)} - {el}')
    ind+=1
print(f'\t>{more}\t={equ}\t<{less}')

def dB(x):
    return 10**(x/10)

#for i in range(0, 20):
    #print(i, 1-dB(-float(i)))

def graph(*idf):
    print(type(idf))
    '''
    for d in idf:
        print(type(d))
        leg = ''
        #if d==idf[0]:
            #leg = 'asdf'
        #else:
            #leg = 'asdfffffff'
        #if d == idf[0]:
           #leg='asdf' 
        plt.plot(d['Hz']/1e6, d['S12'], label=leg)
    '''
    ind=0
    lbl = '1'
    for d in idf:
        ind+=1
        if ind>4:
            lbl='2'
            ind=1
        plt.plot(d['Hz']/1e6, d['S12'], label=lbl+'-'+str(ind))
    plt.plot(idf[0]['Hz']/1e6, idf[0]['S12'], label='r1')
    #plt.plot(idf[1]['Hz']/1e6, idf[1]['S12'], label='r2')
    #plt.plot(idf[2]['Hz']/1e6, idf[2]['S12'], label='r3')
    #plt.plot(idf[3]['Hz']/1e6, idf[3]['S12'], label='r4')
    plt.legend()
    plt.show()
    

#graph(r1, r2, r3, r4)
#graph(r1, r2, r3, r4, r21, r22, r23, r24)


def mm(*d):
    rs, cs = d[0].shape
    #s = 0
    ssum = 0
    fr = []
    r1 = []
    r2 = []
    r3 = []
    r4 = []
    r21 = []
    r32 = []
    r43 = []
    mark = []
    gpi = 180/math.pi
    for r in range(0, rs):
        s = 0
        for idf in range(0, len(d)):
            if idf==0:
                last=d[idf]['S12'].iloc[r]
                continue
            if d[idf]['S12'].iloc[r]>last:
                last=d[idf]['S12'].iloc[r]
                s+=1
            else:
                break
        if s==(len(d)-1):
            ssum+=1
            fr+=[round(d[0]['Hz'].iloc[r]/1e6)]
            r1+=[d[0]['S12'].iloc[r]]
            #r2+=[d[0]['S12'].iloc[r]/d[1]['S12'].iloc[r]]
            #r3+=[d[0]['S12'].iloc[r]/d[2]['S12'].iloc[r]]
            #r4+=[d[0]['S12'].iloc[r]/d[3]['S12'].iloc[r]]
            r2+=[math.atan(d[1]['S12'].iloc[r]-d[0]['S12'].iloc[r])*gpi]
            r3+=[math.atan(d[2]['S12'].iloc[r]-d[1]['S12'].iloc[r])*gpi]
            r4+=[math.atan(d[3]['S12'].iloc[r]-d[2]['S12'].iloc[r])*gpi]
            
            d21 = d[1]['S12'].iloc[r]-d[0]['S12'].iloc[r]
            r21+=[ d21 ]
            
            d32 = d[2]['S12'].iloc[r]-d[1]['S12'].iloc[r]
            r32+=[ d32 ]
            
            d43 = d[3]['S12'].iloc[r]-d[2]['S12'].iloc[r]
            r43+=[ d43 ]
            
            if d43<d32 and d32<d21:
                mark+=[1]
            else:
                mark+=[0]
            #print(d[0]['Hz'].iloc[r])
    print(ssum)
    
    ndf = pandas.DataFrame({'fr':fr, 'r1':r1, 'r2':r2, 'r3':r3, 'r4':r4, 'r21':r21, 'r32':r32, 'r43':r43,\
        'mark':mark})
    print(ndf.shape)
    ndf.to_excel('asdf.xlsx')
    
    #print(len(d))
#mm(r1, r2, r3, r4)
#mm(r21, r22, r23, r24)

def interp(d, c1, c2):
    rs, cs = d.shape
    
    x = []
    y = []
    
    for r in range(0, rs):
        x+=[d.iloc[r, c1]/10**9]
        y+=[d.iloc[r, c2]]
    
    print(numpy.interp(8, x, y))

#interp(r1, 0, 2)

def poly(d, c1, c2):
    rs, cs = d.shape
    print(f'{rs} x {cs}')
    
    x = []
    y = []
    
    #x = ()
    #for r in range(0, rs):
    for r in range(0, 50):
        x+=[d.iloc[r, c1]/10**9]
        y+=[d.iloc[r, c2]]
        #x = x+(d.iloc[r, c2])
    #print((d.iloc[4, c2]))
    #print(tuple(y))
    #ar = numpy.poly(tuple(y))
    ar = numpy.poly(numpy.array([x, y]))
    print(ar.size)
    
    for el in ar:
        print(el)
poly(r1, 0, 2)
