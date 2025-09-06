class InMemoryStorage:
    def __init__(self):
        self.storage = {}

    def upload_file(self, path: str, content: str) -> None:
        """Upload or overwrite a file in storage."""
        self.storage[path] = content
        print(f"📁 Uploaded: {path}")

    def read_file(self, path: str) -> str:
        """Retrieve file content by path."""
        if path not in self.storage:
            print(f"❌ File not found: {path}")
            return None
        print(f"📖 Reading: {path}")
        return self.storage[path]

    def delete_file(self, path: str) -> None:
        """Delete file if it exists."""
        if path in self.storage:
            del self.storage[path]
            print(f"🗑️ Deleted: {path}")
        else:
            print(f"❌ File not found: {path}")

    def list_files(self) -> None:
        """List all stored files."""
        if not self.storage:
            print("📂 Storage is empty.")
        else:
            print("📂 Files in storage:")
            for path in self.storage.keys():
                print(f"  - {path}")


# --- Simulation Example ---
if __name__ == "__main__":
    fs = InMemoryStorage()

    # Upload files
    fs.upload_file("users/profile1.png", "binary-data-profile1")
    fs.upload_file("docs/invoice1.pdf", "pdf-binary-content")
    fs.upload_file("reports/2025/report.txt", "Report content here...")

    # List files
    fs.list_files()

    # Read a file
    content = fs.read_file("docs/invoice1.pdf")
    print("File Content:", content)

    # Delete a file
    fs.delete_file("users/profile1.png")

    # List again
    fs.list_files()
