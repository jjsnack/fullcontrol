default_initial_settings = {
    "name": "ELEGOO NEPTUNE 4",
    "manufacturer": "ELEGOO",
    "start_gcode": ";ELEGOO NEPTUNE 4 / 4 PRO\nM220 S100 ;Set the feed speed to 100%\nM221 S100 ;Set the flow rate to 100%\nM104 S140 ;Start heating extruder\nM190 S{data['bed_temp']} ;Wait for the bed to reach print temp\nG90\nG28 ;home\nG1 Z10 F300\nG1 X67.5 Y0 F6000\nG1 Z0 F300\nM109 S{data['nozzle_temp']} ;Wait for extruder to reach print temp\nG92 E0 ;Reset Extruder\nG1 X67.5 Y0 Z0.4 F300 ;Move to start position\nG1 X167.5 E30 F400 ;Draw the first line\nG1 Z0.6 F120.0 ;Move to side a little\nG1 X162.5 F3000\nG92 E0 ;Reset Extruder",
    "end_gcode": "G91 ;Relative positionning\nG1 E-2 F2700 ;Retract a bit\nG1 E-2 Z0.2 F2400 ;Retract and raise Z\nG1 X5 Y5 F3000 ;Wipe out\nG1 Z2 ;Raise Z more\nG90 ;Absolute positionning\nG1 X0 Y{data['build_volume_y'] - 5} ;Present print\nM106 S0 ;Turn-off fan\nM104 S0 ;Turn-off hotend\nM140 S0 ;Turn-off bed\nM84 X Y E ;Disable all steppers but Z",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 250,
    "travel_speed": 250,
    "dia_feed": 1.75,
    "build_volume_x": 235,
    "build_volume_y": 230,
    "build_volume_z": 270,
}
