# prepared import of enumerations
from model import Color, FuelType, Manufacturer, Transmission, Vehicle
# prepared csv module import
import csv
from typing import List

class VehicleFileManager:
    def __init__(self, file_path):
        self.file_path = file_path

        

    def import_vehicles_from_file(self, file_path):
        # TODO read vehicle-list.csv and transform to String array
            vehicle_list = []
            with open(self.file_path,mode='r' , newline='') as file_path:
                csv_reader = csv.reader(file_path)
                for row in csv_reader:
                    vehicle_list.append(row)
            return vehicle_list

    def rewrite_file(self, vehicle_list):
        # TODO write back into vehicle-list.csv and transform to String array
        
         print(vehicle_list)
         with open(self.file_path, mode='w', newline='') as vehicle_file:
            csv_writer = csv.writer(vehicle_file)
            for vehicle in vehicle_list: 
                if isinstance(vehicle, Vehicle):
                    vehicle_list = self.prepare_the_vehicle_for_rewriting(vehicle.get_id , vehicle)
                    csv_writer.writerow(vehicle_list)

    def prepare_the_vehicle_for_rewriting(self, vehicle_string_for_rewrite, vehicle):
        vehicle_values = [
            str(vehicle.get_id()),
            str(vehicle.get_manufacturer()),
            str(vehicle.get_model()),
            str(vehicle.get_horsePower()),
            str(vehicle.get_price()),
            str(vehicle.get_color()),
            str(vehicle.get_mileage()),
            str(vehicle.get_productionYear()),          
            str(vehicle.get_fuelType()),
            str(vehicle.get_transmission())
        ]
        vehicle_string_for_rewrite = "".join(vehicle_values)
        return vehicle_string_for_rewrite

class VehicleShopPrinter:
    
    def print_available_vehicles(self, vehicle_list):
        # Check if the vehicle list is empty or None
        if not vehicle_list:
            print("No vehicles available.")
            return
        
        # Print header
        header = f"{'ID':<2} | {'Manufacturer':<14} | {'Model':<10} | {'Horse Power':<10} | {'Mileage':<9} | {'Color':<8}  |  {'Price':<6}  | {'ProductionYear':<5} | {'Fuel Type':<14} | {'Transmission':<15}  "
        print(header)
        print("=" * len(header))
        
        # Print each vehicle's details
        for vehicle in vehicle_list:
            if isinstance(vehicle, Vehicle):
                vehicle_details = f"{vehicle.get_id():<2} | {vehicle.get_manufacturer():<14} | {vehicle.get_model():<10} | {vehicle.get_horsePower():<11} | {vehicle.get_mileage():<8}  | {vehicle.get_price():<9}  | {vehicle.get_productionYear():<6} | {vehicle.get_color():<13}   | {vehicle.get_fuelType():<15} | {vehicle.get_transmission():<18} "
            print(vehicle_details)  
       
    
    def print_vehicle_sold_message(self, vehicle_chosen_id):
        print("\nVehicle with ID", vehicle_chosen_id, "was sold.")
    
    def print_vehicle_id_to_sell_message(self):
        print("\n\n Please enter the number (ID) of the vehicle you want to sell: ")



class VehicleShopProcessor:

    # responsible to sell a specified vehicle by id

    def sell_vehicle(self, vehicle_list, selected_vehicle_id):
    # TODO selling a vehicle means to remove it from the available vehicle list
    
        for vehicle in vehicle_list:
            if vehicle.id == selected_vehicle_id:
                vehicle_list.remove(vehicle)
                return vehicle

class VehicleTransformer:

    # transforms a data array into a {@link Vehicle} list 
	# @param vehicle data array
	# @return list of {@link Vehicle} objects

    def transform_data_as_string_array_to_vehicle_objects(self, vehicles_as_string_array: List[str]) -> List[Vehicle]:
        # Convert and extract each attribute from the array
        try:

            # TODO take data from String list and transform to list of vehicle objects
            id = int(vehicles_as_string_array[0])
            manufacturer = vehicles_as_string_array[1]  # Example: Capitalize manufacturer name
            model = vehicles_as_string_array[2]
            horsePower = vehicles_as_string_array[3]
            price = vehicles_as_string_array[4]
            color = vehicles_as_string_array[5]
            mileage = int(vehicles_as_string_array[6])
            productionYear = int(vehicles_as_string_array[7])
            fuelType = vehicles_as_string_array[8]
            transmission = vehicles_as_string_array[9]

            return (id,manufacturer, model, horsePower, price, color, mileage, productionYear, fuelType, transmission)
        except ValueError as e:
            print(f"ValueError: {e}")
            raise
        except IndexError as e:
            print(f"IndexError: {e}")
            raise

        # TODO call method transformToVehicleObject
    def transform_data_as_string_array_to_vehicle_objects(self, vehicles_as_string_array: List[List[str]]) -> List[Vehicle]:
        vehicles = []
        
        for vehicle_array in vehicles_as_string_array:
            try:
                vehicle = self.transform_to_vehicle_object(vehicle_array)
                vehicles.append(vehicle)
            except (ValueError, IndexError) as e:
                print(f"Skipping invalid data: {vehicle_array} - {e}")
        
        return vehicles

    # transforms a vehicle data record as String into a {@link Vehicle} object
	# @param vehicle data record as String 
	# @return {@link Vehicle} object 
    
    def transform_to_vehicle_object(self, vehicle_as_string_array: str) -> Vehicle: 
        # TODO transform the vehicle as string into a vehicle object
        
        id = int(vehicle_as_string_array[0])
        manufacturer =str(vehicle_as_string_array[1])
        model = str(vehicle_as_string_array[2])
        horsePower = int(vehicle_as_string_array[3])
        price = int(vehicle_as_string_array[4])
        color = str(vehicle_as_string_array[5])
        mileage = int(vehicle_as_string_array[6])
        productionYear = int(vehicle_as_string_array[7])
        fuelType = str(vehicle_as_string_array[8])
        transmission = str(vehicle_as_string_array[9])

        vehicle = Vehicle(id, manufacturer, model, horsePower, price, color, mileage, productionYear, fuelType, transmission)
        return vehicle
    
    # Example for Enumeration processing to use for all other Enumerations
    def get_manufacturer_from_string(self, manufacturer_as_string):
        for manufacturer in Manufacturer:
            if manufacturer.name == manufacturer_as_string:
                return manufacturer
            
        raise ValueError("Manufacturer not supported: " + manufacturer_as_string)
    
    def get_color_from_string(self, color_from_string):
        for color in Color:
            if color.name == color_from_string:
                return color
            
        raise ValueError("Color not supported: " + color_from_string)
    
    def get_fuel_type_from_string(self, fuel_type_from_string):
        for fuel_type in FuelType:
            if fuel_type.name == fuel_type_from_string:
                return fuel_type
            
        raise ValueError("Fuel type not supported: " + fuel_type_from_string)
    
    def get_transmission_from_string(self, transmission_from_string):
        for transmission in Transmission:
            if transmission.name == transmission_from_string:
                return transmission
            
        raise ValueError("Transmission not supported: " + transmission_from_string)
    
    


