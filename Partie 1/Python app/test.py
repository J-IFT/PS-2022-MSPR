import nmap

host = input("10.60.68.18")

nm = nmap.PortScanner()
nm.scan(host, '1-65535')

for host in nm.all_hosts():
    print('Hôte : %s (%s)' % (host, nm[host].hostname()))
    for proto in nm[host].all_protocols():
        lport = nm[host][proto].keys()
        lport.sort()
        for port in lport:
            print('port : %s\tétat : %s' % (port, nm[host][proto][port]['state']))