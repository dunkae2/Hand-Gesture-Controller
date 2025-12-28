#!/bin/bash

# Get current brightness
current=$(brightness -l | grep brightness | awk '{print $4}')

# Step value (change as needed)
step=0.1

# Calculate new brightness (capped at 1.0)
new=$(echo "$current + $step" | bc)
if (( $(echo "$new > 1.0" | bc -l) )); then
  new=1.0
fi

# Apply new brightness
brightness $new
