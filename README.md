# Robot Server

A simple remote control for controlling a robot that polls an API endpoint for commands.

Note: the remote control, i.e. the browser controlling the UI, needs to have websockets enabled.

## Endpoints

<table>
<tr>
    <td><a href="http://localhost:8888/robot_server/">http://localhost:8888/robot_server/<a></td>
    <td>Web UI</td>
</tr>
<tr>
    <td><a href="http://localhost:8888/robot_server/out.json">http://localhost:8888/robot_server/out.json</a></td>
    <td>endpoint for robot to poll on</td>
</tr>
</table>
