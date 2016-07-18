### mysql-remote-backup

Backup a remote mysql database.

    Usage:
    
        fab backup:dbname=<dbname>,dbuser=<dbuser>,dbpass=<dbpass>

        Optional arguments:
            remote_backup_path : Defaults to /tmp/bak/<dbname>
            local_backup_path  : Defaults to /tmp/bak/<dbname>

    Example: 
    
        $ fab backup:dbname=x-account-database,dbuser=x-user-john,dbpass=x-pass-john
        # Backup x-account-database to /tmp/bak/x-account-database remotely and locally

### Integrate with launchd (OSX)

1. Copy `config/launchd-example.plist.default` to `~/Library/LaunchAgents/any-name.plist`
2. Open `~/Library/LaunchAgents/any-name.plist` and edit the boilerplate settings
3. Load the plist with launchctl to register it as an Agent/Daemon
    
        launchctl load ~/Library/LaunchAgents/any-name.plist

4. By default, the command is scheduled to run everyday at 00:00. If your computer is not awake at 00:00, launchd will start the job the next time the computer wakes up.
        
For more information on launchd, see your local manuals:

- launchctl(1)
- launchd.plist(5)

### License

The MIT License (MIT)

Copyright (c) 2016 Hank Ehly

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
