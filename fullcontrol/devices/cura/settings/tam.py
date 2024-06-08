default_initial_settings = {
    "name": "Series 1 2014",
    "manufacturer": "TypeAMachines",
    "start_gcode": ";-- START GCODE --\n;Sliced for Type A Machines Series 1\n;Basic settings:\nG21 ;metric values\nG90 ;absolute positioning\nG28 ;move to endstops\nG29 ;allows for auto-levelling\nG1 Z15.0 F12000 ;move the platform down 15mm\nG1 X150 Y5 F9000 ;center\nM140 S{data['bed_temp']} ;Prep Heat Bed\nM109 S{data['nozzle_temp']} ;Heat To temp\nM190 S{data['bed_temp']} ;Heat Bed to temp\nG1 X150 Y5 Z0.3 ;move the platform to purge extrusion\nG92 E0 ;zero the extruded length\nG1 F200 X250 E30 ;extrude 30mm of feed stock\nG92 E0 ;zero the extruded length again\nG1 X150 Y150  Z25 F12000 ;recenter and begin\nG1 F9000",
    "end_gcode": "M104 S0 ;extruder heater off\nM140 S0 ;heated bed heater off (if you have it)\nG91 ;relative positioning\nG1 E-1 F300  ;retract the filament a bit before lifting the nozzle, to release some of the pressure\nG1 Z+0.5 E-5 X-20 Y-20 F9000 ;move Z up a bit and retract filament even more\nG28 X0 Y0 ;move X/Y to min endstops, so the head is out of the way\nM84 ;steppers off\nG90 ;absolute positioning",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 305,
    "build_volume_y": 305,
    "build_volume_z": 305,
}