class Class:
    def __init__(self, id, start, end):
        self.id = id
        self.start = start
        self.end = end

def schedule_classes(classes):
    classes.sort(key=lambda x: x.end)  # Sort classes by end time
    scheduled_classes = []
    while classes:
        selected_class = classes.pop(0)  # Select the class with the earliest end time
        scheduled_classes.append(selected_class)
        classes = [c for c in classes if c.start >= selected_class.end]  # Remove conflicting classes
    return scheduled_classes

def display_schedule(scheduled_classes):
    print("Scheduled classes:")
    for cls in scheduled_classes:
        print(f"Class ID: {cls.id}, Start Time: {cls.start}, End Time: {cls.end}")

def input_class():
    classes = []
    num_classes = int(input("Enter the number of classes to schedule: "))
    for i in range(num_classes):
        class_id = input("Enter class ID: ")
        start_time = input("Enter start time (e.g., 9:00 AM): ")
        end_time = input("Enter end time (e.g., 12:30 AM): ")
        classes.append(Class(class_id, start_time, end_time))
    return classes

if __name__ == "__main__":
    print("Welcome to the Class Scheduling System!")
    classes = input_class()
    scheduled_classes = schedule_classes(classes)
    display_schedule(scheduled_classes)

