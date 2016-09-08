#!/bin/tclsh
package require Thread
package require Ttrace

#read *.log
set fldes [open "some.log" ]
# set fld [open "test.file" "w+"]

set count $argc
# you can use sed in tclsh
# exec sed s/text/tall/g test.file > new.file 

# set test_switch 1
# switch $test_switch {
    # 1 { puts $test_switch }
    # default {
        # puts "aaa"
    # }
# }

if { $argc > 1 } {
    puts "error,you should try again!"
} elseif { $argc == 1 } {
    if { $argv == "-pid" } {
    puts "pid here"
    set text [ read $fldes ]
    regexp {([0-9]+)} $text res
    puts "Your pid:$res"

} elseif { $argv == "-help" } {
    puts " Dear developer,you can get a man-page from this section! \ngood luck"
}
} else {
    puts "error,you should try again!"
}

