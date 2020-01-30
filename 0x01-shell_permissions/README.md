# 0x01-shell_permissions
  This project is all about permissions in the shell, and the nightmares that come with them.

0.My name is Betty

Created a script that changed the user ID to betty.
 
  su betty


1. Who am I

Wrote a script that prints the effective userid of the current user.

whoami


2. Groups

Wrote a script that prints all the groups the current user is part of.

groups


3. New owner

Wrote a script that changes the owner of the file hello to the user betty.

sudo chown betty hello


4. Empty!

Wrote a script that creates an empty file called hello.

touch hello


5.Execute

Wrote a script that adds execute permission to the owner of the file hello.

chmod u+x hello


6.Multiple permissions

Wrote a script taht adds execute permission to the owner and the group owner, and read permission to other users, to th
e file hello.

chmod ug+x,o+r hello


7.Everbody!

Wrote a script that adds execution permission to the owner, the group owner and the other users, to the file hello
chmod ugo+x hello


8. James Bond

Wrote a script that sets the permission to the file hello with no permission for owner and group, and all permissions  for other users. No commas allowed for this exercise. The file is in the working directory.

chmod 007 hello


9.John Doe

Wrote a script that sets the mode of the file hello to the following:
-rwxr-x-wx

chmod 753 hello


10.Look in the mirror

Wrote a script that sets the mode of the file hello the same as olleh's mode. Both files are in the current working d  
irectory.

chmod --reference=olleh hello


11.Directories

Created a script that adds execute permission to all subdirectories of the current directory for the owner, the group  
owner and all other users. Regular files should not be changed.

chmod -R a+X *


12.More directories

Created a script that creates a directory called dir_holberton with permissions 751 in the working directory.

mkdir -m 751 dir_holberton


13.Change group

Wrote a script that changes the group owner to holberton for the file hello. Hello is in the current working director  y.

chgrp holberton hello


14.Owner and group

Wrote a script that changes the owner to betty and the group owner to holberton for all the files and directories in   
the working directory.

chown betty:holberton *


15.Symbolic links

Write a script that changes the owner and the group owner of the file _hello to betty and holberton respectively. _hell
o is in the current working directory, and is a symbolic link.

sudo chown -h betty:holberton _hello


16.If only

Wrote a script that changes the owner of the file hello to betty only if it is owned by the user guillaume. hello is in
the current working directory.

sudo chown --from=guillaume betty hello


17.Star Wars

Wrote a script that plays Star Wars: A New Hope in the terminal.

telnet towel.blinkenlights.nl


18.RTFM

Created a man page that is identical to the example.

Check the file.

  