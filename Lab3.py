from collections import deque

class Ticket:
    def __init__(self, customer_name, issue, priority=False):
        self.customer_name = customer_name
        self.issue = issue
        self.priority = priority

    def __str__(self):
        return f"{'[URGENT] ' if self.priority else ''}{self.customer_name}: {self.issue}"

class TicketingSystem:
    def __init__(self):
        self.regular_queue = deque()
        self.priority_queue = deque()
    
    def submit_ticket(self, customer_name, issue, priority=False):
        ticket = Ticket(customer_name, issue, priority)
        if priority:
            self.priority_queue.append(ticket)
        else:
            self.regular_queue.append(ticket)
        print(f"Ticket submitted: {ticket}")
    
    def display_tickets(self):
        if not self.priority_queue and not self.regular_queue:
            print("No pending tickets.")
            return
        print("\nPending Tickets:")
        for ticket in list(self.priority_queue) + list(self.regular_queue):
            print(ticket)
    
    def process_ticket(self):
        if self.priority_queue:
            ticket = self.priority_queue.popleft()
        elif self.regular_queue:
            ticket = self.regular_queue.popleft()
        else:
            print("No tickets to process.")
            return
        print(f"Processing ticket: {ticket}")

# Example usage
def main():
    system = TicketingSystem()
    
    while True:
        print("\n1. Submit Ticket\n2. View Tickets\n3. Process Ticket\n4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter your name: ")
            issue = input("Describe your issue: ")
            priority = input("Is this urgent? (yes/no): ").strip().lower() == 'yes'
            system.submit_ticket(name, issue, priority)
        elif choice == '2':
            system.display_tickets()
        elif choice == '3':
            system.process_ticket()
        elif choice == '4':
            print("Exiting ticketing system.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
