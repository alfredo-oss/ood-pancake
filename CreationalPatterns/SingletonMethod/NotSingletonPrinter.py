"""
The following class shows the design of a straightforward
PrintService class. Any computer could create an instance 
when it needs to print or check the printer status.
"""

class PrintService:
    def __init__(self):
        self.print_queue = []
    
    def send_document(self, doc):
        self.print_queue.append(doc)
    
    def get_printer_status(self):
        pass

    def _print_next(self) -> str:
        document = self.print_queue[0]
        self.print_queue.pop(0)
        return document

print_service = PrintService()
print_service.send_document("ubiluc")
print_service.send_document("bingalac")
print_service.send_document("chalabum")
print_service.send_document("kubisun")
print_service.send_document("bangalasin")
print(print_service._print_next())
print(print_service._print_next())
print(print_service._print_next())
print(print_service._print_next())
