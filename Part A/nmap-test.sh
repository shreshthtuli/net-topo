for i in {1..24}
do
	nmap -sP 10.208.26.0/24 >> nmap-test.txt
	sleep 3600
done