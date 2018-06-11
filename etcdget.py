#!/bin/python3.6
import subprocess,sys
import json
def etcdget(key, prefix=''):
 endpoints=''
 data=json.load(open('/pacedata/runningetcdnodes.txt'));
 for x in data['members']:
  endpoints=endpoints+str(x['clientURLs'])[2:][:-2]+','
 cmdline=['/bin/etcdctl','--endpoints='+endpoints,'get',key,prefix]
 result=subprocess.run(cmdline,stdout=subprocess.PIPE)
 z=[]
 try:
  if(prefix =='--prefix'):
   mylist=str(result.stdout)[2:][:-3].split('\\n')
   zipped=zip(mylist[0::2],mylist[1::2])
   for x in zipped:
    z.append(x) 
    print(x)
  elif(prefix == ''):
   z.append((str(result.stdout).split(key)[1][2:][:-3]))
   print(str(result.stdout).split(key)[1][2:][:-3])
  else:
   mylist=str(result.stdout)[2:][:-3].split('\\n')
   zipped=zip(mylist[0::2],mylist[1::2])
   for x in zipped:
    if prefix in str(x):
     z.append(x)
     print(x)
 except:
  z.append(-1)
  print('-1')
 return z
if __name__=='__main__':
 etcdget(*sys.argv[1:])
