import os
import shodan
import re
import sys
import subprocess
import string

SHODAN_API_KEY = "Mawfb3ne6mFteBiRLkbDH6v5UfKyizdj"
api = shodan.Shodan(SHODAN_API_KEY)

f=open("c://xmpp2.txt","w")
fr=open("c://from.txt",'w')
fid=open("c://id.txt",'w')
pattern_iid=re.compile(r'id="(\w|\W)+"')
pattern_iid2=re.compile(r"id='(\w|\W)+'")
pattern_from=re.compile(r'from=(\'|\")(\w|\W)+(\'|\")')
try:
        # Search Shodan
        results = api.search(r"xmpp")
       
        # Show the results
        print 'Results found: %s \n' % results['total']
        i=1
        for result in results['matches']:
                i+=1
                f.write("IP:"+str(result["ip_str"])+"\n")
                f.write("Port:"+str(result["port"])+"\n")
                f.write(result["data"]+"\n\n")
                
                iid=re.search(pattern_iid,result['data'])
                print iid
                if iid==None:
                    iid=re.search(pattern_iid2,result['data'])
                    print iid
                from_id=re.search(pattern_from,result['data'])
                print from_id
                
                try:
                    fid.write(from_id.group()+'\n')
                except:
                    pass
                
                try:
                    f.write(iid.group()+'\n')
                except:
                    pass
                
                try:
                    f.write(from_id.group()+'\n\n')
                except:
                    pass
                
                print ''
        print i
        
except shodan.APIError, e:
        print 'Error: %s' % e
        
f.close()
fr.close()
fid.close()
'''
location='c:\\down.txt'
pattern_ip=re.compile('\d+.\d+.\d+.\d+')
pattern_port=re.compile('\d+/tcp\s+open\s+\w+')

indata=open(location,'r')   
n=1
count=len(indata.readlines())
for line in indata:
  print '----------------------------------------'
  print 'current line is:%d  totality of lines:%d' %(n,count)
  print '----------------------------------------'
  n+=1
  outdata=open(location.strip('.txt')+'-output.txt','a+')
  

  if re.match(pattern_ip,line):
    outdata.write(line.strip('\n'))
    
    ip=re.match(pattern_ip,line).group()
    
    print ip
    #nmap_data=os.popen('nmap '+str(ip)).read()
    print '~~~~~~~~~~~nmaping~~~~~~~~~~~~'
    nmap_data= subprocess.Popen('nmap '+str(ip), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    nmap_port=re.findall(pattern_port,nmap_data.stdout.read())
    tmp='\n'
    outdata.write(tmp)
    
    line=line.strip('\n')
    for port_line in nmap_port:
        tmp+=port_line+'\n'
        print port_line
    try:
        print '~~~~~~~~~~~~~shodaning~~~~~~~~~~~~'
        host=api.host(ip)
        org=host.get('org','n/a')
        os=host.get('os', 'n/a')
        port=host.get('port','n/a')       
        tmp=tmp.strip('\n')
        for service in host['data']:
          tmp=tmp+'Port:'+str(service['port'])+'\n'+'Banner:'+str(service['data'])
        outdata.write(org+','+str(os)+','+str(port)+','+'\n'+tmp+'\n')
        
    except shodan.APIError, e:
        print 'Error: %s' % e   
    
  else:
      outdata.write(line)
      continue
    
  outdata.close()

indata.close()
'''
