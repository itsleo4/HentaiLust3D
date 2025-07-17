import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class AutoGitPushHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.event_type in ['modified', 'created', 'deleted']:
            print("📦 Detected change. Pushing to GitHub...")
            try:
                subprocess.run(["git", "add", "."], check=True)
                subprocess.run(["git", "commit", "-m", "🔥 Auto-push on file change"], check=True)
                subprocess.run(["git", "push", "origin", "main"], check=True)
                print("✅ Code pushed successfully!")
            except subprocess.CalledProcessError:
                print("⚠️ Nothing to commit or push failed.")

if __name__ == "__main__":
    path = "."  # Watch current directory
    event_handler = AutoGitPushHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=True)
    observer.start()
    print("🔁 Auto Git push started. Watching for changes...")

    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
