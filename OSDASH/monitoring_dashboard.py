# Import Libraries
import psutil
import platform
from flask import Flask, render_template

# Initialize Flask App
app = Flask(__name__)

# Create Route for Dashboard
@app.route('/')
def dashboard():
    # Collect system information
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    # Collect process information
    processes = psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])
    process_list = [{'pid': process.info['pid'], 'name': process.info['name'],
                     'cpu_percent': process.info['cpu_percent'], 'memory_percent': process.info['memory_percent']} for process in processes]

    # Top Processes
    top_cpu_processes = sorted(process_list, key=lambda x: x['cpu_percent'], reverse=True)[:5]
    top_memory_processes = sorted(process_list, key=lambda x: x['memory_percent'], reverse=True)[:5]

    # Process Status (Example: Check if a process named "example_process" is running)
    example_process_running = any(process['name'] == 'example_process' for process in process_list)

    # Security Alerts (Example: Placeholder for security alerts)
    security_alerts = ["Alert: Suspicious activity detected!", "Warning: Unauthorized access attempt!"]

    # System Updates
    system_updates = "No updates available"  # Placeholder for system updates information

    # Update Status (Example: Placeholder for update status)
    up_to_date = True  # Set to False if updates are not up-to-date

    # Server Hardware Information
    cpu_info = platform.processor()
    ram_info = psutil.virtual_memory().total

    # Render the dashboard template with collected information
    return render_template('dashboard.html', cpu_percent=cpu_percent, memory_info=memory_info,
                           disk_info=disk_info, process_list=process_list, network_info=psutil.net_io_counters(),
                           top_cpu_processes=top_cpu_processes, top_memory_processes=top_memory_processes,
                           example_process_running=example_process_running,
                           security_alerts=security_alerts, system_updates=system_updates, up_to_date=up_to_date,
                           cpu_info=cpu_info, ram_info=ram_info)

# Create HTML Template
# Save this HTML code in a file named 'dashboard.html' in a folder named 'templates'

# Run the Flask App
if __name__ == '__main__':
    app.run(debug=True)
