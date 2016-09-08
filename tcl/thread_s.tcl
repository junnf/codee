#!/usr/bin/tclsh
package require Thread

thread::create {
    package require fileutil

    set files [fileutil::findByPattern [pwd] *.tcl]

    set fid [open files.txt w]
    # puts $fid [join $files]
    puts $files
    close $fid

}
