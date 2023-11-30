import arcpy
import os

def create_gdb(folder_path, gdb_name):
    gdb_path = os.path.join(folder_path, gdb_name)
    if not arcpy.Exists(gdb_path):
        arcpy.CreateFileGDB_management(folder_path, gdb_name)
    return gdb_path


def import_csv_to_gdb(gdb_path, csv_path, route_layer_name):
    bus_stops = arcpy.MakeXYEventLayer_management(csv_path, 'Longitude', 'Latitude', route_layer_name)
    input_layer = bus_stops
    arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
    return gdb_path + '\\' + route_layer_name


def make_excel_route_analysis_layer(params):
    try:
        arcpy.MakeRouteAnalysisLayer_na(*params)
        print("Route analysis layer created successfully.")
        travel_modes = arcpy.na.GetTravelModes(network)
        # Construct a new TravelMode object from the existing Driving Time travel mode
        new_travel_mode = arcpy.na.TravelMode(travel_modes["Driving Time"])
        # Update the uTurns property to turn uTurns off, and update the name
        new_travel_mode.name = "Driving Time without uTurns"
        new_travel_mode.uTurns = "NO_UTURNS"
        # Use the new travel mode object when creating an route analysis layer
        arcpy.MakeRouteAnalysisLayer_na(network, new_excel_route_name, new_travel_mode, "PRESERVE_BOTH", None, "UTC", "ALONG_NETWORK", None, "DIRECTIONS", "UTC", "SKIP")
        print("Route analysis layer no uturns created successfully")
        return True
    except arcpy.ExecuteError:
        print(arcpy.GetMessages(2))
        return False


def make_hullabaloo_route_analysis_layer(params):
    try:
        arcpy.MakeRouteAnalysisLayer_na(*params)
        print("Route analysis layer created successfully.")
        travel_modes = arcpy.na.GetTravelModes(network)
        # Construct a new TravelMode object from the existing Driving Time travel mode
        new_travel_mode = arcpy.na.TravelMode(travel_modes["Driving Time"])
        # Update the uTurns property to turn uTurns off, and update the name
        new_travel_mode.name = "Driving Time without uTurns"
        new_travel_mode.uTurns = "NO_UTURNS"
        # Use the new travel mode object when creating an route analysis layer
        arcpy.MakeRouteAnalysisLayer_na(network, new_hullabaloo_route_name, new_travel_mode, "PRESERVE_BOTH", None, "UTC", "ALONG_NETWORK", None, "DIRECTIONS", "UTC", "SKIP")
        print("Route analysis layer no uturns created successfully")
        return True
    except arcpy.ExecuteError:
        print(arcpy.GetMessages(2))
        return False
   
def make_matthewgaines_route_analysis_layer(params):
    try:
        arcpy.MakeRouteAnalysisLayer_na(*params)
        print("Route analysis layer created successfully.")
        travel_modes = arcpy.na.GetTravelModes(network)
        # Construct a new TravelMode object from the existing Driving Time travel mode
        new_travel_mode = arcpy.na.TravelMode(travel_modes["Driving Time"])
        # Update the uTurns property to turn uTurns off, and update the name
        new_travel_mode.name = "Driving Time without uTurns"
        new_travel_mode.uTurns = "NO_UTURNS"
        # Use the new travel mode object when creating an route analysis layer
        arcpy.MakeRouteAnalysisLayer_na(network, new_matthewgaines_route_name, new_travel_mode, "PRESERVE_BOTH", None, "UTC", "ALONG_NETWORK", None, "DIRECTIONS", "UTC", "SKIP")
        print("Route analysis layer no uturns created successfully")
        return True
    except arcpy.ExecuteError:
        print(arcpy.GetMessages(2))
        return False
   
def make_ringdance_route_analysis_layer(params):
    try:
        arcpy.MakeRouteAnalysisLayer_na(*params)
        print("Route analysis layer created successfully.")
        travel_modes = arcpy.na.GetTravelModes(network)
        # Construct a new TravelMode object from the existing Driving Time travel mode
        new_travel_mode = arcpy.na.TravelMode(travel_modes["Driving Time"])
        # Update the uTurns property to turn uTurns off, and update the name
        new_travel_mode.name = "Driving Time without uTurns"
        new_travel_mode.uTurns = "NO_UTURNS"
        # Use the new travel mode object when creating an route analysis layer
        arcpy.MakeRouteAnalysisLayer_na(network, new_ringdance_route_name, new_travel_mode, "PRESERVE_BOTH", None, "UTC", "ALONG_NETWORK", None, "DIRECTIONS", "UTC", "SKIP")
        print("Route analysis layer no uturns created successfully")
        return True
    except arcpy.ExecuteError:
        print(arcpy.GetMessages(2))
        return False


