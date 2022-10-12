# Linux-users-groups-task

- Create users and add the following options to them

![image](https://user-images.githubusercontent.com/85888419/195319556-6ea06094-8cb8-4d97-8ad8-5f196f753e9b.png)

## After creating users:
  - Create 6 groups and add each user to its respective group.
  - Add this password **Alibabastudent001** to CEO,HR, and SALES groups 

![image](https://user-images.githubusercontent.com/85888419/195319766-b305a26b-be0a-4e80-abc5-fe1e256bd500.png)

After finishing the lab take screen shots of the /etc/passwd & /etc/shadow & /etc/group. Then save history output to a file and then upload the three pictures and the text file to the forked repo and then create a pull request. 

 
  103  sudo groupadd SHIPING
  104  sudo groupadd MANAGER
  105  sudo groupadd FINANCE
  106  tail /etc/group
  107  useradd ALI -c "HR,MANAGER" -e 2025-1-1
  108  sudo useradd ALI -c "HR,MANAGER" -e 2025-1-1
  109  sudo useradd ALI -p alibaba@S1 -c "HR,MANAGER" -e 2025-1-1
  110  ALI -p alibaba@S1
  111  sudo useradd SALEM -p alibaba@S1 -c "CEO" 
  112  sudo useradd RAGHED -p alibaba@S1 -c "HR Specialist" -e 2025-1-1
  113  sudo useradd SARAH -p alibaba@S1 -c "Sales represntative" -e 2025-1-1
  114  sudo useradd ABDULLAH -p alibaba@S1 -c "Shipping" -e 2025-1-1
  115  sudo useradd DEEM -p alibaba@S1 -c "HR Specialist" -e 2025-1-1
  116  sudo useradd KHALID -p alibaba@S1 -c "Finance,Manager" -e 2025-1-1
  117  sudo useradd NORAH -p alibaba@S1 -c "Finance Specialist" -e 2025-1-1
  118  sudo useradd KHALID -p alibaba@S1 -c "HR Specialist" -e 2025-1-1
  119  sudo useradd KHALID2 -p alibaba@S1 -c "HR Specialist" -e 2025-1-1
  120  sudo useradd RANEEM -p alibaba@S1 -c "Sales represntative" -e 2025-1-1
  121  sudo useradd AHMED -p alibaba@S1 -c "Shipping" -e 2025-1-1
  122  sudo useradd OUDI -p alibaba@S1 -c "Shipping" -e 2025-1-1
  123  sudo useradd ABDULAZIZ -p alibaba@S1 -c "Shipping" -e 2025-1-1
  124  sudo useradd NAIF -p alibaba@S1 -c "Sales represntative" -e 2025-1-1
  125  sudo useradd GHADA -p alibaba@S1 -c "HR,MANAGER" -e 2025-1-1
  126  sudo useradd MOHAMMED -p alibaba@S1 -c "Shipping" -e 2025-1-1
  127  sudo useradd HANAN -p alibaba@S1 -c "Sales represntative" -e 2025-1-1
  128  tail  /etc/passwd
  129  sudo groupadd -p Alibabastudent001 HR
  130  sudo groupadd -p Alibabastudent001 CEO
  131  sudo groupadd -p Alibabastudent001 SALES
  132  sudo useradd -a -G CEO SALEM
  133  sudo usermod -a -G CEO SALEM
  134  sudo usermod -a -G HR DEEM
  135  sudo usermod -a -G HR GHADA
  136  sudo usermod -a -G HR KHAILID
  137  sudo usermod -a -G HR KHALID
  138  sudo usermod -a -G HR ALI
  139  sudo usermod -a -G HR RAGHED
  140  sudo usermod -a -G SALES HANAN
  141  sudo usermod -a -G SALES NAIF
  142  sudo usermod -a -G SALES RANEEM
  143  sudo usermod -a -G SALES SARAH
  144  sudo usermod -a -G SHIPPING OUDI
  145  sudo usermod -a -G  SHIPING OUDI
  146  sudo usermod -a -G  SHIPING MOHAMMED
  147  sudo usermod -a -G  SHIPING ABDULAZIZ
  148  sudo usermod -a -G  SHIPING AHMED
  149  sudo usermod -a -G  MANAGER KHALID 
  150  sudo usermod -a -G  MANAGER GHADA
  151  sudo usermod -a -G  MANAGER ALI
  152  sudo usermod -a -G  FINANCE KHALID 
  153  sudo usermod -a -G  FINANCE NORAH
  154  sudo passwd SALEM
  155  sudo passwd ALI
  156  sudo passwd RAGHED
  157  sudo passwd SARAH
  158  sudo passwd ABDULLAH
  159  sudo passwd DEEM
  160  sudo passwd KHALID
  161  sudo passwd NORAH
  162  sudo passwd RANEEM
  163  sudo passwd AHMED
  164  sudo passwd OUDI
  165  sudo passwd ABDULAZIZ
  166  sudo passwd NAIF
  167  sudo passwd GHADA
  168  sudo passwd MOHAMMED
  169  sudo passwd HANAN
  170  sudo cat /etc/shadow
  171  sudo cat /etc/passwd
  172  sudo cat /etc/group
