#----#


  180  sudo groupadd 'HR'
  181  sudo groupadd 'CEO'
  182  sudo groupadd 'SALES'
  183  sudo groupadd 'SHIPPING'
  184  sudo groupadd 'MANAGER'
  185  sudo groupadd 'FINANCE'
  
  ---------------------------------------------------------------------------------------------------------------------
  
  186  sudo cat /etc/group

  ---------------------------------------------------------------------------------------------------------------------

  188  sudo useradd  -c "HR, MANAGER", -G HR,MANAGER -e 2025-1-1  ALI  &&  sudo  passwd  ALI
  189  sudo useradd  -c "CEO", -G CEO  SALEM  &&  sudo  passwd  SALEM
  197  sudo useradd  -c "HR Specialist", -G HR -e 2025-1-1  RAGHED  &&  sudo  passwd  RAGHED
  200  sudo useradd  -c "Sales representative", -G SALES -e 2025-1-1  SARAH  &&  sudo  passwd  SARAH
  201  sudo useradd  -c "Shipping", -e 2025-1-1  ABDULLAH  &&  sudo  passwd  ABDULLAH
  202  sudo useradd  -c "HR Specialist", -G HR, -e 2025-1-1  DEEM  &&  sudo  passwd  DEEM
  203  sudo useradd  -c "HR Specialist", -G HR -e 2025-1-1  DEEM  &&  sudo  passwd  DEEM
  204  sudo useradd  -c "Finance, Manager, HR Specialist", -G HR, MANAGER, FINANCE -e 2025-1-1  KHALID  &&  sudo  passwd  KHALID
  205  sudo useradd  -c "Finance, Manager, HR Specialist", -G HR,MANAGER,FINANCE -e 2025-1-1  KHALID  &&  sudo  passwd  KHALID
  206  sudo useradd  -c "Finance Specialist", -G FINANCE -e 2025-1-1  NORAH  &&  sudo  passwd  NORAH
  207  sudo useradd  -c "Sales representative", -G FINANCE -e 2025-1-1  RANEEM  &&  sudo  passwd  RANEEM
  208  sudo useradd  -c "Shipping", -G SHIPPING -e 2025-1-1  AHMED  &&  sudo  passwd  AHMED
  209  sudo useradd  -c "Shipping", -G SHIPPING -e 2025-1-1  OUDI  &&  sudo  passwd  OUDI
  210  sudo useradd  -c "Shipping", -G SHIPPING -e 2025-1-1  ABDULAZIZ  &&  sudo  passwd  ABDULAZIZ
  211  sudo useradd  -c "Sales representative", -G SALES -e 2025-1-1  NAIF  &&  sudo  passwd  NAIF
  212  sudo useradd  -c "HR, Manager", -G HR,MANAGER -e 2025-1-1  GHADA  &&  sudo  passwd  GHADA
  213  sudo useradd  -c "Shipping", -G SHIPPING -e 2025-1-1  MOHAMMED  &&  sudo  passwd  MOHAMMED
  214  sudo useradd  -c "Sales representative", -G SALES -e 2025-1-1  HANAN  &&  sudo  passwd  HANAN

----------------------------------------------------------------------------------------------------------------------

  215  sudo cat /etc/group
  216  sudo cat /etc/shadow
  217  sudo cat /etc/passwd

----------------------------------------------------------------------------------------------------------------------

<img width="215" alt="Screenshot 2022-10-12 154138" src="https://user-images.githubusercontent.com/60838224/195348188-f135ea26-4c18-4b23-8fea-a49d532e2d7d.png">

----------------------------------------------------------------------------------------------------------------------

<img width="470" alt="Screenshot 2022-10-12 154226" src="https://user-images.githubusercontent.com/60838224/195348205-3edc5d20-a434-4c22-95be-3f6cf38f7520.png">

----------------------------------------------------------------------------------------------------------------------

<img width="346" alt="Screenshot 2022-10-12 154342" src="https://user-images.githubusercontent.com/60838224/195348252-b4d5b5ac-b422-43e2-b541-5c71cb1cc7f4.png">

----------------------------------------------------------------------------------------------------------------------