def make_oldarmy_route_analysis_layer(params):
    try:
        arcpy.MakeRouteAnalysisLayer_na(*params)
        print("Route analysis layer created successfully.")
        travel_modes = arcpy.na.GetTravelModes(network)
        # Construct a new TravelMode object from the existing Driving Time travel mode
        new_travel_mode = arcpy.na.TravelMode(travel_modes["Driving Time"])
        # Update the uTurns property to turn uTurns off, and update the name
        new_travel_mode.name = "Driving Time without uTurns"
        new_travel_mode.uTurns = "NO_UTURNS"
        # Use the new travel mode object when creating an route analysis layer
        arcpy.MakeRouteAnalysisLayer_na(network, new_oldarmy_route_name, new_travel_mode, "PRESERVE_BOTH", None, "UTC", "ALONG_NETWORK", None, "DIRECTIONS", "UTC", "SKIP")
        print("Route analysis layer no uturns created successfully")
        return True
    except arcpy.ExecuteError:
        print(arcpy.GetMessages(2))
        return False
   
def make_centurytree_route_analysis_layer(params):
    try:
        arcpy.MakeRouteAnalysisLayer_na(*params)
        print("Route analysis layer created successfully.")
        travel_modes = arcpy.na.GetTravelModes(network)
        # Construct a new TravelMode object from the existing Driving Time travel mode
        new_travel_mode = arcpy.na.TravelMode(travel_modes["Driving Time"])
        # Update the uTurns property to turn uTurns off, and update the name
        new_travel_mode.name = "Driving Time without uTurns"
        new_travel_mode.uTurns = "NO_UTURNS"
        # Use the new travel mode object when creating an route analysis layer
        arcpy.MakeRouteAnalysisLayer_na(network, new_centurytree_route_name, new_travel_mode, "PRESERVE_BOTH", None, "UTC", "ALONG_NETWORK", None, "DIRECTIONS", "UTC", "SKIP")
        print("Route analysis layer no uturns created successfully")
        return True
    except arcpy.ExecuteError:
        print(arcpy.GetMessages(2))
        return False
    
def make_rudder_route_analysis_layer(params):
    try:
        arcpy.MakeRouteAnalysisLayer_na(*params)
        print("Route analysis layer created successfully.")
        travel_modes = arcpy.na.GetTravelModes(network)
        # Construct a new TravelMode object from the existing Driving Time travel mode
        new_travel_mode = arcpy.na.TravelMode(travel_modes["Driving Time"])
        # Update the uTurns property to turn uTurns off, and update the name
        new_travel_mode.name = "Driving Time without uTurns"
        new_travel_mode.uTurns = "NO_UTURNS"
        # Use the new travel mode object when creating an route analysis layer
        arcpy.MakeRouteAnalysisLayer_na(network, new_rudder_route_name, new_travel_mode, "PRESERVE_BOTH", None, "UTC", "ALONG_NETWORK", None, "DIRECTIONS", "UTC", "SKIP")
        print("Route analysis layer no uturns created successfully")
        return True
    except arcpy.ExecuteError:
        print(arcpy.GetMessages(2))
        return False
    
def make_rellis_route_analysis_layer(params):
    try:
        arcpy.MakeRouteAnalysisLayer_na(*params)
        print("Route analysis layer created successfully.")
        travel_modes = arcpy.na.GetTravelModes(network)
        # Construct a new TravelMode object from the existing Driving Time travel mode
        new_travel_mode = arcpy.na.TravelMode(travel_modes["Driving Time"])
        # Update the uTurns property to turn uTurns off, and update the name
        new_travel_mode.name = "Driving Time without uTurns"
        new_travel_mode.uTurns = "NO_UTURNS"
        # Use the new travel mode object when creating an route analysis layer
        arcpy.MakeRouteAnalysisLayer_na(network, new_rellis_route_name, new_travel_mode, "PRESERVE_BOTH", None, "UTC", "ALONG_NETWORK", None, "DIRECTIONS", "UTC", "SKIP")
        print("Route analysis layer no uturns created successfully")
        return True
    except arcpy.ExecuteError:
        print(arcpy.GetMessages(2))
        return False

