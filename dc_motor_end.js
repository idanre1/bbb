//https://github.com/jadonk/node-roboticscape

var rc = require('roboticscape');

/* Allocate the userspace usage of the robotics cape features */
rc.initialize();

/* Set the state to RUNNING */
rc.state("EXITING");
