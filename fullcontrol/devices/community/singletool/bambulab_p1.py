from fullcontrol.gcode import Point, Printer, Extruder, ManualGcode, PrinterCommand, GcodeComment, Buildplate, Hotend, Fan, StationaryExtrusion
import fullcontrol.gcode.printer_library.singletool.base_settings as base_settings


def set_up(user_overrides: dict):
    ''' DO THIS
    '''

    # overrides for this specific printer relative those defined in base_settings.py
    printer_overrides = {
        "model_height": 250,
        "bed_type": "Textured PEI Plate",
        "print_speed": 1000,
        "travel_speed": 5000,
        "area_model": "rectangle",
        "extrusion_width": 0.4,
        "extrusion_height": 0.2,
        "nozzle_temp": 220,
        "bed_temp": 55,
        "parts_fan_percent": 50,
        "aux_fan_percent": 0,
        "chamber_fan_percent":30,
        "print_speed_percent": 100,
        "material_flow_percent": 100,
        "e_units": "mm",  # options: "mm" / "mm3"
        "relative_e": True,
        "manual_e_ratio": None,
        "dia_feed": 1.75,
        "travel_format": "G0",  # options: "G0" / "G1_E0"
        "primer": "front_lines_then_y",
        "printer_command_list": {
            "home": "G28 ; home axes",
            "retract": "G10 ; retract",
            "unretract": "G11 ; unretract",
            "absolute_coords": "G90 ; absolute coordinates",
            "relative_coords": "G91 ; relative coordinates",
            "units_mm": "G21 ; set units to millimeters"
        }
    }

    # update default initialization settings with printer-specific overrides and user-defined overrides
    initialization_data = {**base_settings.default_initial_settings, **printer_overrides}
    initialization_data = {**initialization_data, **user_overrides}


    # STARTING PROCEDURE

    starting_procedure_steps = []
    starting_procedure_steps.append(ManualGcode(
        text='; Time to print!!!!!\n; GCode created with FullControl - tell us what you\'re printing!\n; info@fullcontrol.xyz or tag FullControlXYZ on Twitter/Instagram/LinkedIn/Reddit/TikTok \n'))
    starting_procedure_steps.append(ManualGcode(
        text='; For BambuLab P1 Printers, when using custom GCode, the first print after start-up may stop extruding shortly after starting. Just re-print\n'))
    
    # printer resets
    starting_procedure_steps.append(ManualGcode(text='\n; printer resets\n'))
    starting_procedure_steps.append(PrinterCommand(id='relative_coords'))
    starting_procedure_steps.append(ManualGcode(text='M17 Z0.4 ; lower the z-motor current'))
    starting_procedure_steps.append(ManualGcode(text='G380 S2 Z30 F300 ; G380 is same as G38; lower the hotbed , to prevent the nozzle is below the hotbed'))
    starting_procedure_steps.append(ManualGcode(text='G380 S2 Z-25 F300 ;'))
    starting_procedure_steps.append(ManualGcode(text='G1 Z5 F300;'))
    starting_procedure_steps.append(PrinterCommand(id='absolute_coords'))
    starting_procedure_steps.append(ManualGcode(text='M220 S100 ;Reset Feedrate'))
    starting_procedure_steps.append(ManualGcode(text='M221 S100 ;Reset Flowrate'))
    starting_procedure_steps.append(ManualGcode(text='M73.2   R1.0 ;Reset left time magnitude'))
    starting_procedure_steps.append(ManualGcode(text='M221 X0 Y0 Z0 ; turn off soft endstop to prevent protential logic problem'))
    starting_procedure_steps.append(ManualGcode(text='G29.1 Z{+0.0} ; clear z-trim value first'))
    starting_procedure_steps.append(ManualGcode(text='M204 S10000 ; init ACC set to 10m/s^2'))

    # start bed and toolhead heating
    starting_procedure_steps.append(Buildplate(temp=initialization_data["bed_temp"], wait=False))
    starting_procedure_steps.append(Hotend(temp=250, wait=False))
    starting_procedure_steps.append(Buildplate(temp=initialization_data["bed_temp"], wait=True))
    
    # prepare print temperature and material
    starting_procedure_steps.append(PrinterCommand(id='relative_coords'))
    starting_procedure_steps.append(ManualGcode(text='G0 Z10 F1200'))
    starting_procedure_steps.append(PrinterCommand(id='absolute_coords'))
    starting_procedure_steps.append(ManualGcode(text='G28 X'))
    starting_procedure_steps.append(ManualGcode(text='M975 S1 ; turn on magic'))
    starting_procedure_steps.append(ManualGcode(text='G1 X60 F12000'))
    starting_procedure_steps.append(ManualGcode(text='G1 Y245'))
    starting_procedure_steps.append(ManualGcode(text='G1 Y265 F3000'))
    
    # purge filament
    starting_procedure_steps.append(ManualGcode(text='M412 S1 ; turn on filament runout detection'))
    starting_procedure_steps.append(Hotend(temp=250, wait=True))
    starting_procedure_steps.append(Fan(speed_percent=0))
    starting_procedure_steps.append(ManualGcode(text='G92 E0'))
    starting_procedure_steps.append(StationaryExtrusion(volume=50, speed=200))
    starting_procedure_steps.append(ManualGcode(text='M400'))
    starting_procedure_steps.append(Hotend(temp=initialization_data["nozzle_temp"], wait=False))
    starting_procedure_steps.append(ManualGcode(text='G92 E0'))
    starting_procedure_steps.append(StationaryExtrusion(volume=50, speed=200))
    starting_procedure_steps.append(ManualGcode(text='M400'))
    starting_procedure_steps.append(Fan(speed_percent=100))
    starting_procedure_steps.append(ManualGcode(text='G92 E0'))
    starting_procedure_steps.append(StationaryExtrusion(volume=25, speed=300))
    starting_procedure_steps.append(ManualGcode(text=f'M109 S{initialization_data["nozzle_temp"] - 25} ; drop nozzle temp, make filament shrink a bit'))
    starting_procedure_steps.append(ManualGcode(text='G92 E0'))
    starting_procedure_steps.append(ManualGcode(text='G1 E-1 F300'))

    # nozzle wipe
    starting_procedure_steps.append(ManualGcode(text='G1 X70 F9000'))
    starting_procedure_steps.append(ManualGcode(text='G1 X76 F15000'))
    starting_procedure_steps.append(ManualGcode(text='G1 X65 F15000'))
    starting_procedure_steps.append(ManualGcode(text='G1 X76 F15000'))
    starting_procedure_steps.append(ManualGcode(text='G1 X65 F15000; shake to put down garbage'))
    starting_procedure_steps.append(ManualGcode(text='G1 X80 F6000'))
    starting_procedure_steps.append(ManualGcode(text='G1 X95 F15000'))
    starting_procedure_steps.append(ManualGcode(text='G1 X80 F15000'))
    starting_procedure_steps.append(ManualGcode(text='G1 X165 F15000; wipe and shake'))
    starting_procedure_steps.append(ManualGcode(text='M400'))
    starting_procedure_steps.append(Fan(speed_percent=0))

    # wipe nozzle procedure
        
    # home toolhead
    starting_procedure_steps.append(PrinterCommand(id='home'))
    starting_procedure_steps.append(PrinterCommand(id='absolute_coords'))
    starting_procedure_steps.append(PrinterCommand(id='units_mm'))
    starting_procedure_steps.append(Extruder(relative_gcode=initialization_data["relative_e"]))
    starting_procedure_steps.append(Point(x=20, y=30, z=10)) # updated from (20, 20, 10) to (20, 30, 10)
    starting_procedure_steps.append(ManualGcode(text='G92 X0 Y0 ; offset print to avoid filament cutting area'))
    starting_procedure_steps.append(Point(x=5, y=5, z=10))

    # set hotend temperature
    starting_procedure_steps.append(ManualGcode(text='\n; set hot end temperature\n'))
    starting_procedure_steps.append(Hotend(temp=initialization_data["nozzle_temp"], wait=True))
    starting_procedure_steps.append(Extruder(on=False))

    # lower bed for PEI plate
    starting_procedure_steps.append(ManualGcode(text='\n; lower bed for PEI plate\n'))
    if initialization_data["bed_type"] == "Textured PEI Plate":
        starting_procedure_steps.append(ManualGcode(text='G29.1 Z{-0.04} ; for Textured PEI Plate'))

    # wait for extrude temperature, set fan and travel speed
    starting_procedure_steps.append(ManualGcode(text='\n; wait for hot end temperature\n'))
    starting_procedure_steps.append(ManualGcode(text=f'M106 P2 S{initialization_data["aux_fan_percent"]} ; enable aux fan'))
    starting_procedure_steps.append(Fan(speed_percent=initialization_data["parts_fan_percent"]))
    starting_procedure_steps.append(ManualGcode(text='M975 S1 ; turn on mech mode supression'))
    starting_procedure_steps.append(Printer(travel_speed=initialization_data["travel_speed"]))
    starting_procedure_steps.append(Point(x=10.0, y=10.0, z=0.2))
    starting_procedure_steps.append(Extruder(on=True))

    # set print speed and material flow
    starting_procedure_steps.append(ManualGcode(text='\n; set print speed and flow\n'))
    starting_procedure_steps.append(ManualGcode(
        text='M220 S' + str(initialization_data["print_speed_percent"])+' ; set speed factor override percentage'))
    starting_procedure_steps.append(ManualGcode(
        text='M221 S' + str(initialization_data["material_flow_percent"])+' ; set extrude factor override percentage'))
    
    starting_procedure_steps.append(ManualGcode(text=';==========\n; END OF STARTING PROCEDURE\n;==========\n'))


    # ENDING PROCEDURE

    ending_procedure_steps = []
    ending_procedure_steps.append(ManualGcode(text='\n;==========\n; START OF ENDING PROCEDURE\n;==========\n'))
    ending_procedure_steps.append(ManualGcode(text='M400 ; wait for buffer to clear'))
    ending_procedure_steps.append(ManualGcode(text='M83\nG0 E-0.8 F1800 ; retract'))
    
    # move toolhead
    ending_procedure_steps.append(ManualGcode(text='\n; move toolhead\n'))
    starting_procedure_steps.append(PrinterCommand(id='relative_coords'))
    ending_procedure_steps.append(ManualGcode(text='G0 Z1 F900 ; drop bed a little'))
    starting_procedure_steps.append(PrinterCommand(id='absolute_coords'))
    ending_procedure_steps.append(ManualGcode(text='G1 X65 Y245 F12000 ; move to safe position'))
    ending_procedure_steps.append(ManualGcode(text='G1 Y265 F3000'))
    ending_procedure_steps.append(ManualGcode(text='G1 X65 Y245 F12000'))
    ending_procedure_steps.append(ManualGcode(text='G1 Y265 F3000'))
    
    # turn heat bed and fans off
    ending_procedure_steps.append(ManualGcode(text='\n; turn heat bed and fans off\n'))
    ending_procedure_steps.append(Buildplate(temp=0, wait=False))
    ending_procedure_steps.append(Fan(speed_percent=0))
    ending_procedure_steps.append(ManualGcode(text='M106 P2 S0 ; disable aux fan'))
    ending_procedure_steps.append(ManualGcode(text='M106 P3 S0 ; disable chamber fan'))
    
    # wipe
    ending_procedure_steps.append(ManualGcode(text='\n; wipe nozzle\n'))
    ending_procedure_steps.append(ManualGcode(text='G1 X100 F12000 ; wipe'))
    ending_procedure_steps.append(ManualGcode(text='G1 X20 Y50 F12000'))
    ending_procedure_steps.append(ManualGcode(text='G1 Y-3'))
    ending_procedure_steps.append(ManualGcode(text='G1 X65 F12000'))
    ending_procedure_steps.append(ManualGcode(text='G1 Y265'))
    ending_procedure_steps.append(ManualGcode(text='G1 X100 F12000 ; wipe'))
    
    # turn off hot end
    ending_procedure_steps.append(ManualGcode(text='\n; turn off hotend\n'))
    ending_procedure_steps.append(Hotend(temp=0, wait=False))
    
    # move bed down
    ending_procedure_steps.append(ManualGcode(text='\n; move bed down\n'))
    model_height = initialization_data["model_height"]
    ending_procedure_steps.append(ManualGcode(text='M400 ; wait for buffer to clear'))
    ending_procedure_steps.append(ManualGcode(text='M17 S'))
    ending_procedure_steps.append(ManualGcode(text='M17 Z0.4 ; lower z motor current to reduce impact if there is something in the bottom'))
    if (model_height + 1 + 50.0) < 250.0:
        ending_procedure_steps.append(ManualGcode(text=f'G1 Z{model_height + 50} F600'))
        ending_procedure_steps.append(ManualGcode(text=f'G1 Z{model_height + 48}'))
    else:
        ending_procedure_steps.append(ManualGcode(text='G1 Z250 F600'))
        ending_procedure_steps.append(ManualGcode(text='G1 Z248'))    
    ending_procedure_steps.append(ManualGcode(text='M400 P100'))
    ending_procedure_steps.append(ManualGcode(text='M17 R ; restore z current'))
    
    # park toolhead
    ending_procedure_steps.append(ManualGcode(text='\n; park toolhead\n'))
    starting_procedure_steps.append(PrinterCommand(id='absolute_coords'))
    ending_procedure_steps.append(ManualGcode(text='G1 X128 Y250 F3600'))
    
    # reset
    ending_procedure_steps.append(ManualGcode(text='\n; reset printer\n'))
    ending_procedure_steps.append(ManualGcode(text='M221 S100 ; reset flow'))
    ending_procedure_steps.append(ManualGcode(text='M201.2 K1.0 ; Reset acc magnitude'))
    ending_procedure_steps.append(ManualGcode(text='M73.2 R1.0 ; Reset left time magnitude'))
    ending_procedure_steps.append(ManualGcode(text='M900 K0 ; reset LA'))
    ending_procedure_steps.append(ManualGcode(text='M84 ; disable steppers'))


    # FIN

    initialization_data['starting_procedure_steps'] = starting_procedure_steps
    initialization_data['ending_procedure_steps'] = ending_procedure_steps

    return initialization_data
