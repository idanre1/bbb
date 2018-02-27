//https://github.com/jadonk/node-roboticscape

var rc = require('roboticscape');

/* Allocate the userspace usage of the robotics cape features */
rc.initialize();

/* Set the state to RUNNING */
rc.state("RUNNING");

/* Exercise the robotics cape hardware */
rc.led("GREEN", true);
rc.on("PAUSE_PRESSED", function() { 
    console.log("PAUSE pressed");
    
    /* Set the state to EXITING */
    rc.state("EXITING");
});
rc.motor("ENABLE");
rc.motor(1,0.3);

/* Read encoder every second until PAUSE button pressed */
setInterval(function() {
    if(rc.state() == "RUNNING") {
//        var enc1 = rc.encoder(1);
        console.log("encoder 1 = ");
    } else {
        /* The robotics cape userspace interface is automatically freed on exit */
        process.exit();
    }
}, 1000);