def make_fishcamp_route_analysis_layer(params):
    try:
        arcpy.MakeRouteAnalysisLayer_na(*params)
        print("Route analysis layer created successfully.")
        travel_modes = arcpy.na.GetTravelModes(network)
        # Construct a new TravelMode object from the existing Driving Time travel mode
        new_travel_mode = arcpy.na.TravelMode(travel_modes["Driving Time"])
        # Update the uTurns property to turn uTurns off, and update the name
        new_travel_mode.name = "Driving Time without uTurns"
        new_travel_mode.uTurns = "NO_UTURNS"
        # Use the new travel mode object when creating an route analysis layer
        arcpy.MakeRouteAnalysisLayer_na(network, new_fishcamp_route_name, new_travel_mode, "PRESERVE_BOTH", None, "UTC", "ALONG_NETWORK", None, "DIRECTIONS", "UTC", "SKIP")
        print("Route analysis layer no uturns created successfully")
        return True
    except arcpy.ExecuteError:
        print(arcpy.GetMessages(2))
        return False

def make_elephantwalk_route_analysis_layer(params):
    try:
        arcpy.MakeRouteAnalysisLayer_na(*params)
        print("Route analysis layer created successfully.")
        travel_modes = arcpy.na.GetTravelModes(network)
        # Construct a new TravelMode object from the existing Driving Time travel mode
        new_travel_mode = arcpy.na.TravelMode(travel_modes["Driving Time"])
        # Update the uTurns property to turn uTurns off, and update the name
        new_travel_mode.name = "Driving Time without uTurns"
        new_travel_mode.uTurns = "NO_UTURNS"
        # Use the new travel mode object when creating an route analysis layer
        arcpy.MakeRouteAnalysisLayer_na(network, new_elephantwalk_route_name, new_travel_mode, "PRESERVE_BOTH", None, "UTC", "ALONG_NETWORK", None, "DIRECTIONS", "UTC", "SKIP")
        print("Route analysis layer no uturns created successfully")
        return True
    except arcpy.ExecuteError:
        print(arcpy.GetMessages(2))
        return False

def add_locations_to_route(layer_name, stops):
    try:
        arcpy.AddLocations_na(layer_name, "Stops", stops)
        print("Locations added successfully.")
        return True
    except arcpy.ExecuteError:
        print(arcpy.GetMessages(2))
        return False


def calculate_field(layer_name, field, value, expression, field_type):
    try:
        arcpy.CalculateField_management(layer_name + "\\Stops", field, value, expression, None, field_type)
        print("Field calculated successfully.")
        return True
    except arcpy.ExecuteError:
        print(arcpy.GetMessages(2))
        return False


def solve_route(layer_name):
    try:
        arcpy.Solve_na(layer_name, "SKIP", "TERMINATE", None)
        print("Route solved successfully.")
        arcpy.management.SaveToLayerFile(layer_name, folder_path + '\\' + layer_name,'RELATIVE')
        print("Layer saved successfully")
        return True
    except arcpy.ExecuteError:
        print(arcpy.GetMessages(2))
        return False


# Parameters
folder_path = r'C:\\Users\\Administrator\\Documents\\College\\GEOG 676 - GIS Programming\\Group Project'
gdb_name = 'GISProgramming_RouteOptimization.gdb'
network = "https://www.arcgis.com/"


# Add CSVs and their name as variables
# Excel csv path, stops layer name, route name, and new route name (uturns)
excel_csv_path = r'C:\\Users\\Administrator\\Documents\\College\\GEOG 676 - GIS Programming\\Group Project\\ExcelRoute.csv'
excel_stops_layer_name = 'Excel_Stops'
excel_route_name = 'Excel Route'
new_excel_route_name = 'Excel Route No U-Turns'


# Hullabaloo csv path, stops layer name, route name, and new route name (uturns)
hullabaloo_csv_path = r'C:\\Users\\Administrator\\Documents\\College\\GEOG 676 - GIS Programming\\Group Project\\HullabalooRoute.csv'
hullabaloo_stops_layer_name = 'Hullabaloo_Stops'
hullabaloo_route_name = 'Hullabaloo Route'
new_hullabaloo_route_name = 'Hullabaloo Route No U-Turns'


