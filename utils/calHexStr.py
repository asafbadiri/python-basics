import hexstr as hs
import os
import subprocess
from subprocess import Popen,PIPE

print("Hello From callStrHex")
print("The value of __name__ is:", repr(__name__))

print("\nreturnValue for hs.hexstr 199 is " + hs.hexstr(199) + "\n")

print("os.system run another program outside local scope")
cmd1 = "python3 hexstr.py 346"
returnValue = os.system(cmd1)
print("\nreturnValue for os.system = %d\n" %returnValue)

result_code = os.system(cmd1 + ' > output.txt')
if os.path.exists('output.txt'):
    fp = open('output.txt', "r")
    output = fp.read()
    fp.close()
    os.remove('output.txt')
    print("\nfrom output.txt file %d" %result_code)
    print(output)

print("Now with import subprocess check_output ")
result = subprocess.check_output(cmd1, shell=True)
print("shell result is\n" , result)

print("\nNow with import subprocess call ")
rc = subprocess.call(cmd1, shell=True) #(["grep","-Eq","(z|k|tc)sh","/etc/passwd"])
print(str(rc))

#from subprocess import Popen,PIPE             p = Popen(["cat","/etc/passwd","/foo/bar"], stdout=PIPE,stderr=PIPE)
print("\nNow with import subprocess Popen and PIPE ")
p = Popen(["python3","hexstr.py","346"], stdout=PIPE,stderr=PIPE)
(out,err) = p.communicate();
print ("python3 hexstr.py 346 returned code = %d" % p.returncode)
print ("python3 hexstr.py 346 output: %s" % out)
print ("python3 hexstr.py 346 errors: %s" % err)


try:
    fout = open('files.txt','w')
    ferr = open('errors.txt','w')
    subprocess.check_call ("ls -l /etc/", shell=True, stdout=fout, stderr=ferr)
    fout.close()
    ferr.close()
except IOError as e:
    sys.exit("I/O error on '%s': %s" % (e.filename, e.strerror))
except CalledProcessError as e:
    sys.exit("'ls' failed, returned code %d (check 'errors.txt')" \
             % (e.returncode))
except OSError as e:
    sys.exit("failed to run shell: %s" % (str(e)))


print("\nEND OF PROGRAM ")
