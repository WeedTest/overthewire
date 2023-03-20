nmap -p- 127.0.0.1 |grep 'tcp' | while IFS= read -r line;do echo "$line" | cut -d'/' -f1 ; done # lister les port
nmap -p- 127.0.0.1 |grep 'tcp' | while IFS= read -r line;do echo  $line | cut -d'/' -f1 | xargs -I {} ./suconnect {} ; done #exec suconnect on all port
