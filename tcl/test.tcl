#!/usr/bin/tclsh
package req Thread
package req Ttrace

for {set i 0} {$i < 4} {incr i} {
    set tid($i) [thread::create -preserved]
}

ttrace::eval {
    proc foo args {
        puts foo
    }
    proc bar args {
        puts bar
    }
}
