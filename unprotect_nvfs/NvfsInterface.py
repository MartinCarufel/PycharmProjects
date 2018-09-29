import clr
import sys
clr.AddReferenceToFileAndPath(r'.\DLLs\NVFSLibrary.dll')
import NVFSLibrary

class NvfsInterface:

    nvfs_communicator = None

    port_name = None

    @staticmethod
    def _get_communicator(module_id = ""):
        """Creates and gets the NVFS communicator based on module ID (or none)"""
        if(module_id == ""):
            if(NvfsInterface.nvfs_communicator == None):
                NvfsInterface.nvfs_communicator = NVFSLibrary.NVFSCommunicator()
        else:
            if(NvfsInterface.nvfs_communicator == None):
                NvfsInterface.nvfs_communicator = NVFSLibrary.NVFSCommunicator(module_id)

        NvfsInterface.port_name = NvfsInterface.nvfs_communicator.PortName
        
        return NvfsInterface.nvfs_communicator

    @staticmethod  
    def nvfs_read(name, module_id = ""):
        """Read an NVFS variable and returns the data in an hex formatted string"""
        return NvfsInterface._nvfs_read(name, module_id).DataNVFSHex

    @staticmethod
    def nvfs_read_ascii(name, module_id = ""):
        """Read an NVFS variable and returns the data in an ASCII string (mostly used for VIN)"""
        return NvfsInterface._nvfs_read(name, module_id).DataNVFSString

    @staticmethod
    def _nvfs_read(name, module_id = ""):
        """Reads an NVFS variable and returns the NVFS Entry object"""
        communicator = NvfsInterface._get_communicator(module_id)
        return communicator.ReadNVFS(name)

    @staticmethod
    def nvfs_write(name, data, module_id = ""):
        """Writes an NVFS variable. data is an hex formatted string"""
        NvfsInterface._nvfs_write(name, data, True, module_id)

    @staticmethod
    def nvfs_write_ascii(name, data, module_id = ""):
        """Writes an NVFS variable. data is an ascii encoded string"""
        NvfsInterface._nvfs_write(name, data, False, module_id)

    @staticmethod
    def _nvfs_write(name, data, hex, module_id = ""):
        """
        Writes an NVFS variable.
        data is either an hex formatted string or ascii encoded string based on the boolean hex param
        """
        communicator = NvfsInterface._get_communicator(module_id)
        entry = NVFSLibrary.NVFSEntry(name, data, hex)
        communicator.WriteNVFS(entry)

    @staticmethod
    def nvfs_delete(name, module_id = ""):
        """Deletes an NVFS variable"""
        communicator = NvfsInterface._get_communicator(module_id)
        communicator.DeleteNVFS(name, True)

    @staticmethod
    def nvfs_reset(module_id = ""):
        """Resets the NVFS and deletes all variables that are not in the blocked master list to delete"""
        communicator = NvfsInterface._get_communicator(module_id)
        communicator.DeleteAllExcepted()

    @staticmethod
    def nvfs_dump(module_id = ""):
        """Dumps all the NVFS entry and returns a dictionary of NVFS Entry"""
        communicator = NvfsInterface._get_communicator(module_id)
        return communicator.DumpNVFS()
        
    @staticmethod
    def nvfs_dump_print(module_id = ""):
        """Prints all the variables from a dump and returns the dump in a Dictionary of NVFSEntry"""
        dump = NvfsInterface.nvfs_dump(module_id)
        for entry in dump.Values:
            print entry.ToString()
        return dump

    @staticmethod
    def nvfs_get_all_variables(module_id = ""):
        """Returns a list of all the NVFS variable names"""
        communicator = NvfsInterface._get_communicator(module_id)
        return communicator.GetAllNVFSVariableName()
       
    @staticmethod 
    def nvfs_print_all_variables(module_id = ""):
        """Prints the name of all the NVFS variables and returns a list containing all the names"""
        variables = NvfsInterface.nvfs_get_all_variables(module_id)
        for variable in variables:
            print(variable)
        return variables

    @staticmethod
    def nvfs_get_firmware_name(module_id = ""):
        """Gets and returns the firmware name"""
        communicator = NvfsInterface._get_communicator(module_id)
        return communicator.GetFirmwareName()

    @staticmethod
    def nvfs_get_firmware_version(module_id = ""):
        """Gets and returns the firmware version"""
        communicator = NvfsInterface._get_communicator(module_id)
        return communicator.GetFirmwareVersion()

    @staticmethod
    def nvfs_get_firmware_info(module_id = ""):
        """Gets and return firmware info. Some firmwares don't have info in this field"""
        communicator = NvfsInterface._get_communicator(module_id)
        return communicator.GetFirmwareInfo()

    @staticmethod
    def nvfs_set_write_protected(name, module_id = ""):
        """Sets a variable write-protected"""
        communicator = NvfsInterface._get_communicator(module_id)
        communicator.SetAttributNVFS(name, True)

    @staticmethod
    def nvfs_remove_write_protected(name, module_id = ""):
        """Removes the write-protected status on a variable"""
        communicator = NvfsInterface._get_communicator(module_id)
        communicator.SetAttributNVFS(name, False)

    @staticmethod
    def nvfs_get_write_protected(name, module_id = ""):
        """Gets and returns if a variable is write-protected"""
        communicator = NvfsInterface._get_communicator(module_id)
        return communicator.GetAttributNVFS(name)

    @staticmethod
    def nvfs_get_tag(module_id = ""):
        """Returns the tag of the module"""
        communicator = NvfsInterface._get_communicator(module_id)
        return communicator.TrustNVFS()

    @staticmethod
    def nvfs_flash(pathEncFile, module_id = ""):
        """Flashes an .enc file to the module"""
        communicator = NvfsInterface._get_communicator(module_id)
        communicator.FlashModule(pathEncFile)

    @staticmethod
    def nvfs_write_vin(vin, module_id = ""):
        """Writes the FW_NAME,VIN variable to the module"""
        name = NvfsInterface._nvfs_get_vin_variable_name(module_id)
        NvfsInterface.nvfs_write_ascii(name, vin.upper(), module_id);

    @staticmethod
    def nvfs_read_vin(module_id = ""):
        """Returns the VIN in the module"""
        name = NvfsInterface._nvfs_get_vin_variable_name(module_id)
        return NvfsInterface.nvfs_read_ascii(name, module_id)

    @staticmethod
    def _nvfs_get_vin_variable_name(module_id = ""):
        """Returns the VIN variable names based on the firmware's name on the module"""
        name = NvfsInterface.nvfs_get_firmware_name(module_id)
        return name + ",VIN"

    @staticmethod
    def nvfs_delete_all_except(module_id = ""):
        """Creates the master list and deletes all the NVFS variables except the ones in the master_list"""
        master_list = "PLATFORM|HW_VER|HW_ID|BOOT_VER|SERNUM|ID|SYS_TYPE|SYS_TYPE_FACTORY"
        NvfsInterface._nvfs_delete_all_except(master_list, module_id)

    @staticmethod
    def port_name(module_id = ""):
        """ Return the name of COM port from the module is connected"""

        communicator = NvfsInterface._get_communicator( module_id = "")
        return  NvfsInterface.nvfs_communicator.PortName

    @staticmethod
    def _nvfs_delete_all_except(master_list, module_id = ""):
        """Deletes all the NVFS variables except the ones in the master_list"""
        dump = NvfsInterface.nvfs_dump(module_id)
        except_list = master_list.split('|')
        for key in dump.Keys:
            if key not in except_list:
                try:
                    NvfsInterface.nvfs_delete(key)
                except NVFSLibrary.NVFSResultException as inst:
                    if inst.ErrorCode == 2:
                        NvfsInterface.nvfs_remove_write_protected(key, module_id)
                        NvfsInterface.nvfs_delete(key)
                    else:
                        throw(inst)
