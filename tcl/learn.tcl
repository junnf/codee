#!/bin/tclsh
package require Thread
package require Ttrace

#read *.log
set fldes [open "some.log" ]

set count $argc
if { $argc > 1 } {
    puts "error,you should try again!"
} elseif { $argc == 1 } {
    if { $argv == "-pid" } {
    puts "pid here"
    set text [ read $fldes ]
    regexp {([0-9]+)} $text res
    puts "进程id为:$res"

} elseif { $argv == "-help" } {
    puts " Dear developer,you can get a man-page from this section! \ngood luck"
}
} else {
    puts "error,you should try again!"
}

