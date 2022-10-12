# Linux-users-groups-task

- Create users and add the following options to them

/etc/passwd conent :

![image](https://user-images.githubusercontent.com/114053471/195334418-b89c395b-c9c1-4676-9714-0e15504c9df7.png)


/etc/shadow content:
![image](https://user-images.githubusercontent.com/114053471/195334638-a6485f3f-233a-4053-b67c-6e4614b55f79.png)


## After creating users:
  - Create 6 groups and add each user to its respective group.
  - Add this password **Alibabastudent001** to CEO,HR, and SALES groups 

/etc/group content:
![image](https://user-images.githubusercontent.com/114053471/195334760-2c41c434-38da-4933-85f6-16822eeac9a5.png)


history:
![image](https://user-images.githubusercontent.com/114053471/195338630-2f0d42a0-47d7-4837-b42a-d873817566c0.png)

![image](https://user-images.githubusercontent.com/114053471/195338763-9d9cf8c5-0cc2-473c-a75d-69b9c406935e.png)


└─# cat history.txt
    1  lsblk
    2  nmcali
    3  nmcli
    4  nmcli con show 
    5  nmcli con show  Wired\ connection\ 1
    6  sudo -lU kali
    7  tail -5 /var/log/secure
    8  groupadd HR CEO SALES SHIPPING MANAGER FINANCE
    9  groupadd -r HR CEO SALES SHIPPING MANAGER FINANCE
   10  ^[[200~for group in group1 group2 group3;do groupadd -r ${group};done
   11  for group in HR CEO SALES SHIPPING MANAGER FINANCE;do groupadd -r ${group};done
   12  GROUPS
   13  groups
   14  tail /etc/group
   15  useradd ALI -c "HR,Manager" -e 2025-1-1 
   16  useradd SALEM -c "CEO" -e 2025-1-1 
   17  useradd RAGHAD -c "HR SPECIALT" -e 2025-1-1 
   18  useradd SARAH -c "Sales representative" -e 2025-1-1 
   19  useradd  ABDULLAH -c "shipping" -e 2025-1-1 
   20  useradd  DEEM -c "HR SPECIALT" -e 2025-1-1 
   21  useradd KHALED -c "FINANCE,MANAGER" -e 2025-1-1 
   22  useradd NORAH -c "Finance specialt" -e 2025-1-1 
   23  useradd KHALED -c "HR SPECIALT" -e 2025-1-1 
   24  useradd KHALED -c "HR SPECIALT" -e 2025-1-1 -u 334
   25  useradd KHALED -c "HR SPECIALT" -e 2025-1-1 -u 1033
   26  useradd KHALED -c "HR SPECIALT" -e 2025-1-1 -u 2032
   27  useradd RANEEM -c "SALES REPRESNITIVE" -e 2025-1-1 
   28  useradd Ahmed -c "Shipping" -e 2025-1-1 
   29  useradd OUDI -c "Shipping" -e 2025-1-1 
   30  useradd Abdulaziz -c "Shipping" -e 2025-1-1 
   31  useradd Naif -c "sale represitative" -e 2025-1-1 
   32  useradd GHADA -c "HR,MANAGER" -e 2025-1-1 
   33  useradd Mohammed -c "Shipping" -e 2025-1-1 
   34  useradd Hanan -c "sale represitative" -e 2025-1-1 
   35  ^[[200~for user in userA userB userC; do sudo usermod -a -G mygroup "$user"; done
   36  for user in DEEM GHADA KHALED ALI RAGHAD; do sudo usermod -a -G HR "$user"; done
   37  groups DEEM
   38  for user in SALEM; do sudo usermod -a -G CEO "$user"; done
   39  for user in Hanan naif raneem sarah; do sudo usermod -a -G SALES "$user"; done
   40  for user in Hanan NAIF RANEEM SARAH; do sudo usermod -a -G SALES "$user"; done
   41  for user in Hanan Naif RANEEM SARAH; do sudo usermod -a -G SALES "$user"; done
   42  for user in OUDI Mohammed ABDULAZIZ AHMED; do sudo usermod -a -G SHIPPING "$user"; done
   43  for user in OUDI Mohammed Abdulaziz Ahmed; do sudo usermod -a -G SHIPPING "$user"; done
   44  for user in Khaled GHADA ALI; do sudo usermod -a -G MANAGER "$user"; done
   45  for user in KHALED GHADA ALI; do sudo usermod -a -G MANAGER "$user"; done
   46  for user in KHALED NORAH; do sudo usermod -a -G FINANCE "$user"; done
   47  for user in ALI SALEM RAGHAD SARAH ABDULLAH DEEM Khaled NORAH RANEEM AHMED OUDI Abdulaziz Naif GHADA Mohammed HANAN ; do sudo passwd alibaba@S1 "$user"; done
   48  passwd SARAH AHMED 
   49  passwd ALI
   50  passwd SALEM
   51  passwd RAGHAD 
   52  passwd SARAH 
   53  passwd ABDULLAH
   54  passwd Deem
   55  passwd DEEM
   56  passwd Khaled
   57  passwd KHALED
   58  passwd NORAH
   59  passwd RANEEM
   60  passwd Ahmed
   61  passwd OUDI
   62  passwd Abdulaziz
   63  passwd NAIF
   64  passwd Naif
   65  passwd GHADA
   66  passwd Mohammed
   67  passwd HANAN
   68  passwd Hanan
   69  gpasswd HR
   70  gpasswd CEO
   71  gpasswd SALES
   72  gpasswd SHIPPING
   73  gpasswd MANAGER
   74  gpasswd FINANCE
   75  cat /etc/passwd
   76  usermod KHALED -c "FINANCE MANAGER , HR SPECIALT"
   77  cat /etc/passwd
   78  cat /etc/shadow
   79  cat /etc/group
   80  history
                 
