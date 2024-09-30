# Installing MySQL Workbench and MariaDB

<iframe src="https://share.descript.com/embed/MMUOjJ2Ggjt" width="640" height="360" frameborder="0" allowfullscreen></iframe>

### Links
- [MySQL :: Download MySQL Workbench](https://dev.mysql.com/downloads/workbench/)
	- *If you have an newer mac (M1 Chip) use macOS (ARM, 64-bit)
- [Download MariaDB Server - MariaDB.org](https://mariadb.org/download/?t=mariadb&p=mariadb&r=11.4.2&os=windows&cpu=x86_64&pkg=msi&mirror=xtom_fre)

### Mac Only Links
- [Homebrew — The Missing Package Manager for macOS (or Linux)](https://brew.sh/)
- [Installing MariaDB Server on macOS Using Homebrew - MariaDB Knowledge Base](https://mariadb.com/kb/en/installing-mariadb-on-macos-using-homebrew/)
- *I'm aware that this process on mac is a bit tricky. If you're having trouble don't burn too much time on it, feel free to reach out to me and I can get you set up with with hosting on PHPMyAdmin.*

Commands to set password on MariaDB (Mac only):
```sql
ALTER USER 'root'@'localhost' IDENTIFIED BY 'your_new_password';
FLUSH PRIVILEGES;
```

### Windows Only Links
[Latest supported Visual C++ Redistributable downloads | Microsoft Learn](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)

*This may be necessary if it is not already installed on your system. Click download and check the x64 box. Run the installation. You may also need to restart your machine afterwards.*

<img src="https://raw.githubusercontent.com/kellerflint/Class-Intro-SQL/hugo/content/SQL-Files/Images/VS2015-2022-Redistrib.png">

### Back: [[SQL Analytics M2 - Basic Querying]]