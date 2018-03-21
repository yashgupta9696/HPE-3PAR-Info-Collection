# HPE_work
****SEE RAW FOR BETTER VIEW****

Used to fetch all the details from 3PAR using a Tkinter GUI. 
Just type "python cpg_info_all.py" to start the script.
It will ask the user about the different IP Addresses of the 3PAR(s) and the corresponding username(s) and password(s).
On the next window it will ask the user about the type of information he/she wants.

On executing the file "cpg_info_all.py" it will create the folders of each 3PAR with the name of the IP Address of the 3PAR having all the required information as requested by the user.
It will also contain a .zip file in each folder having all the .txt files in it.

The commands which are used to generate the information files are as follows:

------------------>>NODE INFO

servicenode status
showauthparam
showbattery
showcim
showdate
showdomain -d
showhost -d
showhost -chap
showiscsisession
showlicense
shownet
shownet -d
shownode -d
shownode -i
showport
showport -c
showport -i
showport -iscsi
showport -iscsiname
showport -par
showport -rc
showport -sfp
showport -sfp -d
showport -sfp -ddm
showportarp
showportdev
showportisns
showrcopy -d
showsched -all
showsnmpmgr
showsys -d
showsys -param
showsys -space
showtask
showsysmgr
showsysmgr -l
showtoc
showversion
controlencryption status
showflashcache
showsr
showsralertcrit
showwsapi
controlrecoveryauth status
showinventory -svc

----------------->>CAGE INFO

showcage -d
showcage -sfp
showcage -sfp -ddm
showcage -sfp -d
showpd
showpd -c
showpd -i
showpd -s

----------------->>VOLUME INFO

showcpg
showcpg -r
showcpg -sag
showcpg -sdg
showcpg -space
showhostset
showld
showld -d
showdomainset
showspace
showspace -cpg
showtemplate
showvlun
showvv
showvv -d
showvv -p
showvv -r
showvv -s
showvv -p -prov dds
showvvcpg
showvvset
showqos
showflashcache -vvset
showvasa
showvvolsc
showfed