# Matthew Gaines csv path, stops layer name, route name, and new route name (uturns)
matthewgaines_csv_path = r'C:\\Users\\Administrator\\Documents\\College\\GEOG 676 - GIS Programming\\Group Project\\MatthewGainesRoute.csv'
matthewgaines_stops_layer_name = 'MatthewGaines_Stops'
matthewgaines_route_name = 'Matthew Gaines Route'
new_matthewgaines_route_name = 'Matthew Gaines Route No U-Turns'


# Ring Dance csv path, stops layer name, route name, and new route name (uturns)
ringdance_csv_path = r'C:\\Users\\Administrator\\Documents\\College\\GEOG 676 - GIS Programming\\Group Project\\RingDanceRoute.csv'
ringdance_stops_layer_name = 'RingDance_Stops'
ringdance_route_name = 'Ring Dance Route'
new_ringdance_route_name = 'Ring Dance Route No U-Turns'


# Old Army Route csv path, stops layer name, route name, and new route name (uturns)
oldarmy_csv_path = r'C:\\Users\\Administrator\\Documents\\College\\GEOG 676 - GIS Programming\\Group Project\\OldArmyRoute.csv'
oldarmy_stops_layer_name = 'OldArmy_Stops'
oldarmy_route_name = 'Old Army Route'
new_oldarmy_route_name = 'Old Army Route No U-Turns'


# Century Tree Route csv path, stops layer name, route name, and new route name (uturns)
centurytree_csv_path = r'C:\\Users\\Administrator\\Documents\\College\\GEOG 676 - GIS Programming\\Group Project\\CenturyTreeRoute.csv'
centurytree_stops_layer_name = 'CenturyTree_Stops'
centurytree_route_name = 'Century Tree Route'
new_centurytree_route_name = 'Century Tree Route No U-Turns'


# Rudder Route csv path, stops layer name, route name, and new route name (uturns)
rudder_csv_path = r'C:\\Users\\Administrator\\Documents\\College\\GEOG 676 - GIS Programming\\Group Project\\RudderRoute.csv'
rudder_stops_layer_name = 'Rudder_Stops'
rudder_route_name = 'Rudder Route'
new_rudder_route_name = 'Rudder Route No U-Turns'


# Rellis Route csv path, stops layer name, route name, and new route name (uturns)
rellis_csv_path = r'C:\\Users\\Administrator\\Documents\\College\\GEOG 676 - GIS Programming\\Group Project\\RellisRoute.csv'
rellis_stops_layer_name = 'Rellis_Stops'
rellis_route_name = 'Rellis Route'
new_rellis_route_name = 'Rellis Route No U-Turns'


# Fish Camp Route csv path, stops layer name, route name, and new route name (uturns)
fishcamp_csv_path = r'C:\\Users\\Administrator\\Documents\\College\\GEOG 676 - GIS Programming\\Group Project\\FishCampRoute.csv'
fishcamp_stops_layer_name = 'FishCamp_Stops'
fishcamp_route_name = 'Fish Camp Route'
new_fishcamp_route_name = 'Fish Camp Route No U-Turns'


# Elephant Walk Route csv path, stops layer name, route name, and new route name (uturns)
elephantwalk_csv_path = r'C:\\Users\\Administrator\\Documents\\College\\GEOG 676 - GIS Programming\\Group Project\\ElephantWalkRoute.csv'
elephantwalk_stops_layer_name = 'ElephantWalk_Stops'
elephantwalk_route_name = 'Elephant Walk Route'
new_elephantwalk_route_name = 'Elephant Walk Route No U-Turns'


# Create GeoDatabase
gdb_path = create_gdb(folder_path, gdb_name)


