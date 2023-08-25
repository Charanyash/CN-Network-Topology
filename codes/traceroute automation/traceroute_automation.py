import subprocess

# Read destination addresses from destination.txt
with open("destinations.txt", "r") as f:
    destinations = f.read().splitlines()
source = "JapanVPN"
#source cant be automated we need to change accordingly


# Perform tracert for each destination and save results to separate files
for destination in destinations:
    tracert_command = ["tracert","-4", destination]
    
    try:
        result = subprocess.run(tracert_command, stdout=subprocess.PIPE, text=True, check=True)
        output_filename = f"{source}_{destination.replace('.', '_')}.txt"
        
        lines = result.stdout.splitlines()
        print(lines[0])
        lines = lines[5:-1]  # Skip the first five lines and the last line
        
        with open(output_filename, "w") as output_file:
            # output_file.write(f"Tracert for destination: {destination}\n")
            output_file.write("\n".join(lines))
            
        print(f"Tracert completed for destination {destination}, results saved to {output_filename}")
    except subprocess.CalledProcessError:
        print(f"Error executing tracert for destination: {destination}")
