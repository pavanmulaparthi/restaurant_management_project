import time
import random

class TaskQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, task):
        """Add task to the queue."""
        self.queue.append(task)
        print(f"Task added: {task}")

    def dequeue(self):
        """Remove and return the next task (FIFO)."""
        if self.is_empty():
            print("Queue is empty, no task to process.")
            return None
        task = self.queue.pop(0)  # remove from front
        print(f"Processing task: {task}")
        return task

    def peek(self):
        """See the next task without removing it."""
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        """Check if queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return number of tasks in queue."""
        return len(self.queue)


# --- Simulation Example ---
if __name__ == "__main__":
    tq = TaskQueue()

    # Add tasks to queue
    for i in range(5):
        tq.enqueue(f"Task-{i+1}")

    print("\nStarting background task processing...\n")

    # Process tasks
    while not tq.is_empty():
        current_task = tq.dequeue()
        # Simulate processing time
        time.sleep(random.uniform(0.5, 1.5))
        print(f"✅ Completed: {current_task}\n")

    print("All tasks processed!")
