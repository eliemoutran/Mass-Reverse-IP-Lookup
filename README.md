# Mass Reverse IP Lookup

Description
------------
MRIL (Mass Reverse IP Lookup) is a multithreaded python tool to reverse ip lookup a list of ip addresses using yougetsignal.com.

Requirements
-------------
* Python 3.x.x

Installing Dependencies
-------------
`pip install requests`

Examples
-------------
* Simple port knocking example: 
`python MRIL.py`

```
******************************************************
*                                                    *
*  __  __ _____  _____ _                             *
* |  \/  |  __ \|_   _| |                            *
* | \  / | |__) | | | | |                            *
* | |\/| |  _  /  | | | |                            *
* | |  | | | \ \ _| |_| |____                        *
* |_|  |_|_|  \_\_____|______|                       *
*                                                    *
* Mass Reverse IP Lookup                             *
* Coded by thebish0p                                 *
* https://github.com/thebish0p/                      *
******************************************************

[*] Enter ip addresses file: ipaddr.txt
[*] Enter number of threads: 5
[*] Reversing 172.217.18.174 ...
[*] Reversing 199.83.128.77 ...
[*] Reversing 104.18.155.3 ...
[*] No domains for 172.217.18.174
[*] 2 domains found for 104.18.155.3
[*] 27 domains found for 199.83.128.77
******************************************************
[*] Scan is done
[*] Output file: /root/Desktop/MRIL/output.txt
******************************************************
```
