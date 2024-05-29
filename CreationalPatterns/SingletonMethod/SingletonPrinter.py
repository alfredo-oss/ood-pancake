import threading

class PrinterService:
    _instance_lock = threading.Lock() # This is used to ensure that the instance is thread safe
    _unique_instance = None # The unique instance

    def __new__(cls):
        with cls._instance_lock:
            if cls._unique_instance is None:
                cls._unique_instance = super(PrinterService, cls).__new__(cls)
                cls._unique_instance._init_printer_service()

        return cls._unique_instance
    
    def _init_printer_service(self):
        self.mode = "GrayScale"

    def get_printer_status(self):
        return self.mode
    
    def set_mode(self, mode):
        self.mode = mode
        print(f"Mode changed to {mode}")

worker1 = PrinterService() # Worker one initializes the machine
worker2 = PrinterService() # Worker two does not instantiates a new instance just receives the instance it was previously instantiated.

worker1.set_mode("Color") # Worker one sets the global status 
worker2.set_mode("Grayscale") # Worker 2 sets the global status

worker1_mode = worker1.get_printer_status() # This will retrieve the last status that was set
worker2_mode = worker2.get_printer_status() # This will retrieve the last status that was set

print(worker1_mode)
print(worker2_mode)