# Import CSV to GeoDatabase
excel_bus_stop_points = import_csv_to_gdb(gdb_path, excel_csv_path, excel_stops_layer_name)
hullabaloo_bus_stop_points = import_csv_to_gdb(gdb_path, hullabaloo_csv_path, hullabaloo_stops_layer_name)
matthewgaines_bus_stop_points = import_csv_to_gdb(gdb_path, matthewgaines_csv_path, matthewgaines_stops_layer_name)
ringdance_bus_stop_points = import_csv_to_gdb(gdb_path, ringdance_csv_path, ringdance_stops_layer_name)
oldarmy_bus_stop_points = import_csv_to_gdb(gdb_path, oldarmy_csv_path, oldarmy_stops_layer_name)
centurytree_bus_stop_points = import_csv_to_gdb(gdb_path, centurytree_csv_path, centurytree_stops_layer_name)
rudder_bus_stop_points = import_csv_to_gdb(gdb_path, rudder_csv_path, rudder_stops_layer_name)
rellis_bus_stop_points = import_csv_to_gdb(gdb_path, rellis_csv_path, rellis_stops_layer_name)
fishcamp_bus_stop_points = import_csv_to_gdb(gdb_path, fishcamp_csv_path, fishcamp_stops_layer_name)
elephantwalk_bus_stop_points = import_csv_to_gdb(gdb_path, elephantwalk_csv_path, elephantwalk_stops_layer_name)

# Declare work space to have output into Geodatabase
arcpy.env.workspace = gdb_path


# Make Route Analysis Layer
excelMakeRouteParams = [
    "https://www.arcgis.com/",
    excel_route_name,
    "Driving Time",
    "PRESERVE_BOTH",
    None,
    "UTC",
    "ALONG_NETWORK",
    None,
    "DIRECTIONS",
    "UTC",
    "SKIP"
]


hullabalooMakeRouteParams = [
    "https://www.arcgis.com/",
    hullabaloo_route_name,
    "Driving Time",
    "PRESERVE_BOTH",
    None,
    "UTC",
    "ALONG_NETWORK",
    None,
    "DIRECTIONS",
    "UTC",
    "SKIP"
]


matthewgainesMakeRouteParams = [
    "https://www.arcgis.com/",
    matthewgaines_route_name,
    "Driving Time",
    "PRESERVE_BOTH",
    None,
    "UTC",
    "ALONG_NETWORK",
    None,
    "DIRECTIONS",
    "UTC",
    "SKIP"
]


ringdanceMakeRouteParams = [
    "https://www.arcgis.com/",
    ringdance_route_name,
    "Driving Time",
    "PRESERVE_BOTH",
    None,
    "UTC",
    "ALONG_NETWORK",
    None,
    "DIRECTIONS",
    "UTC",
    "SKIP"
]


oldarmyMakeRouteParams = [
    "https://www.arcgis.com/",
    oldarmy_route_name,
    "Driving Time",
    "PRESERVE_BOTH",
    None,
    "UTC",
    "ALONG_NETWORK",
    None,
    "DIRECTIONS",
    "UTC",
    "SKIP"
]

centurytreeMakeRouteParams = [
    "https://www.arcgis.com/",
    centurytree_route_name,
    "Driving Time",
    "PRESERVE_BOTH",
    None,
    "UTC",
    "ALONG_NETWORK",
    None,
    "DIRECTIONS",
    "UTC",
    "SKIP"
]

rudderMakeRouteParams = [
    "https://www.arcgis.com/",
    rudder_route_name,
    "Driving Time",
    "PRESERVE_BOTH",
    None,
    "UTC",
    "ALONG_NETWORK",
    None,
    "DIRECTIONS",
    "UTC",
    "SKIP"
]

rellisMakeRouteParams = [
    "https://www.arcgis.com/",
    rellis_route_name,
    "Driving Time",
    "PRESERVE_BOTH",
    None,
    "UTC",
    "ALONG_NETWORK",
    None,
    "DIRECTIONS",
    "UTC",
    "SKIP"
]

fishcampMakeRouteParams = [
    "https://www.arcgis.com/",
    fishcamp_route_name,
    "Driving Time",
    "PRESERVE_BOTH",
    None,
    "UTC",
    "ALONG_NETWORK",
    None,
    "DIRECTIONS",
    "UTC",
    "SKIP"
]

elephantwalkMakeRouteParams = [
    "https://www.arcgis.com/",
    elephantwalk_route_name,
    "Driving Time",
    "PRESERVE_BOTH",
    None,
    "UTC",
    "ALONG_NETWORK",
    None,
    "DIRECTIONS",
    "UTC",
    "SKIP"
]

