#!/usr/bin/python
import sys, itertools, os, time
gapenting="""
++++++++++++++[WORDLIST GENERATOR]++++++++++++++
+                                              +
+++++++++++++[CODED BY SECURITY007]+++++++++++++

"""
print gapenting
chrs = raw_input("Word to generate combination  : ")
min_length =int(raw_input("Min length character : "))
max_length =int(raw_input("Max length character : "))
output = raw_input("Output file name [ex:wordlist.txt] : ")
psd = open(output, 'wb')
timeS=time.asctime()
start=time.time()
for i in xrange(min_length,max_length+1):
  r=100*i/max_length
  l="Progress : "+str(r)+' %'
  
  sys.stdout.write("\r%s"%l+" Complete" )
  sys.stdout.flush()
  psd.flush()
  for xs in itertools.product(chrs, repeat=i):
    psd.write(''.join(xs)+'\n')
end=time.time()
totaltime=end-start
print "\n[-]------------------------[Result]--------------------------[-]"
print "Proccess start :",timeS
print "Proccess finish :",time.asctime()
print "Total time :",totaltime,"Second"
print "Saved as : "+output
print "Location : "+os.getcwd()+"/"+output
print "[-]----------------------------------------------------------[-]"
psd.flush()    
psd.close()