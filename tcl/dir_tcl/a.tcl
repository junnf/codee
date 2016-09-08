#!/bin/tclsh
#Thread 
package require Thread
package require Ttrace

###math builtin func
namespace import ::tcl::mathfunc::


#read *.log
set fldes [open "some.log" ]
# set fld [open "test.file" "w+"]

set count $argc
# you can use sed in tclsh
# exec sed s/text/tall/g test.file > new.file 

# set test_switch 2
# switch $test_switch {
    # 1 { puts $test_switch }
    # default {
        # $test_switch
    # }
# }

if { $argc > 1 } {
    puts "error,you should enter one parameter at\n\
    least,and try again!"
} elseif { $argc == 1 } {
    if { $argv == "-pid" } {
    puts "pid here"
    set text [ read $fldes ]
    regexp {([0-9]+)} $text res
    puts "Your pid:$res"

} elseif { $argv == "-help" } {
    puts " Dear developer,you can get a man-page from \
    this section! \ngood luck"
}
  elseif { $argv == "-thread" } {
    #test thread 

  
  }
} else {
    puts "error,you should try again!"
}