# Excel Route Creation
if make_excel_route_analysis_layer(excelMakeRouteParams):
    # Add Locations to Route
    if add_locations_to_route(new_excel_route_name, excel_bus_stop_points):
        # Calculate Field
        if calculate_field(new_excel_route_name, "CurbApproach", 1, "PYTHON3", "TEXT"):
            # Solve Route
            solve_route(new_excel_route_name)


# Hullabaloo Route Creation
if make_hullabaloo_route_analysis_layer(hullabalooMakeRouteParams):
    # Add Locations to Route
    if add_locations_to_route(new_hullabaloo_route_name, hullabaloo_bus_stop_points):
        # Calculate Field
        if calculate_field(new_hullabaloo_route_name, "CurbApproach", 1, "PYTHON3", "TEXT"):
            # Solve Route
            solve_route(new_hullabaloo_route_name)


# Matthew Gaines Route Creation
if make_matthewgaines_route_analysis_layer(matthewgainesMakeRouteParams):
    # Add Locations to Route
    if add_locations_to_route(new_matthewgaines_route_name, matthewgaines_bus_stop_points):
        # Calculate Field
        if calculate_field(new_matthewgaines_route_name, "CurbApproach", 1, "PYTHON3", "TEXT"):
            # Solve Route
            solve_route(new_matthewgaines_route_name)


# Ring Dance Route Creation
if make_ringdance_route_analysis_layer(ringdanceMakeRouteParams):
    # Add Locations to Route
    if add_locations_to_route(new_ringdance_route_name, ringdance_bus_stop_points):
        # Calculate Field
        if calculate_field(new_ringdance_route_name, "CurbApproach", 1, "PYTHON3", "TEXT"):
            # Solve Route
            solve_route(new_ringdance_route_name)


# Old Army Route Creation
if make_oldarmy_route_analysis_layer(oldarmyMakeRouteParams):
    # Add Locations to Route
    if add_locations_to_route(new_oldarmy_route_name, oldarmy_bus_stop_points):
        # Calculate Field
        if calculate_field(new_oldarmy_route_name, "CurbApproach", 1, "PYTHON3", "TEXT"):
            # Solve Route
            solve_route(new_oldarmy_route_name)

# Century Tree Route Creation
if make_centurytree_route_analysis_layer(centurytreeMakeRouteParams):
    # Add Locations to Route
    if add_locations_to_route(new_centurytree_route_name, centurytree_bus_stop_points):
        # Calculate Field
        if calculate_field(new_centurytree_route_name, "CurbApproach", 1, "PYTHON3", "TEXT"):
            # Solve Route
            solve_route(new_centurytree_route_name)

# Rudder Route Creation
if make_rudder_route_analysis_layer(rudderMakeRouteParams):
    # Add Locations to Route
    if add_locations_to_route(new_rudder_route_name, rudder_bus_stop_points):
        # Calculate Field
        if calculate_field(new_rudder_route_name, "CurbApproach", 1, "PYTHON3", "TEXT"):
            # Solve Route
            solve_route(new_rudder_route_name)

# Rellis Route Creation
if make_rellis_route_analysis_layer(rellisMakeRouteParams):
    # Add Locations to Route
    if add_locations_to_route(new_rellis_route_name, rellis_bus_stop_points):
        # Calculate Field
        if calculate_field(new_rellis_route_name, "CurbApproach", 1, "PYTHON3", "TEXT"):
            # Solve Route
            solve_route(new_rellis_route_name)

# Fish Camp Route Creation
if make_fishcamp_route_analysis_layer(fishcampMakeRouteParams):
    # Add Locations to Route
    if add_locations_to_route(new_fishcamp_route_name, fishcamp_bus_stop_points):
        # Calculate Field
        if calculate_field(new_fishcamp_route_name, "CurbApproach", 1, "PYTHON3", "TEXT"):
            # Solve Route
            solve_route(new_fishcamp_route_name)

# Elephant Walk Route Creation
if make_elephantwalk_route_analysis_layer(elephantwalkMakeRouteParams):
    # Add Locations to Route
    if add_locations_to_route(new_elephantwalk_route_name, elephantwalk_bus_stop_points):
        # Calculate Field
        if calculate_field(new_elephantwalk_route_name, "CurbApproach", 1, "PYTHON3", "TEXT"):
            # Solve Route
            solve_route(new_elephantwalk_route_name)