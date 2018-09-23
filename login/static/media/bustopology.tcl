set ns [new Simulator]
set nf [open out.nam w]
$ns namtrace-all $nf
proc finish {} {
     	global ns nf
        $ns flush-trace
        close $nf
        exec nam out.nam &
        exit 0
}
$ns at 5.0 "finish"
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]
set n6 [$ns node]
set lan0 [$ns newLan "$n0 $n1 $n2 $n3 $n4 $n5 $n6" 0.7Mb 20ms LL Queue/FQ MAC/Csma/Cd Channel]
set src [new Agent/TCP]
$ns attach-agent $n6 $src
set des5 [new Agent/TCPSink]
$ns attach-agent $n3 $des5
$ns connect $src $des5
set rate [new Application/Traffic/CBR]
$rate set packetsize_ 300
$rate set interval_ 0.05
$rate attach-agent $src
$ns at 0.1 "$rate start"
$ns run
