var robot_state = {
    "cutter": false,
    "light": false,
    "notification": false,
    "wheels" : {
        "left": 0,
        "right": 0,
    },
    "camera" : 0
};

var Socket = new WebSocket("ws://localhost:8888/robot_server/commands/");

$(document).ready(function() {
    $("#cutter").on("click", function(e){
        robot_state.cutter = !robot_state.cutter;
        Socket.send(JSON.stringify({"cutter": robot_state.cutter}));
    });
    $("#light").on("click", function(e){
        robot_state.light = !robot_state.light;
        Socket.send(JSON.stringify({"light": robot_state.light}));
    });
    $("#notification").on("click", function(e){
        robot_state.notification = !robot_state.notification;
        Socket.send(JSON.stringify({"notification": robot_state.notification}));
    });

    $("#wheelsRightPlus").on("click", function(e){
        if (robot_state.wheels.right < 255) {
            robot_state.wheels.right = robot_state.wheels.right + 1;
            message = JSON.stringify({"wheels": {"right": robot_state.wheels.right}});
            console.log("sending " + message);
            Socket.send(message);
        }
    });
    $("#wheelsRightMinus").on("click", function(e){
        if (robot_state.wheels.right > 0) {
            robot_state.wheels.right = robot_state.wheels.right - 1;
            message = JSON.stringify({"wheels": {"right": robot_state.wheels.right}});
            console.log("sending " + message);
            Socket.send(message);
        }
    });
    $("#wheelsLeftPlus").on("click", function(e){
        if (robot_state.wheels.left < 255) {
            robot_state.wheels.left = robot_state.wheels.left + 1;
            message = JSON.stringify({"wheels": {"left": robot_state.wheels.left}});
            console.log("sending " + message);
            Socket.send(message);
        }
    });
    $("#wheelsLeftMinus").on("click", function(e){
        if (robot_state.wheels.left > 0) {
            robot_state.wheels.left = robot_state.wheels.left - 1;
            message = JSON.stringify({"wheels": {"left": robot_state.wheels.left}});
            console.log("sending " + message);
            Socket.send(message);
        }
    });
    $("#cameraLeft").on("click", function(e){
        if (robot_state.camera > 0) {
            robot_state.camera = robot_state.camera - 1;
            message = JSON.stringify({"camera": robot_state.camera});
            console.log("sending " + message);
            Socket.send(message);
        }
    });
    $("#cameraRight").on("click", function(e){
        if (robot_state.camera < 180) {
            robot_state.camera = robot_state.camera + 1;
            message = JSON.stringify({"camera": robot_state.camera});
            console.log("sending " + message);
            Socket.send(message);
        }
    });
});
